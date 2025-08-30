import os.path
import traceback

from path_dict import PathDict
from core import lingoIO
import json
import ujson  # just for json to be more compact and fast
from core import info
from core.Exceptions import *
from core.HistorySystem import History
from core.Level.LevelPart import LevelPart
from core.Level.CustomLevelData import CustomLevelData
from PySide6.QtCore import QPoint, Slot, QRect, QSize
from core.HistorySystem import HistoryElement, MultiHistoryElement

defaultlevel = open(os.path.join(info.PATH_FILES, "default.txt"), "r").read()
minimallevel = open(os.path.join(info.PATH_FILES, "minimal.txt"), "r").read()
defaultlevellines = defaultlevel.split("\n")
minimallevellines = minimallevel.split("\n")


class RWELevel:
    def __init__(self, manager, file=None):
        from BaseMod.LevelParts import GeoLevelPart, TileLevelPart, EffectLevelPart, PropLevelPart, CameraLevelPart, InfoLevelPart, LightLevelPart
        self.manager = manager
        self.file = file
        self.lightdata = None
        if file is not None:
            self.openfile(file)
        else:
            self.data = RWELevel.turntoproject(defaultlevel)
        self.history = History(self)
        self.viewport = None
        self.levelparts: dict[str, LevelPart] = {}
        self.mount_levelparts()

        # quick access stuff
        self.l_info: InfoLevelPart = self.levelparts["info"]
        self.l_geo: GeoLevelPart = self.levelparts["geo"]
        self.l_tiles: TileLevelPart = self.levelparts["tiles"]
        self.l_effects: EffectLevelPart = self.levelparts["effects"]
        self.l_props: PropLevelPart = self.levelparts["props"]
        self.l_cameras: CameraLevelPart = self.levelparts["camera"]
        self.l_light: LightLevelPart = self.levelparts["light"]

        self.custom_level_data = CustomLevelData(self)

        self.was_resized = False

    def level_resized(self, newrect: QRect):
        elements: list[HistoryElement] = []
        for i in self.levelparts.values():
            element = i.level_resized(newrect)
            if element is None:
                continue
            elements.append(element)
        self.add_history(MultiHistoryElement, elements)
        if self.viewport is None:
            return
        for i in self.viewport.modules:
            i.level_resized(newrect)

    def mount_levelparts(self):
        if self.manager is None:
            return
        for i in self.manager.mods:
            i.mount_levelparts(self)

    @Slot()
    def undo(self):
        self.history.undo()

    @Slot()
    def redo(self):
        self.history.redo()

    def add_history(self, historytype, *args, **kwargs):
        self.history.add_element(historytype(self.history, *args, **kwargs))

    @property
    def last_history_element(self):
        return self.history.last_element

    @property
    def shortname(self):
        if self.file is None:
            return "Unnamed"
        return os.path.split(self.file)[1]

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    @property
    def level_rect(self) -> QRect:
        return QRect(0, 0, self.level_width, self.level_height)

    @property
    def extra_tiles(self) -> list[int]:
        return self.l_info.extra_tiles

    def inside(self, point: QPoint) -> bool:
        return 0 <= point.x() < self.level_width and 0 <= point.y() < self.level_height

    def inside_border(self, point: QPoint) -> bool:
        borders = self.extra_tiles
        topleft = QPoint(borders[0], borders[1])
        bottomright = self.level_size - QPoint(borders[2], borders[3])
        rect = QRect(topleft, bottomright)
        return rect.contains(point)

    @property
    def level_width(self) -> int:
        if hasattr(self, "l_geo"):
            return self.l_geo.width
        return self.levelparts["geo"].width

    @property
    def level_height(self) -> int:
        if hasattr(self, "l_geo"):
            return self.l_geo.height
        return self.levelparts["geo"].height

    @property
    def level_size(self) -> QPoint:
        return QPoint(self.level_width, self.level_height)

    @property
    def level_size_qsize(self) -> QSize:
        return QSize(self.level_width, self.level_height)

    @property
    def changed(self):
        return len(self.history.undoactions) > 0

    def turntolingo(self, file):
        with file as fl:
            fl.write(str(self["GE"]) + "\r")
            fl.write(lingoIO.tolingo(self["TE"]) + "\r")
            fl.write(lingoIO.tolingo(self["FE"]) + "\r")
            fl.write(lingoIO.tolingo(self["LE"]) + "\r")
            fl.write(lingoIO.tolingo(self["EX"]) + "\r")
            fl.write(lingoIO.tolingo(self["EX2"]) + "\r")
            fl.write(lingoIO.tolingo(self["CM"]) + "\r")
            fl.write(lingoIO.tolingo(self["WL"]) + "\r")
            fl.write(lingoIO.tolingo(self["PR"]) + "\r")
            if self.data.get("CLD") is not None:
                fl.write(lingoIO.tolingo(self["CLD"]) + "\r")

    @staticmethod
    def turntoproject(string: str) -> PathDict:
        proj = {}
        lines = string.split("\n")
        proj["GE"] = json.loads(lines[0])  # geometry
        proj["TE"] = lingoIO.tojson(lines[1])  # tile editor and his settings
        proj["FE"] = lingoIO.tojson(lines[2])  # effect editor params
        proj["LE"] = lingoIO.tojson(lines[3], defaultlevellines[3])  # light editor and presets
        proj["EX"] = lingoIO.tojson(lines[4], defaultlevellines[4])  # map settings
        proj["EX2"] = lingoIO.tojson(lines[5], defaultlevellines[5])  # light and level settings
        proj["CM"] = lingoIO.tojson(lines[6], defaultlevellines[6])  # camera settings
        proj["WL"] = lingoIO.tojson(lines[7], defaultlevellines[7])  # water level
        proj["PR"] = lingoIO.tojson(lines[8], defaultlevellines[8])  # props and settings why the hell i typed both settings wrong???
        if len(lines) > 9:
            proj["CLD"] = lingoIO.tojson(lines[9])
        return PathDict(proj)

    def openfile(self, file: str):
        from core.Level.RWLParser import RWLParser
        if not os.path.exists(file):
            raise FileNotFoundError("No file found!!!")
        _, ext = os.path.splitext(file)
        if ext == ".rwl":
            level, light = RWLParser.parse_rwl(file)
            self.lightdata = light
            self.data = PathDict(level)
            return
        with open(file) as f:
            if ext == ".txt":
                self.data = RWELevel.turntoproject(f.read())
                self.get_light(file)
                return
            elif ext == ".wep":
                self.data = PathDict(json.load(f))
                self.get_light(file)
                return
            raise FileNotCompatible(f"{file} is not compatible with {info.NAME}!")

    def get_light(self, file):
        lightpath, _ = os.path.splitext(file)
        lightpath += ".png"
        if os.path.exists(lightpath):
            with open(lightpath, "rb") as f:
                self.lightdata = f.read()

    def save_light(self, file):
        if self.lightdata is None:
            return
        lightpath, _ = os.path.splitext(file)
        with open(lightpath + ".png", "wb") as l:
            l.write(self.lightdata)

    def save_file(self) -> bool:
        from core.Level.RWLParser import RWLParser
        for i, v in self.levelparts.items():
            v.save_level()
        if self.file is None:
            return False
        self.was_resized = False
        _, ex = os.path.splitext(self.file)
        if ex == ".txt":
            self.turntolingo(open(self.file, "w"))
            self.save_light(self.file)
            return True
        elif ex == ".wep":
            with open(self.file, "w") as f:
                f.write(ujson.dumps(self.data.data))
            self.save_light(self.file)
            return True
        elif ex == ".rwl":
            RWLParser.save_rwl(self.data.data, self.file, self.lightdata)
            return True
        try:
            self.file += ".rwl"
            RWLParser.save_rwl(self.data.data, self.file, self.lightdata)
            return True
        except Exception:
            traceback.print_exc()
        return False
