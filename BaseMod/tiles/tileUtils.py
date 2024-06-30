from __future__ import annotations

from PySide6.QtCore import QPoint

from RWESharp.Core import lingoIO, RWELevel
from RWESharp.Loaders import Tile, tile_offset
from RWESharp.Modify import HistoryElement


def point_collision(level: RWELevel, pos: QPoint, layer: int, tilepos: QPoint, tile: Tile) -> bool:
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


def check_collisions(level: RWELevel, pos: QPoint, layer: int, tile: Tile) -> bool:
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            levelpos = QPoint(x, y)
            tilepos = levelpos - pos
            if not level.inside(levelpos):
                continue
            result = point_collision(level, levelpos, layer, tilepos, tile)
            if not result:
                return False
    return True


def can_place(level: RWELevel,
              pos: QPoint,
              layer: int,
              tile: Tile,
              area: list[list[bool]],
              area2: list[list[bool]],
              force_place: bool,
              force_geometry: bool) -> bool:
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return False
    # if area is available
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            if not level.inside(QPoint(x, y)):
                continue
            if not area[x][y]:
                return False
            if isinstance(tile.cols[1], list) and not area2[x][y]:
                return False
    # mf got through our defence
    if force_place:
        return False
    return check_collisions(level, pos, layer, tile) or force_geometry


def place_tile(level: RWELevel,
               pos: QPoint,
               layer: int,
               tile: Tile,
               area: list[list[bool]] = None,
               area2: list[list[bool]] = None,
               force_place: bool = False,
               force_geometry: bool = False) -> PlacedTile | None:
    if tile.type == "material":
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "material", "data": tile.name}
        level.manager.basemod.tilemodule.get_layer(layer).draw_tile(pos)
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return PlacedTile(pos, layer, tile)
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return None
    for x in range(tile.size.width()):
        for y in range(tile.size.height()):
            tilepos = QPoint(x, y) + pos
            if not level.inside(tilepos):
                continue
            if area is not None:
                area[tilepos.x()][tilepos.y()] = False
            # area2[x][y] = False
            try:
                col = tile.cols[0][x * tile.size.height() + y]
            except IndexError:
                col = 1
            if isinstance(tile.cols[1], list) and layer + 1 < 3:
                if area2 is not None:
                    area2[tilepos.x()][tilepos.y()] = False
                try:
                    col = tile.cols[1][x * tile.size.height() + y]
                except IndexError:
                    col = 1
                if col != -1:
                    level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer + 1] = \
                        {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x(), headpos.y()], "point"), layer]}
            if col == -1:
                continue
            if tilepos == headpos:
                level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer] = {"tp": "tileHead", "data": [
                    lingoIO.makearr([tile.cat.x(), tile.cat.y()], "point"), tile.name]}
                continue
            level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer] = \
                {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x(), headpos.y()], "point"), layer]}
    level.manager.basemod.tilemodule.get_layer(layer).draw_tile(headpos)
    return PlacedTile(pos, layer, tile)


def remove_tile(level: RWELevel, pos: QPoint, layer: int):
    if not level.inside(pos):
        return
    data = level.tile_data(pos, layer)
    tp = data.get("tp", "default")
    head = [lingoIO.makearr([pos.x(), pos.y()], "point"), layer]
    if tp == "default":
        return
    elif tp == "material":
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "default", "data": 0}
        level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(pos)
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return
    elif tp == "tileBody":
        head = data.get("data")
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "default", "data": 0}
        if head is None:
            return
    headpos = QPoint(*lingoIO.fromarr(head[0], "point"))
    headdata = level.tile_data(headpos, head[1])
    if headdata.get("tp") != "tileHead":
        return
    foundtile = level.manager.tiles[headdata.get("data")[1]]
    if foundtile is None:
        return
    offset = tile_offset(foundtile)
    for x in range(foundtile.size.width()):
        for y in range(foundtile.size.height()):
            bodypos = QPoint(x, y) + headpos - offset
            if not level.inside(bodypos):
                continue
            try:
                col = foundtile.cols[0][x * foundtile.size.height() + y]
            except IndexError:
                col = 1
            if isinstance(foundtile.cols[1], list) and layer + 1 < 3:
                try:
                    col2 = foundtile.cols[1][x * foundtile.size.height() + y]
                except IndexError:
                    col2 = 1
                if col2 != -1:
                    level.manager.basemod.tilemodule.get_layer(layer + 1).clean_pixel(bodypos)
                    level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer + 1] = {"tp": "default", "data": 0}
            if col == -1:
                continue
            level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(bodypos)
            level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer] = {"tp": "default", "data": 0}


class PlacedTile:
    def __init__(self, pos: QPoint, layer: int, tile: Tile):
        self.pos = pos
        self.layer = layer
        self.tile = tile

    def undo(self, element: TileHistory):
        remove_tile(element.history.level, self.pos, self.layer)

    def redo(self, element: TileHistory):
        place_tile(element.history.level, self.pos, self.layer, self.tile)


class TileHistory(HistoryElement):
    def __init__(self, history, tile: Tile, layer: int):
        super().__init__(history)
        self.area = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.area2 = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.layer = layer
        self.tile = tile
        self.savedtiles: list[PlacedTile] = []

    def undo_changes(self, level):
        for i in self.savedtiles:
            i.undo(self)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()

    def redo_changes(self, level):
        for i in self.savedtiles:
            i.redo(self)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()
