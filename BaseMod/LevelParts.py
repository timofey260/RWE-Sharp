from copy import deepcopy

import numpy as np
from PySide6.QtCore import QPoint, QPointF, QSize, QByteArray, QBuffer, QIODevice, QRect
from PySide6.QtGui import QImage, QPainter, QColor, QImageWriter

from BaseMod.tiles.tileUtils import PlacedMaterial, PlacedTileHead, PlacedTileBody
from RWS.Core import lingoIO
from RWS.Core import SPRITESIZE, CELLSIZE, ofsleft, ofstop
from RWS.Modify import LevelPart
from RWS.Utils import polar2point, point2polar

stack_pos = [1, 2, 11, 3, 4, 5, 6, 7, 9, 10, 12, 13, 19, 21, 20, 18]


class InfoLevelPart(LevelPart):
    def level_resized(self, changerect: QRect):
        from BaseMod.properties.PropertiesHistory import LevelResizedProperties
        return LevelResizedProperties(self.level.history, changerect)

    def save_level(self):
        self.level.data["EX2"]["extraTiles"] = self.extra_tiles.copy()
        self.level.data["EX2"]["tileSeed"] = self.tile_seed
        self.level.data["EX2"]["size"] = lingoIO.point(self.size)
        self.level.data["WL"]["waterLevel"] = self.water_level
        self.level.data["WL"]["waterInFront"] = 1 if self.water_in_front else 0

    def __init__(self, level):
        super().__init__("info", level)
        self.size: list[int] = lingoIO.fromarr(level.data["EX2"]["size"], "point")
        self.extra_tiles: list[int] = level.data["EX2"]["extraTiles"].copy()
        self.tile_seed: int = level.data["EX2"]["tileSeed"]
        self.water_level: int = level.data["WL"]["waterLevel"]
        self.water_in_front = level.data["WL"]["waterInFront"] == 1

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]


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

    def level_resized(self, changerect: QRect):
        from BaseMod.geo.geoHistory import LevelResizedGeo
        return LevelResizedGeo(self.level.history, changerect)

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

    def getlevelgeo_all(self, x: int, y: int) -> [np.uint8, np.uint16]:
        return [[self.blocks[x, y, 0], self.stack[x, y, 0]], [self.blocks[x, y, 1], self.stack[x, y, 1]], [self.blocks[x, y, 2], self.stack[x, y, 2]]]

    def getlevelgeo(self, x: int, y: int, l: int) -> [np.uint8, np.uint16]:
        return [self.blocks[x, y, l], self.stack[x, y, l]]

    def setlevelgeo(self, x: int, y: int, l: int, v: [np.uint8, np.uint16]):
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
        # self.tiles = self.level.data["TE"]["tlMatrix"]
        self.default_material = level["TE"]["defaultMaterial"]
        self.tiles: list[list[list[PlacedTileHead | PlacedTileBody | PlacedMaterial | None]]] | None = None
        self.load_tiles()

    def load_tiles(self):
        # tilebodies: dict[(QPoint, int), list[PlacedTileBody]] = {}
        self.tiles = [[[self.scantile(QPoint(x, y), 0),
                        self.scantile(QPoint(x, y), 1),
                        self.scantile(QPoint(x, y), 2)]
                       for y in range(self.level.level_height)] for x in range(self.level.level_width)]
        # for k, v in tilebodies.items():
        #     pos = k[0]
        #     layer = k[1]
        #     tilehead = self.tiles[pos.x()][pos.y()][layer]
        #     if not isinstance(tilehead, PlacedTileHead):
        #         continue
        #     tilehead.tilebodies = v
        #     for i in v:
        #         i.tilehead = tilehead

    def scantile(self, pos: QPoint, layer: int):
        tile = self.level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer]
        match tile["tp"]:
            case "material":
                foundtile = self.level.manager.tiles.find_tile(tile["data"])
                if foundtile is None:
                    return None  # todo notfound material and tile exceptions
                return PlacedMaterial(foundtile, pos, layer)
            case "tileHead":
                foundtile = self.level.manager.tiles.find_tile(tile["data"][1])
                if foundtile is None:
                    return None
                return PlacedTileHead(foundtile, pos, layer)
            case "tileBody":
                head = tile.get("data")
                headlayer = head[1] - 1
                tileheadpos = QPoint(*lingoIO.frompoint(head[0])) - QPoint(1, 1)
                if self.level.data["TE"]["tlMatrix"][tileheadpos.x()][tileheadpos.y()][headlayer].get("tp") == "default":
                    return None  # removing all improper tile bodies
                # l = tb.get((tileheadpos, layer), None)
                tileheadoffset = pos - tileheadpos
                tilebody = PlacedTileBody(tileheadoffset, headlayer, pos, layer)
                # if l is None:
                #     tb[(tileheadpos, layer)] = [tilebody]
                #     return tilebody
                # l.append(tilebody)
                return tilebody

    def save_level(self):
        self.level.data["TE"]["tlMatrix"] = [[[self.convert_to_dict(x, y, 0), self.convert_to_dict(x, y, 1), self.convert_to_dict(x, y, 2)]
                       for y in range(self.level.level_height)] for x in range(self.level.level_width)]
        self.level.data["TE"]["defaultMaterial"] = self.default_material

    def convert_to_dict(self, x, y, l):
        tile = self.tiles[x][y][l]
        if tile is None:
            return {"tp": "default", "data": 0}
        if isinstance(tile, PlacedMaterial):
            return {"tp": "material", "data": tile.tile.name}
        if isinstance(tile, PlacedTileBody):
            return {"tp": "tileBody", "data": [lingoIO.point((tile.headpos + QPoint(1, 1)).toTuple()), tile.headlayer + 1]}
        if isinstance(tile, PlacedTileHead):
            return {"tp": "tileHead", "data": [lingoIO.point((tile.tile.cat + QPoint(1, 1)).toTuple()), tile.tile.name]}
        raise NotImplementedError("someone probably fucked up")

    def level_resized(self, changerect: QRect):
        from BaseMod.tiles.tileHistory import LevelResizedTiles
        return LevelResizedTiles(self.level.history, changerect)

    def tile_data_xy(self, x: int, y: int, layer: int) -> None | PlacedTileBody | PlacedTileHead | PlacedMaterial:
        """
        returns tile on specific layer
        :param x: x position of tile
        :param y: y position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.tiles[x][y][layer]

    def tile_data(self, pos: QPoint, layer: int) -> None | PlacedTileBody | PlacedTileHead | PlacedMaterial:
        """
        returns tile on specific layer
        :param pos: position of tile
        :param layer: layer of tile(0-2)
        :return:
        """
        return self.tiles[pos.x()][pos.y()][layer]

    def __call__(self, *args, **kwargs):
        return self.tile_data(*args, **kwargs)

    def __getitem__(self, item: QPoint):
        return self.tiles[item.x()][item.y()]


class PropLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("props", level)
        self.props: list[PropLevelPart.PlacedProp] = []
        for i in self.level["PR"]["props"]:
            newp = self.copyprop(i)
            # find prop
            found = self.manager.props.find_prop(newp[1])
            if found is None:
                found = self.manager.props.default
            prop = PropLevelPart.PlacedProp(found, newp[0],
                                            [QPointF(*lingoIO.fromarr(p, "point")) * (CELLSIZE / SPRITESIZE) for p in newp[3]],
                                            newp[4])
            # newp[3] = [QPointF(*lingoIO.fromarr(p, "point")) * (CELLSIZE / SPRITESIZE) for p in newp[3]]
            # if newp[4].get("points") is not None:
            #     newp[4]["points"] = [QPointF(*lingoIO.fromarr(p, "point")) * (CELLSIZE / SPRITESIZE) for p in newp[4]["points"]]
            self.props.append(prop)

    def level_resized(self, changerect: QRect):
        from BaseMod.props.propHistory import LevelResizedProps
        return LevelResizedProps(self.level.history, changerect)

    def save_level(self):
        self.level["PR"]["props"] = []
        for i in self.props:
            self.level["PR"]["props"].append(i.tolist)

    class PlacedProp:
        def __init__(self, prop, depth: int, quad: [QPointF, QPointF, QPointF, QPointF], settings: dict):
            self.prop = prop
            self.depth = depth
            self.quad = quad
            self.settings = settings

        @property
        def name(self):
            return self.prop.name

        @property
        def tolist(self):
            return [self.depth, self.name, lingoIO.point([i + 1 for i in self.prop.cat.toTuple()]),
                    [lingoIO.point((p * (SPRITESIZE / CELLSIZE)).toTuple()) for p in self.quad], self.settings]

        def copy(self):
            return PropLevelPart.PlacedProp(self.prop, self.depth, self.quad.copy(), self.settings.copy())

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

    def level_resized(self, changerect: QRect):
        from BaseMod.effects.effectHistory import LevelResizedEffects
        return LevelResizedEffects(self.level.history, changerect)

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
            newi["mtrx"] = [[round(float(i["mtrx"][x, y]), 4) for y in range(self.level.level_height)] for x in range(self.level.level_width)]
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

    def level_resized(self, changerect: QRect):
        from BaseMod.camera.cameraHistory import LevelResizedCameras
        return LevelResizedCameras(self.level.history, changerect)

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


class LightLevelPart(LevelPart):
    def __init__(self, level):
        super().__init__("light", level)
        self.angle = level.data["LE"]["lightAngle"]
        self.flatness = level.data["LE"]["flatness"]
        newcolortable = [QColor(0, 0, 0, 0).rgba(), QColor(0, 0, 0, 255).rgba()]
        imagesize = QSize((self.level.level_width + ofsleft) * CELLSIZE, (self.level.level_height + ofstop) * CELLSIZE)
        if level.lightdata is None:
            newimage = QImage(imagesize, QImage.Format.Format_Mono)
            newimage.setColorTable(newcolortable)
            newimage.fill(0)
            self.image = newimage
            return
        self.image = QImage.fromData(level.lightdata)
        self.image.convertTo(QImage.Format.Format_Mono)
        self.image.setColorTable(newcolortable)
        if self.image.size() != imagesize:
            newimage = QImage(imagesize, QImage.Format.Format_Mono)
            newimage.setColorTable(newcolortable)
            newimage.fill(0)
            painter = QPainter(newimage)
            painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
            painter.drawImage(QPoint(), self.image)
            self.image = newimage

    def level_resized(self, changerect: QRect):
        from BaseMod.light.lightHistory import LevelResizedLight
        return LevelResizedLight(self.level.history, changerect)

    def save_level(self):
        self.level.data["LE"]["lightAngle"] = round(self.angle, 4)
        self.level.data["LE"]["flatness"] = int(round(self.flatness))
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.OpenModeFlag.WriteOnly)
        writer = QImageWriter(buff, b"PNG")
        writer.write(self.image)
        self.level.lightdata = ba.data()