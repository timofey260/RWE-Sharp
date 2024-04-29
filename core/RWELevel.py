from path_dict import PathDict
import lingoIO
import json
import info
from Exceptions import *

defaultlevel = open(info.PATH_FILES + "default.txt", "r").readlines()

class RWELevel:
    def __init__(self, data=None):
        if data is None:
            self.data = PathDict({})
        else:
            self.data = PathDict(data)
        self.undohistory = []
        self.redohistory = []

    def undo(self):
        pass

    def redo(self):
        pass

    def change(self, path, value, override_match=False):
        # 1 history element is tree of history elements
        # history element can either contain value before and after change or children, creating tree
        if self.data[path] == value or override_match:
            pass
        self.data[path] = value
        pass

    @staticmethod
    def load_from_file(file: str):
        if file[-3:] == "txt":
            print("trying to load LE level")
            return lingoIO.turntoproject(open(file, "r").read())
        elif file[-3:] == "wep":
            print("trying to load RWE+ level")
            return RWELevel(json.load(open(file, "r")))
        elif file[-3:] == "rwee":
            print("trying to load RWEE level")
            return RWELevel()

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    def GE_data(self, x, y, layer):
        return self.data["GE"][int(x)][int(y)][layer]

    def TE_data(self, x, y, layer):
        return self.data["TE"]["tlMatrix"][int(x)][int(y)][layer]

    @property
    def levelwidth(self):
        return len(self.data["GE"])

    @property
    def levelheight(self):
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
        print("Loading level...")
        proj["GE"] = eval(lines[0])  # geometry
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
        with open(file, "r") as f:
            if file.endswith(".txt"):
                pass
            elif file.endswith(".wep"):
                return
            elif file.endswith(".slug"):
                raise NotImplementedError("Does not support slug files yet")
            raise FileNotCompatible(f"{file} is not compatible with {info.NAME}!")