from RWESharp.Modify import LevelPart
from RWESharp.Core import lingoIO, SPRITESIZE, CELLSIZE
from RWESharp.Utils import polar2point, point2polar
from PySide6.QtCore import QPoint, QPointF
import numpy as np
from copy import deepcopy


stack_pos = [1, 2, 11, 3, 4, 5, 6, 7, 9, 10, 12, 13, 19, 21, 20, 18]


class GeoLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("geo", level)
        level_size = (len(level.data["GE"]), len(level.data["GE"][0]))
        self.blocks = np.zeros((*level_size, 3), np.uint8)
        self.stack = np.zeros((*level_size, 3), np.uint16)

        # loading level
        self.load_level()

    def load_level(self):
        dat = self.level.data["GE"]
        with np.nditer(self.blocks, flags=['multi_index'], op_flags=['writeonly']) as it:
            for x in it:
                x[...] = dat[it.multi_index[0]][it.multi_index[1]][it.multi_index[2]][0]
        with np.nditer(self.stack, flags=['multi_index'], op_flags=['writeonly']) as it:
            for x in it:
                x[...] = self.stack2byte(dat[it.multi_index[0]][it.multi_index[1]][it.multi_index[2]][1])

        #print("new")
        #print(np.asarray(dat, np.int8))

    def save_level(self):
        if self.level.was_resized:
            self.level.data["GE"] = [[[[0, []], [0, []], [0, []]] for _ in range(self.width)] for _ in range(self.height)]
        with np.nditer(self.blocks, flags=['multi_index'], op_flags=['readonly']) as it:
            for x in it:
                self.level.data["GE"][it.multi_index[0]][it.multi_index[1]][it.multi_index[2]][0] = int(x[...])
        with np.nditer(self.stack, flags=['multi_index'], op_flags=['readonly']) as it:
            for x in it:
                self.level.data["GE"][it.multi_index[0]][it.multi_index[1]][it.multi_index[2]][1] = self.byte2stack(x[...])

    @staticmethod
    def stack2byte(stack) -> np.int16:
        b = np.uint16()
        for i in stack:
            b |= 1 << stack_pos.index(i)
        return b

    @staticmethod
    def byte2stack(b) -> list:
        stack = []
        for i in range(16):
            if b & 1 << i > 0:
                stack.append(stack_pos[i])
        return stack

    def getlevelgeo_all(self, x, y) -> [np.uint8, np.uint16]:
        return [[self.blocks[x, y, 0], self.stack[x, y, 0]], [self.blocks[x, y, 1], self.stack[x, y, 1]], [self.blocks[x, y, 2], self.stack[x, y, 2]]]

    def getlevelgeo(self, x, y, l) -> [np.uint8, np.uint16]:
        return [self.blocks[x, y, l], self.stack[x, y, l]]

    def setlevelgeo(self, x, y, l, v: [np.uint8, np.uint16]):
        self.blocks[x, y, l], self.stack[x, y, l] = v

    @property
    def width(self):
        return self.blocks.shape[0]

    @property
    def height(self):
        return self.blocks.shape[1]


class TileLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("tiles", level)
        self.tiles = self.level.data["TE"]["tlMatrix"]

    def save_level(self):
        self.level.data["TE"]["tlMatrix"] = self.tiles

    def tile_data_xy(self, x: int, y: int, layer: int) -> dict[str, ...]:
        """
        returns tile on specific layer
        :param x: x position of tile
        :param y: y position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.tiles[x][y][layer]

    def tile_data(self, pos: QPoint, layer: int) -> dict[str, ...]:
        """
        returns tile on specific layer
        :param pos: position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.tiles[pos.x()][pos.y()][layer]

    def __call__(self, *args, **kwargs):
        return self.tile_data(*args, **kwargs)


class PropLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("props", level)
        self.props = []
        for i in self.level["PR"]["props"]:
            newp = self.copyprop(i)
            newp[3] = [QPointF(*lingoIO.fromarr(p, "point")) * (CELLSIZE / SPRITESIZE) for p in newp[3]]
            self.props.append(newp)

    def save_level(self):
        self.level["PR"]["props"] = []
        for i in self.props:
            newp = self.copyprop(i)
            newp[3] = [lingoIO.point((p * (SPRITESIZE / CELLSIZE)).toTuple()) for p in newp[3]]
            self.level["PR"]["props"].append(newp)

    def __len__(self):
        return len(self.props)

    def __iter__(self):
        return self.props.__iter__()

    def __getitem__(self, item):
        return self.props[item]

    def __setitem__(self, key, value):
        self.props[key] = value

    def pop(self, index):
        return self.props.pop(index)

    def insert(self, index, prop):
        self.props.insert(index, prop)

    def copyprop(self, prop):
        return [prop[0], prop[1], prop[2], prop[3].copy(), prop[4].copy()]

    def index(self, item):
        return self.props.index(item)


class EffectLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("effects", level)
        self.effects = []
        self.load_level()

    def load_level(self):
        dat = self.level.data["FE"]["effects"]
        for i in dat:
            self.effects.append(deepcopy({k: v for k, v in i.items() if k != "mtrx"}))
            self.effects[-1]["mtrx"] = np.zeros(self.level.level_size.toTuple(), np.float16)
            with np.nditer(self.effects[-1]["mtrx"], flags=['multi_index'], op_flags=['writeonly']) as it:
                for x in it:
                    x[...] = i["mtrx"][it.multi_index[0]][it.multi_index[1]]

    def save_level(self):
        self.level.data["FE"]["effects"] = []
        for i in self.effects:
            newi = deepcopy({k: v for k, v in i.items() if k != "mtrx"})
            newi["mtrx"] = [[float(i["mtrx"][x, y]) for y in range(self.level.level_height)] for x in range(self.level.level_width)]
            self.level.data["FE"]["effects"].append(newi)

    def effect_data_xy(self, index: int, x: int, y:int) -> float:
        """
        returns specific value of effect
        :param index: effect index
        :param x: x pos of value
        :param y: y pos of value
        """
        return self.effects[index]["mtrx"][x, y]

    def __len__(self):
        return len(self.effects)

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.effects[item]
        return self.effects[item[0]]["mtrx"][item[1], item[2]]

    def __setitem__(self, key, value):
        self.effects[key[0]]["mtrx"][key[1], key[2]] = value

    def __iter__(self):
        return self.effects.__iter__()

    def append(self, item):
        self.effects.append(item)

    def insert(self, index, item):
        self.effects.insert(index, item)

    def pop(self, index=-1):
        return self.effects.pop(index)

    def index(self, item):
        return self.effects.index(item)


class CameraLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("camera", level)
        self.cameras: list[CameraLevelPart.Camera] = []
        for i, v in enumerate(level.data["CM"]["cameras"]):
            quad = [QPointF(*k) for k in level.data["CM"]["quads"][i]]
            quad = [polar2point(QPointF(i.x() - 90, i.y())) for i in quad]
            self.cameras.append(CameraLevelPart.Camera(QPointF(*lingoIO.frompoint(v)), quad))

    def save_level(self):
        self.level.data["CM"]["cameras"] = []
        self.level.data["CM"]["quads"] = []

        for i in self.cameras:
            newquads = [point2polar(q) for q in i.quads]
            quad = [[(round(k.x(), 4) + 90) % 360, round(k.y(), 4)] for k in newquads]
            self.level.data["CM"]["quads"].append(quad)
            self.level.data["CM"]["cameras"].append(lingoIO.point(i.pos.toTuple()))

    class Camera:
        def __init__(self, pos: QPointF, quads: list[QPointF]):
            self.pos = QPointF(round(pos.x(), 4), round(pos.y(), 4))
            self.quads = quads

    def __iter__(self):
        return self.cameras.__iter__()

    def __len__(self):
        return self.cameras.__len__()

    def pop(self, index):
        return self.cameras.pop(index)

    def insert(self, index, prop):
        self.cameras.insert(index, prop)

    def index(self, item):
        return self.cameras.index(item)

    def __getitem__(self, item):
        return self.cameras.__getitem__(item)
