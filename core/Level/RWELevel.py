import os.path
from path_dict import PathDict
from core import lingoIO
import json
import ujson  # just for json to be more compact and fast
from core import info
from core.Exceptions import *
from core.HistorySystem import History
from core.Level.RWLParser import RWLParser
from core.Level.LevelPart import LevelPart
from core.Level.CustomLevelData import CustomLevelData
from PySide6.QtCore import QPoint, Slot, QRect, QSize
from core.HistorySystem import HistoryElement

defaultlevel = open(os.path.join(info.PATH_FILES, "default.txt"), "r").read()
defaultlevellines = defaultlevel.split("\n")


class RWELevel:
    def __init__(self, manager, file=None):
        self.manager = manager
        self.file = file
        if file is not None:
            self.openfile(file)
        else:
            self.data = RWELevel.turntoproject(defaultlevel)
        self.history = History(self)
        self.viewport = None
        self.levelparts: dict[str, LevelPart] = {}
        self.mount_levelparts()

        # quick access stuff
        self.l_geo = self.levelparts["geo"]
        self.l_tiles = self.levelparts["tiles"]
        self.l_effects = self.levelparts["effects"]
        self.l_props = self.levelparts["props"]

        self.custom_level_data = CustomLevelData(self)

        self.was_resized = False

    def mount_levelparts(self):
        for i in self.manager.mods:
            i.mount_levelparts(self)

    @Slot()
    def undo(self):
        self.history.undo()

    @Slot()
    def redo(self):
        self.history.redo()

    def add_history(self, historyelement: HistoryElement):
        self.history.add_element(historyelement)

    @property
    def last_history_element(self):
        return self.history.last_element

    @property
    def shortname(self):
        if self.file is None:
            return None
        return os.path.split(self.file)[1]

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    @property
    def level_rect(self) -> QRect:
        return QRect(0, 0, self.level_width, self.level_height)

    @property
    def extra_tiles(self) -> [int, int, int, int]:
        return self.data["EX2"]["extraTiles"]

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
            proj["CLD"] = lingoIO.tojson(lines[9])  # props and settings why the hell i typed both settings wrong???
        return PathDict(proj)

    def openfile(self, file: str):
        if not os.path.exists(file):
            raise FileNotFoundError("No file found!!!")
        _, ext = os.path.splitext(file)
        if ext == ".rwl":
            with open(file, "rb") as f:
                self.data = PathDict(RWLParser.parse_rwl(bytearray(f.read())))
                return
        with open(file) as f:
            if ext == ".txt":
                self.data = RWELevel.turntoproject(f.read())
                return
            elif ext == ".wep":
                self.data = PathDict(json.load(f))
                return
            raise FileNotCompatible(f"{file} is not compatible with {info.NAME}!")

    def save_file(self) -> bool:
        for i, v in self.levelparts.items():
            v.save_level()
        if self.file is None:
            return False
        self.was_resized = False
        _, ex = os.path.splitext(self.file)
        if ex == ".txt":
            self.turntolingo(open(self.file, "w"))
            return True
        elif ex == ".wep":
            with open(self.file, "w") as f:
                f.write(ujson.dumps(self.data.data))
            return True
        elif ex == ".rwl":
            with open(self.file, "wb") as f:
                f.write(RWLParser.save_rwl(self.data.data))
            return True
        return False
