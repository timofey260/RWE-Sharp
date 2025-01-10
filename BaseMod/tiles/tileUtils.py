from __future__ import annotations

import numpy as np

from PySide6.QtCore import QPoint

from RWESharp.Core import lingoIO, RWELevel
from RWESharp.Loaders import Tile, tile_offset
from RWESharp.Modify import HistoryElement


def copy_tile(tile: dict) -> dict:
    if isinstance(tile.get("data", []), list):
        return {"tp": tile.get("tp", "default"), "data": tile.get("data", []).copy()}
    return {"tp": tile.get("tp", "default"), "data": tile.get("data", "")}


def point_collision(level: RWELevel, pos: QPoint, layer: int, tilepos: QPoint, tile: Tile, force_place: bool = False, force_geometry: bool = False) -> bool:
    tiledata = level.l_tiles(pos, layer)
    tp = tiledata.get("tp", "default")
    # data = tiledata.get("data", 0)
    if force_place and tp == "tileHead":
        return False
    elif force_place:
        return True
    elif tp != "default":
        return False
    geodata = level.l_geo.blocks[pos.x(), pos.y(), layer]
    try:
        collision = tile.cols[0][tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if collision != -1 and geodata != collision and not force_geometry:
        return False
    # next layer
    if not isinstance(tile.cols[1], list) or layer + 1 > 2:
        return True
    geodata = level.l_geo.blocks[pos.x(), pos.y(), layer + 1]
    try:
        collision = tile.cols[1][tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if collision != -1 and geodata != collision and not force_geometry:
        return False
    return True


def check_collisions(level: RWELevel, pos: QPoint, layer: int, tile: Tile, force_place: bool = False, force_geometry: bool = False) -> bool:
    for x in range(tile.size.width()):
        for y in range(tile.size.height()):
            tilepos = QPoint(x, y)
            levelpos = tilepos + pos
            if not level.inside(levelpos):
                continue
            result = point_collision(level, levelpos, layer, tilepos, tile, force_place, force_geometry)
            if not result:
                return False
    return True


def can_place(level: RWELevel, pos: QPoint, layer: int, tile: Tile, force_place: bool, force_geometry: bool,
              area: list[list[bool]] = None, area2: list[list[bool]] = None) -> bool:
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return False
    # if area is available
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            if not level.inside(QPoint(x, y)):
                continue
            if area is not None and not area[x][y]:
                return False
            if area2 is not None and isinstance(tile.cols[1], list) and not area2[x][y]:
                return False
    return check_collisions(level, pos, layer, tile, force_place, force_geometry)


def check4tile_col(level: RWELevel,
                   pos: QPoint,
                   head: QPoint,
                   tile: Tile,
                   layer: int,
                   col: int,
                   fp: bool,
                   fg: bool,
                   secondlayer: bool) -> [list | None, list | None]:
    if col == -1:
        return None, None
    geochange = None
    if fp and level.l_tiles(pos, layer).get("tp") == "tileHead":
        return None, None
    elif not fp and level.l_tiles(pos, layer).get("tp") != "default":
        return None, None
    level.viewport.modulenames["tiles"].get_layer(layer).clean_pixel(pos)
    if fg and col != level.l_geo.blocks[pos.x(), pos.y(), layer]:
        geochange = [pos, layer, col, level.l_geo.blocks[pos.x(), pos.y(), layer]]
        level.l_geo.blocks[pos.x(), pos.y(), layer] = np.uint8(col)
        # level.data["GE"][pos.x()][pos.y()][layer][0] = col
        level.viewport.modulenames["geo"].get_layer(layer).draw_geo(pos.x(), pos.y(), True)
    if not secondlayer and pos == head:
        change = [pos, layer,
                  {"tp": "tileHead", "data": [lingoIO.point([tile.cat.x(), tile.cat.y()]), tile.name]},
                  copy_tile(level.l_tiles(pos, layer))]
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = copy_tile(change[2])
        return change, geochange
    change = [pos, layer,
              {"tp": "tileBody", "data": [lingoIO.point([head.x() + 1, head.y() + 1]), layer + 1]},
              copy_tile(level.l_tiles(pos, layer))]
    level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = copy_tile(change[2])
    return change, geochange


def place_tile(level: RWELevel,
               pos: QPoint,
               layer: int,
               tile: Tile,
               area: list[list[bool]] = None,
               area2: list[list[bool]] = None,
               force_place: bool = False,
               force_geometry: bool = False) -> PlacedTile | None:
    if tile.type == "material":
        change = [pos, layer, {"tp": "material", "data": tile.name}, copy_tile(level.l_tiles(pos, layer))]
        geochange = []
        if force_geometry and level.l_geo.blocks[pos.x(), pos.y(), layer] != 0:
            geochange = [[pos, layer, 1, level.l_geo.blocks[pos.x(), pos.y(), layer]]]
            # level.data["GE"][pos.x()][pos.y()][layer][0] = 1
            level.l_geo.blocks[pos.x(), pos.y(), layer] = np.uint8(1)
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "material", "data": tile.name}
        level.viewport.modulenames["tiles"].get_layer(layer).draw_tile(pos)
        level.viewport.modulenames["geo"].get_layer(layer).draw_geo(pos.x(), pos.y(), True)
        return PlacedTile([change], geochange)
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return None
    changes = []
    geochanges = []
    isnextlayer = isinstance(tile.cols[1], list) and layer + 1 < 3
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
            if isnextlayer:
                if area2 is not None:
                    area2[tilepos.x()][tilepos.y()] = False
                try:
                    col2 = tile.cols[1][x * tile.size.height() + y]
                except IndexError:
                    col2 = 1
                ch, gch = check4tile_col(level, tilepos, headpos, tile, layer + 1, col2, force_place, force_geometry, True)
                if ch is not None:
                    changes.append(ch)
                if gch is not None:
                    geochanges.append(gch)
            ch, gch = check4tile_col(level, tilepos, headpos, tile, layer, col, force_place, force_geometry, False)
            if ch is not None:
                changes.append(ch)
            if gch is not None:
                geochanges.append(gch)
    level.viewport.modulenames["tiles"].get_layer(layer).draw_tile(headpos)
    return PlacedTile(changes, geochanges)


def remove_tile(level: RWELevel, pos: QPoint, layer: int) -> RemovedTile | None:
    if not level.inside(pos):
        return
    data = level.l_tiles(pos, layer)
    tp = data.get("tp", "default")
    head = [lingoIO.point([pos.x() + 1, pos.y() + 1]), layer]
    if tp == "default":
        return
    elif tp == "material":
        change = [pos, layer, {"tp": "material", "data": data.get("data")}]
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "default", "data": 0}
        level.viewport.modulenames["tiles"].get_layer(layer).clean_pixel(pos)
        return RemovedTile([change])
    elif tp == "tileBody":
        head = data.get("data")
        layer = head[1] - 1
    headpos = QPoint(*lingoIO.fromarr(head[0], "point"))
    headpos -= QPoint(1, 1)
    headdata = level.l_tiles(headpos, layer)
    if headdata.get("tp") != "tileHead":
        return
    foundtile = level.manager.tiles[headdata.get("data")[1]]
    if foundtile is None:
        return
    tiledata = {"tp": "tileBody", "data": [lingoIO.point([headpos.x() + 1, headpos.y() + 1]), layer + 1]}
    changes = []
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
                if col2 != -1 and (level.l_tiles(bodypos, layer + 1) == tiledata or level.l_tiles(bodypos, layer + 1)["tp"] == "default"):
                    level.viewport.modulenames["tiles"].get_layer(layer + 1).clean_pixel(bodypos)
                    changes.append([bodypos, layer + 1, copy_tile(level.l_tiles(bodypos, layer + 1))])
                    level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer + 1] = {"tp": "default", "data": 0}
            if (col == -1 or level.l_tiles(bodypos, layer) != tiledata) and level.l_tiles(bodypos, layer)["tp"] != "default":
                continue
            level.viewport.modulenames["tiles"].get_layer(layer).clean_pixel(bodypos)
            changes.append([bodypos, layer, copy_tile(level.l_tiles(bodypos, layer))])
            level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer] = {"tp": "default", "data": 0}
    changes.append([headpos, layer, copy_tile(level.l_tiles(headpos, layer))])
    level.viewport.modulenames["tiles"].get_layer(layer).clean_pixel(headpos)
    level.data["TE"]["tlMatrix"][headpos.x()][headpos.y()][layer] = {"tp": "default", "data": 0}
    return RemovedTile(changes)


