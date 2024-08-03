import os.path
from path_dict import PathDict
from core import lingoIO
import json
import ujson  # just for json to be more compact and fast
from core import info
from core.Exceptions import *
from core.HistorySystem import History
from core.RWLParser import RWLParser
from PySide6.QtCore import QPoint, Slot, QRect
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

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def geo_data_xy(self, x: int, y: int, layer: int) -> [int, list[int]]:
        """
        returns cell on specific layer
        :param x: x position of cell
        :param y: y position of cell
        :param layer: layer of cell
        :return:
        """
        return self.data["GE"][x][y][layer]

    def geo_data(self, pos: QPoint, layer: int) -> [int, list[int]]:
        """
        returns cell on specific layer
        :param pos: position of cell
        :param layer: layer of cell
        :return:
        """
        return self.data["GE"][pos.x()][pos.y()][layer]

    def tile_data_xy(self, x: int, y: int, layer: int) -> dict[str, ...]:
        """
        returns tile on specific layer
        :param x: x position of tile
        :param y: y position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.data["TE"]["tlMatrix"][x][y][layer]

    def tile_data(self, pos: QPoint, layer: int) -> dict[str, ...]:
        """
        returns tile on specific layer
        :param pos: position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer]

    def effect_data(self, index: int) -> list[list[float]]:
        """
        returns matrix for specific effect
        :param index: effect index
        """
        return self.data["FE"]["effects"][index]

    def effect_data_pixel(self, index: int, pos: QPoint) -> float:
        """
        returns specific value of effect
        :param index: effect index
        :param pos: value position
        """
        return self.data["FE"]["effects"][index]["mtrx"][pos.x()][pos.y()]

    def effect_data_xy(self, index: int, x: int, y:int) -> float:
        """
        returns specific value of effect
        :param index: effect index
        :param x: x pos of value
        :param y: y pos of value
        """
        return self.data["FE"]["effects"][index]["mtrx"][x][y]

    @property
    def effects(self):
        return self.data["FE"]["effects"]

    @property
    def effect_len(self) -> int:
        return len(self.data["FE"]["effects"])

    @property
    def extra_tiles(self) -> [int, int, int, int]:
        return self.data["EX2"]["extraTiles"]

    def inside(self, point: QPoint) -> bool:
        return 0 <= point.x() < self.level_width and 0 <= point.y() < self.level_height

    def inside_border(self, point: QPoint) -> bool:
        borders = self.extra_tiles
        topleft = QPoint(borders[0], borders[1])
        bottomright = self.manager.level.level_size - QPoint(borders[2], borders[3])
        rect = QRect(topleft, bottomright)
        return rect.contains(point)

    @property
    def level_width(self) -> int:
        return len(self.data["GE"])

    @property
    def level_height(self) -> int:
        return len(self.data["GE"][0])

    @property
    def level_size(self) -> QPoint:
        return QPoint(self.level_width, self.level_height)

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
        if self.file is None:
            return False
        _, ex = os.path.splitext(self.file)
        if ex == ".txt":
            self.turntolingo(open(self.file, "w"))
        elif ex == ".wep":
            with open(self.file, "w") as f:
                f.write(ujson.dumps(self.data.data))
        elif ex == ".rwl":
            with open(self.file, "wb") as f:
                f.write(RWLParser.save_rwl(self.data.data))
