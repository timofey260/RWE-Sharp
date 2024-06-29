from __future__ import annotations
from RWESharp.Modify import HistoryElement
from RWESharp.Loaders import Tile, tile_offset
from RWESharp.Utils import draw_line
from RWESharp.Core import RWELevel, lingoIO
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import QPoint


def point_collision(level: RWELevel, pos: QPoint, layer, tilepos: QPoint, tile: Tile) -> bool:
    tiledata = level.tile_data(pos, layer)
    tp = tiledata.get("tp", "default")
    # data = tiledata.get("data", 0)
    if tp != "default":
        return False
    geodata = level.geo_data(pos, layer)[0]
    try:
        collision = tile.cols[0][tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if geodata != collision and geodata != -1:
        return False
    # next layer
    if not isinstance(tile.cols[1], list) or layer + 1 > 2:
        return True
    geodata = level.geo_data(pos, layer + 1)[0]
    try:
        collision = tile.cols[1][tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if geodata != collision and geodata != -1:
        return False
    return True


def check_collisions(level: RWELevel, layer: int, pos: QPoint, tile: Tile) -> bool:
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            levelpos = QPoint(x, y)
            tilepos = levelpos - pos
            result = point_collision(level, levelpos, layer, tilepos, tile)
            if not result:
                return False
    return True


def can_place(level: RWELevel,
              layer: int,
              tile: Tile,
              pos: QPoint,
              area: list[list[bool]],
              area2: list[list[bool]],
              force_place: bool,
              force_geometry: bool) -> bool:
    # if area is available
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            if not area[x][y]:
                return False
            if isinstance(tile.cols[1], list) and not area2[x][y]:
                return False
    # mf got through our defence
    if force_place or force_geometry:
        return False
    return check_collisions(level, layer, pos, tile)


def place_tile(level: RWELevel,
               layer: int,
               tile: Tile,
               pos: QPoint,
               area: list[list[bool]],
               area2: list[list[bool]],
               force_place: bool,
               force_geometry: bool):
    if tile.type == "material":
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "material", "data": tile.name}
        level.manager.basemod.tilemodule.get_layer(layer).draw_tile(pos.x(), pos.y())
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return
    headpos = tile_offset(tile)
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            area[x][y] = False
            # area2[x][y] = False
            if QPoint(x, y) - pos == headpos:
                level.data["TE"]["tlMatrix"][x][y][layer] = {"tp": "tileHead", "data": [
                    lingoIO.makearr([tile.cat.x(), tile.cat.y()], "point"), tile.name]}
                continue
            level.data["TE"]["tlMatrix"][x][y][layer] = {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x(), headpos.y()], "point"), layer]}
    level.manager.basemod.tilemodule.get_layer(layer).draw_tile(pos.x(), pos.y())
    level.manager.basemod.tilemodule.get_layer(layer).redraw()


def remove_tile(level: RWELevel, pos: QPoint, layer: int):
    data = level.tile_data(pos, layer)


class PlacedTile:
    def __init__(self, element: TileHistory, pos: QPoint):
        self.element = element
        self.pos = pos
        place_tile(element.history.level, element.layer, element.tile, pos, element.area, element.area2, False, False)

    def undo(self):
        pass

    def redo(self):
        pass


class TileHistory(HistoryElement):
    def __init__(self, history, tile: Tile, layer: int):
        super().__init__(history)
        self.area = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.area2 = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.layer = layer
        self.tile = tile


class TilePen(TileHistory):
    def __init__(self, history, start: QPoint, tile: Tile, layer: int):
        super().__init__(history, tile, layer)
        self.positions = []
        self.start = start
        self.savedtiles: list[PlacedTile] = []

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            canplace = can_place(self.history.level, self.layer, self.tile, point, self.area, self.area2, False, False)
            if canplace:
                place_tile(self.history.level, self.layer, self.tile, point, self.area, self.area2, False, False)