class BaseTileChangelist:
    def __init__(self, changes):
        self.changes = changes  # [pos, layer, after, before?]

    def undo(self, element: TileHistory):
        pass

    def redo(self, element: TileHistory):
        pass


class PlacedTile(BaseTileChangelist):
    def __init__(self, changes, geochanges=None):
        super().__init__(changes)
        if geochanges is None:
            geochanges = []
        self.geochanges = geochanges  # [pos, layer, after, before]

    def undo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.viewport.modulenames["tiles"].get_layer(i[1]).clean_pixel(i[0])
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = copy_tile(i[3])
            if i[2]["tp"] in ["tileHead", "material"]:
                element.history.level.viewport.modulenames["tiles"].get_layer(i[1]).draw_tile(i[0])
        for i in self.geochanges:
            element.history.level.l_geo.blocks[i[0].x(), i[0].y(), i[1]] = np.uint8(i[3])
            # element.history.level.data["GE"][i[0].x()][i[0].y()][i[1]][0] = i[3]
            element.history.level.viewport.modulenames["geo"].get_layer(i[1]).draw_geo(i[0].x(), i[0].y(), True)

    def redo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = copy_tile(i[2])
            if i[2]["tp"] in ["tileHead", "material"]:
                element.history.level.viewport.modulenames["tiles"].get_layer(i[1]).draw_tile(i[0])
        for i in self.geochanges:
            element.history.level.l_geo.blocks[i[0].x(), i[0].y(), i[1]] = np.uint8(i[2])
            # element.history.level.data["GE"][i[0].x()][i[0].y()][i[1]][0] = i[2]
            element.history.level.viewport.modulenames["geo"].get_layer(i[1]).draw_geo(i[0].x(), i[0].y(), True)


