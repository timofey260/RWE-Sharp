import os.path
from path_dict import PathDict
from core import lingoIO
import json
from core import info
from core.Exceptions import *
from core.HistorySystem import History
from core.RWLParser import RWLParser
from PySide6.QtCore import QPoint

defaultlevel = open(os.path.join(info.PATH_FILES, "default.txt"), "r").readlines()


class RWELevel:
    def __init__(self, data=None):
        #self.manager = manager
        if data is None:
            self.data = PathDict({})
        else:
            self.data = PathDict(data)
        self.history = History(self)

    def undo(self):
        self.history.undo()

    def redo(self):
        self.history.redo()

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def GE_data(self, x, y, layer):
        return self.data["GE"][int(x)][int(y)][layer]

    def TE_data(self, x, y, layer):
        return self.data["TE"]["tlMatrix"][int(x)][int(y)][layer]

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
    def turntoproject(string: str):
        proj = RWELevel()
        lines = string.split("\n")
        proj["GE"] = json.loads(lines[0])  # geometry
        proj["TE"] = lingoIO.tojson(lines[1])  # tile editor and his settings
        proj["FE"] = lingoIO.tojson(lines[2])  # effect editor params
        proj["LE"] = lingoIO.tojson(lines[3], defaultlevel[3])  # light editor and presets
        proj["EX"] = lingoIO.tojson(lines[4], defaultlevel[4])  # map settings
        proj["EX2"] = lingoIO.tojson(lines[5], defaultlevel[5])  # light and level settings
        proj["CM"] = lingoIO.tojson(lines[6], defaultlevel[6])  # camera settings
        proj["WL"] = lingoIO.tojson(lines[7], defaultlevel[7])  # water level
        proj["PR"] = lingoIO.tojson(lines[8], defaultlevel[8])  # props and settings why the hell i typed both settings wrong???
        return proj

    @staticmethod
    def openfile(file: str):
        if not os.path.exists(file):
            raise FileNotFoundError("No file found!!!")
        _, ext = os.path.splitext(file)
        if ext == ".rwl":
            with open(file, "rb") as f:
                return RWELevel(RWLParser.parse_rwl(bytearray(f.read())))
        with open(file, "r") as f:
            if ext == ".txt":
                return RWELevel.turntoproject(f.read())
            elif ext == ".wep":
                return RWELevel(json.load(f))
            raise FileNotCompatible(f"{file} is not compatible with {info.NAME}!")