import os.path
from path_dict import PathDict
from core import lingoIO
import json
from core import info
from core.Exceptions import *
from core.HistorySystem import History
from core.RWLParser import RWLParser
from PySide6.QtCore import QPoint, Slot
from core.HistorySystem import HistoryElement

defaultlevel = open(os.path.join(info.PATH_FILES, "default.txt"), "r").read()
defaultlevellines = defaultlevel.split("\n")


class RWELevel:
    def __init__(self, manager, data=None):
        self.manager = manager
        if data is None:
            self.data = PathDict({})
        else:
            self.data = PathDict(data)
        self.history = History(self)

    @Slot()
    def undo(self):
        print("undo")
        self.history.undo()

    @Slot()
    def redo(self):
        print("redo")
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

    def GE_data(self, x: int, y: int, layer: int) -> list[int, list[int]]:
        """
        returns cell on specific layer
        :param x: x position of cell
        :param y: y position of cell
        :param layer: layer of cell
        :return:
        """
        return self.data["GE"][int(x)][int(y)][layer]

    def TE_data(self, x: int, y: int, layer: int) -> dict[str, ...]:
        """
        returns tile on specific layer
        :param x: x position of tile
        :param y: y position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.data["TE"]["tlMatrix"][int(x)][int(y)][layer]

    @property
    def extra_tiles(self) -> [int, int, int, int]:
        return self.data["EX2"]["extraTiles"]

    def inside(self, x: int, y: int) -> bool:
        return self.inside(QPoint(x, y))

    def inside(self, point: QPoint) -> bool:
        return 0 <= point.x() < self.level_width and 0 <= point.y() < self.level_height

    @property
    def level_width(self) -> int:
        return len(self.data["GE"])

    @property
    def level_height(self) -> int:
        return len(self.data["GE"][0])

    @property
    def level_size(self) -> QPoint:
        return QPoint(self.level_width, self.level_height)

    @staticmethod
    def turntolingo(string: dict, file):
        with file as fl:
            fl.write(str(string["GE"]) + "\r")
            fl.write(lingoIO.tolingo(string["TE"]) + "\r")
            fl.write(lingoIO.tolingo(string["FE"]) + "\r")
            fl.write(lingoIO.tolingo(string["LE"]) + "\r")
            fl.write(lingoIO.tolingo(string["EX"]) + "\r")
            fl.write(lingoIO.tolingo(string["EX2"]) + "\r")
            fl.write(lingoIO.tolingo(string["CM"]) + "\r")
            fl.write(lingoIO.tolingo(string["WL"]) + "\r")
            fl.write(lingoIO.tolingo(string["PR"]) + "\r")

    @staticmethod
    def turntoproject(manager, string: str):
        proj = RWELevel(manager)
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
        return proj

    @staticmethod
    def openfile(manager, file: str):
        if not os.path.exists(file):
            raise FileNotFoundError("No file found!!!")
        _, ext = os.path.splitext(file)
        if ext == ".rwl":
            with open(file, "rb") as f:
                return RWELevel(manager, RWLParser.parse_rwl(bytearray(f.read())))
        with open(file, "r") as f:
            if ext == ".txt":
                return RWELevel.turntoproject(manager, f.read())
            elif ext == ".wep":
                return RWELevel(manager, json.load(f))
            raise FileNotCompatible(f"{file} is not compatible with {info.NAME}!")