class RemovedTile(BaseTileChangelist):
    def undo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = i[2]
            if i[2]["tp"] in ["tileHead", "material"]:
                element.history.level.viewport.modulenames["tiles"].get_layer(i[1]).draw_tile(i[0])

    def redo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.viewport.modulenames["tiles"].get_layer(i[1]).clean_pixel(i[0])
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = {"tp": "default", "data": 0}


class TileHistory(HistoryElement):
    def __init__(self, history, tile: Tile, layer: int, force_place=False, force_geometry=False):
        super().__init__(history)
        self.area = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.area2 = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.layer = layer
        self.tile = tile
        self.savedtiles: list[BaseTileChangelist] = []
        self.fp = force_place
        self.fg = force_geometry

    def redraw(self):
        self.history.level.viewport.modulenames["tiles"].get_layer(self.layer).redraw()
        if self.fg:
            self.history.level.viewport.modulenames["geo"].get_layer(self.layer).redraw()
        if self.layer + 1 < 3:
            if self.fg:
                self.history.level.viewport.modulenames["geo"].get_layer(self.layer + 1).redraw()
            self.history.level.viewport.modulenames["tiles"].get_layer(self.layer + 1).redraw()

    def undo_changes(self):
        for i in self.savedtiles:
            i.undo(self)
        self.redraw()

    def redo_changes(self):
        for i in self.savedtiles:
            i.redo(self)
        self.redraw()
