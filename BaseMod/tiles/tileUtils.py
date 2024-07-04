from __future__ import annotations

from PySide6.QtCore import QPoint

from RWESharp.Core import lingoIO, RWELevel
from RWESharp.Loaders import Tile, tile_offset
from RWESharp.Modify import HistoryElement


def copy_tile(tile: dict) -> dict:
    if isinstance(tile.get("data", []), list):
        return {"tp": tile.get("tp", "default"), "data": tile.get("data", []).copy()}
    return {"tp": tile.get("tp", "default"), "data": tile.get("data", "")}


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
        change = [pos, layer, {"tp": "material", "data": tile.name}, copy_tile(level.tile_data(pos, layer))]
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "material", "data": tile.name}
        level.manager.basemod.tilemodule.get_layer(layer).draw_tile(pos)
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return PlacedTile([change])
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return None
    changes = []
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
                    newpos = lingoIO.makearr([headpos.x() + 1, headpos.y() + 1], "point")
                    change = [tilepos, layer + 1, {"tp": "tileBody", "data": [newpos, layer + 1]}, copy_tile(level.tile_data(tilepos, layer + 1))]
                    changes.append(change)
                    level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer + 1] = {"tp": "tileBody", "data": [newpos, layer + 1]}
            if col == -1:
                continue
            if tilepos == headpos:
                change = [tilepos, layer, {"tp": "tileHead", "data": [lingoIO.makearr([tile.cat.x(), tile.cat.y()], "point"), tile.name]}, copy_tile(level.tile_data(tilepos, layer + 1))]
                changes.append(change)
                level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer] = {"tp": "tileHead", "data": [
                    lingoIO.makearr([tile.cat.x(), tile.cat.y()], "point"), tile.name]}
                continue
            change = [tilepos, layer,
                      {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x() + 1, headpos.y() + 1], "point"), layer + 1]},
                      copy_tile(level.tile_data(tilepos, layer))]
            changes.append(change)
            level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer] = \
                {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x() + 1, headpos.y() + 1], "point"), layer + 1]}
    level.manager.basemod.tilemodule.get_layer(layer).draw_tile(headpos)
    return PlacedTile(changes)


def remove_tile(level: RWELevel, pos: QPoint, layer: int) -> RemovedTile | None:
    if not level.inside(pos):
        return
    data = level.tile_data(pos, layer)
    tp = data.get("tp", "default")
    head = [lingoIO.makearr([pos.x() + 1, pos.y() + 1], "point"), layer]
    if tp == "default":
        return
    elif tp == "material":
        change = [pos, layer, {"tp": "material", "data": data.get("data")}]
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "default", "data": 0}
        level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(pos)
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return RemovedTile([change])
    elif tp == "tileBody":
        head = data.get("data")
        layer = head[1] - 1
    print(head)
    headpos = QPoint(*lingoIO.fromarr(head[0], "point"))
    headpos -= QPoint(1, 1)
    headdata = level.tile_data(headpos, layer)
    if headdata.get("tp") != "tileHead":
        return
    foundtile = level.manager.tiles[headdata.get("data")[1]]
    if foundtile is None:
        return
    tiledata = {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x() + 1, headpos.y() + 1], "point"), layer + 1]}
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
                if col2 != -1 and level.tile_data(bodypos, layer + 1) == tiledata:
                    changes.append([bodypos, layer + 1, copy_tile(level.tile_data(bodypos, layer + 1))])
                    level.manager.basemod.tilemodule.get_layer(layer + 1).clean_pixel(bodypos)
                    level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer + 1] = {"tp": "default", "data": 0}
            print(tiledata, level.tile_data(bodypos, layer))
            if col == -1 or level.tile_data(bodypos, layer) != tiledata:
                continue
            changes.append([bodypos, layer, copy_tile(level.tile_data(bodypos, layer))])
            level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(bodypos)
            level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer] = {"tp": "default", "data": 0}
    changes.append([headpos, layer, copy_tile(level.tile_data(headpos, layer))])
    level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(headpos)
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
    def undo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.manager.basemod.tilemodule.get_layer(i[1]).clean_pixel(i[0])
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = copy_tile(i[3])
            if i[2]["tp"] in ["tileHead", "material"]:
                element.history.level.manager.basemod.tilemodule.get_layer(i[1]).draw_tile(i[0])

    def redo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = copy_tile(i[2])
            if i[2]["tp"] in ["tileHead", "material"]:
                element.history.level.manager.basemod.tilemodule.get_layer(i[1]).draw_tile(i[0])


class RemovedTile(BaseTileChangelist):
    def undo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = i[2]
            if i[2]["tp"] in ["tileHead", "material"]:
                element.history.level.manager.basemod.tilemodule.get_layer(i[1]).draw_tile(i[0])

    def redo(self, element: TileHistory):
        for i in self.changes:
            element.history.level.manager.basemod.tilemodule.get_layer(i[1]).clean_pixel(i[0])
            element.history.level.data["TE"]["tlMatrix"][i[0].x()][i[0].y()][i[1]] = {"tp": "default", "data": 0}


class TileHistory(HistoryElement):
    def __init__(self, history, tile: Tile, layer: int):
        super().__init__(history)
        self.area = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.area2 = [[True for _ in range(self.history.level.level_height)] for _ in range(self.history.level.level_width)]
        self.layer = layer
        self.tile = tile
        self.savedtiles: list[BaseTileChangelist] = []

    def undo_changes(self, level):
        for i in self.savedtiles:
            i.undo(self)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()
        if self.layer + 1 < 3:
            self.history.level.manager.basemod.tilemodule.get_layer(self.layer + 1).redraw()

    def redo_changes(self, level):
        for i in self.savedtiles:
            i.redo(self)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()
        if self.layer + 1 < 3:
            self.history.level.manager.basemod.tilemodule.get_layer(self.layer + 1).redraw()
