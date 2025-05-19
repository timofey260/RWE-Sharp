from __future__ import annotations

import numpy as np

from PySide6.QtCore import QPoint, QRect, QSize
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsRectItem

from RWESharp.Core import RWELevel, CELLSIZE
from RWESharp.Loaders import Tile
from RWESharp.Modify import HistoryElement


class PlacedTileHead:
    def __init__(self, tile: Tile, pos: QPoint, layer: int):
        self.tile = tile
        # self.tilebodies = []
        self.pos = pos
        self.layer = layer
        self.graphics: list[QGraphicsPixmapItem] = []

    def tostring(self, level):
        return self.tile.name

    def remove(self, level, redraw=True):
        # for i in self.tilebodies:
        #     i.remove(level)
        # not recommended to use this method since it doesn't create any history
        ofs = self.tile.top_left
        pos = self.pos - ofs
        for x in range(pos.x(), pos.x() + self.tile.size.width()):
            for y in range(pos.y(), pos.y() + self.tile.size.height()):
                tile = level.l_tiles.tiles[x][y][self.layer]
                if isinstance(tile, PlacedTileBody) and tile.headpos == self.pos and tile.headlayer == self.layer:
                    tile.remove(level)
        if self.tile.multilayer and self.layer < 2:
            for x in range(pos.x(), pos.x() + self.tile.size.width()):
                for y in range(pos.y(), pos.y() + self.tile.size.height()):
                    tile = level.l_tiles.tiles[x][y][self.layer + 1]
                    if isinstance(tile, PlacedTileBody) and tile.headpos == self.pos and tile.headlayer == self.layer:
                        tile.remove(level)
        level.l_tiles[self.pos][self.layer] = None
        self.remove_graphics(level, redraw)

    def remove_graphics(self, level, redraw=True):
        bounds = self.tile_bounds
        if len(self.graphics) > 0:
            for i in self.graphics:
                i.removeFromIndex()
            self.graphics.clear()
            self.graphics = []
        texture = level.viewport.modulenames["tiles"].get_layer(self.layer)
        texture.render_rect(bounds)
        if redraw:
            texture.redraw()

    def add_graphics(self, level, redraw=True):
        if len(self.graphics) > 0:
            self.remove_graphics(level, False)
        layer = level.viewport.modulenames["tiles"].get_layer(self.layer)
        layer.draw_tile(self.pos, True)
        if redraw:
            layer.redraw()

    @property
    def tile_bounds(self):
        tl = (self.pos - self.tile.option_based_top_left(1)) * CELLSIZE
        return QRect(tl, (self.tile.size + QSize(self.tile.bfTiles, self.tile.bfTiles) * 2) * CELLSIZE)

    def copy(self):
        return PlacedTileHead(self.tile, self.pos.__copy__(), self.layer)


class PlacedTileBody:
    def __init__(self, tileheadpos: QPoint, headlayer, pos: QPoint, layer: int):
        self.headpos = tileheadpos
        self.headlayer = headlayer
        self.pos = pos
        self.layer = layer

    def tilehead(self, level):
        return level.l_tiles[self.headpos][self.headlayer]

    def tostring(self, level):
        if not isinstance(level.l_tiles[self.headpos][self.headlayer], PlacedTileHead):
            return "Error"
        return self.tilehead(level).tile.name

    def remove(self, level: RWELevel):
        level.l_tiles[self.pos][self.layer] = None

    def remove_graphics(self, *args):
        pass

    def add_graphics(self, *args):
        pass

    def tile(self, level) -> Tile:
        return self.tilehead(level).tile

    def copy(self):
        return PlacedTileBody(self.headpos.__copy__(), self.headlayer, self.pos.__copy__(), self.layer)


class PlacedMaterial:
    def __init__(self, tile: Tile, pos: QPoint, layer: int):
        self.tile = tile
        self.graphics: list[QGraphicsRectItem] = []
        self.pos = pos
        self.layer = layer

    def tostring(self, level):
        return self.tile.name

    def copy(self):
        return PlacedMaterial(self.tile, self.pos.__copy__(), self.layer)

    def remove(self, level, redraw=True):
        level.l_tiles[self.pos][self.layer] = None
        self.remove_graphics(level, redraw)

    def remove_graphics(self, level, redraw=True):
        bounds = self.tile_bounds
        if len(self.graphics) > 0:
            for i in self.graphics:
                i.removeFromIndex()
            self.graphics.clear()
            self.graphics = []
        texture = level.viewport.modulenames["tiles"].get_layer(self.layer)
        texture.render_rect(bounds)
        if redraw:
            texture.redraw()

    def add_graphics(self, level, redraw=True):
        if len(self.graphics) > 0:
            self.remove_graphics(level, False)
        layer = level.viewport.modulenames["tiles"].get_layer(self.layer)
        layer.draw_tile(self.pos, True)
        if redraw:
            layer.redraw()

    @property
    def tile_bounds(self):
        return QRect(self.pos * CELLSIZE, QSize(CELLSIZE, CELLSIZE))


def can_place(level: RWELevel, pos: QPoint, layer: int, tile: Tile, force_place: bool, force_geometry: bool,
              area: list[list[bool]] = None, area2: list[list[bool]] = None) -> bool:
    headpos = tile.top_left + pos
    if not level.inside(headpos):
        return False
    # if area is available
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            if not level.inside(QPoint(x, y)):
                continue
            if area is not None and not area[x][y]:
                return False
            if area2 is not None and isinstance(tile.cols1, list) and not area2[x][y]:
                return False
    return check_collisions(level, pos, layer, tile, force_place, force_geometry)


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


def point_collision(level: RWELevel, pos: QPoint, layer: int, tilepos: QPoint, tile: Tile, force_place: bool = False, force_geometry: bool = False) -> bool:
    tiledata = level.l_tiles(pos, layer)
    try:
        collision = tile.cols[tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1

    # checking tile-tile collisions
    if isinstance(tiledata, PlacedTileHead) and collision != -1:  # when we know we are placing block on tile head
        return False
    elif not force_place and tiledata is not None and not isinstance(tiledata, PlacedMaterial): return False # when it's not force place

    # checking tile_geo collisions
    geodata = level.l_geo.blocks[pos.x(), pos.y(), layer]
    if collision != -1 and geodata != collision and not force_geometry and not force_place: return False

    # next layer(if exists)
    if not isinstance(tile.cols1, list) or layer > 1: return True

    try:
        collision = tile.cols1[tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if collision != -1:
        return True
    # checking tile-tile collision on next layer
    tiledata = level.l_tiles(pos, layer + 1)
    if isinstance(tiledata, PlacedTileHead) and collision != -1:  # when we know we are placing block on tile head
        return False
    elif not force_place and tiledata is not None and not isinstance(tiledata, PlacedMaterial): return False  # when it's not force place

    # checking tile-geo collision on next layer
    geodata = level.l_geo.blocks[pos.x(), pos.y(), layer + 1]
    if collision != -1 and geodata != collision and not force_geometry and not force_place: return False

    return True


def copy_tile(tile: PlacedTileHead | PlacedTileBody | PlacedMaterial | None):
    if tile is None:
        return None
    return tile.copy()


def tile_changes(level: RWELevel,
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
    if fp and isinstance(level.l_tiles[pos][layer], PlacedTileHead):
        return None, None
    elif not fp and level.l_tiles[pos][layer] is not None:
        return None, None
    #level.viewport.modulenames["tiles"].get_layer(layer).clean_pixel(pos)
    if fg and col != level.l_geo.blocks[pos.x(), pos.y(), layer]:
        geochange = [pos, layer, level.l_geo.blocks[pos.x(), pos.y(), layer], col]
        level.l_geo.blocks[pos.x(), pos.y(), layer] = np.uint8(col)
        # level.data["GE"][pos.x()][pos.y()][layer][0] = col
        level.viewport.modulenames["geo"].get_layer(layer).draw_geo(pos.x(), pos.y(), True)
    if not secondlayer and pos == head:
        change = [copy_tile(level.l_tiles(pos, layer)), PlacedTileHead(tile, pos, layer)]
        if level.l_tiles[pos][layer] is not None:
            level.l_tiles[pos][layer].remove_graphics(level, True)
        # change = [pos, layer,
        #           {"tp": "tileHead", "data": [lingoIO.point([tile.cat.x(), tile.cat.y()]), tile.name]},
        #           copy_tile(level.l_tiles(pos, layer))]
        level.l_tiles[pos][layer] = copy_tile(change[1])
        return change, geochange
    change = [copy_tile(level.l_tiles[pos][layer]), PlacedTileBody(head, layer + (1 if secondlayer else 0), pos, layer)]
    if level.l_tiles[pos][layer] is not None:
        level.l_tiles[pos][layer].remove_graphics(level, True)
    # change = [pos, layer,
    #           {"tp": "tileBody", "data": [lingoIO.point([head.x() + 1, head.y() + 1]), layer + 1]},
    #           copy_tile(level.l_tiles(pos, layer))]
    level.l_tiles[pos][layer] = copy_tile(change[1])
    return change, geochange


def place_tile(level: RWELevel,
               pos: QPoint,
               layer: int,
               tile: Tile,
               area: np.array = None,
               area2: np.array = None,
               force_place: bool = False,
               force_geometry: bool = False) -> PlacedTile | None:
    if tile.type == "material" and area[pos.x(), pos.y()]:
        change = [copy_tile(level.l_tiles[pos][layer]), PlacedMaterial(tile, pos, layer)]
        geochange = []
        if force_geometry and level.l_geo.blocks[pos.x(), pos.y(), layer] != 0:
            geochange = [[pos, layer, level.l_geo.blocks[pos.x(), pos.y(), layer], 1]]
            # level.data["GE"][pos.x()][pos.y()][layer][0] = 1
            level.l_geo.blocks[pos.x(), pos.y(), layer] = np.uint8(1)
        #level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "material", "data": tile.name}
        if level.l_tiles[pos][layer] is not None:
            level.l_tiles[pos][layer].remove_graphics(level, True)
        level.l_tiles[pos][layer] = PlacedMaterial(tile, pos, layer)
        area[pos.x(), pos.y()] = False
        level.viewport.modulenames["tiles"].get_layer(layer).draw_tile(pos, True)
        level.viewport.modulenames["geo"].get_layer(layer).draw_geo(pos.x(), pos.y(), True)
        return PlacedTile(level, [change], geochange)
    headpos = tile.top_left + pos
    if not level.inside(headpos):
        return None
    changes = []
    geochanges = []
    isnextlayer = tile.multilayer and layer < 2
    for x in range(tile.size.width()):
        for y in range(tile.size.height()):
            tilepos = QPoint(x, y) + pos
            if not level.inside(tilepos):
                continue
            if area is not None:
                area[tilepos.x(), tilepos.y()] = False
            # area2[x][y] = False
            try:
                col = tile.cols[x * tile.size.height() + y]
            except IndexError:
                col = 1
            if isnextlayer:
                if area2 is not None:
                    area2[tilepos.x(), tilepos.y()] = False
                try:
                    col2 = tile.cols1[x * tile.size.height() + y]
                except IndexError:
                    col2 = 1
                ch, gch = tile_changes(level, tilepos, headpos, tile, layer + 1, col2, force_place, force_geometry, True)
                if ch is not None:
                    changes.append(ch)
                if gch is not None:
                    geochanges.append(gch)
            ch, gch = tile_changes(level, tilepos, headpos, tile, layer, col, force_place, force_geometry, False)
            if ch is not None:
                changes.append(ch)
            if gch is not None:
                geochanges.append(gch)
    level.viewport.modulenames["tiles"].get_layer(layer).draw_tile(headpos, True)
    return PlacedTile(level, changes, geochanges)


def remove_tile(level: RWELevel, pos: QPoint, layer: int, strict=True):
    tile = level.l_tiles[pos][layer]
    if tile is None:
        return None
    if isinstance(tile, PlacedMaterial):
        tile.remove(level, True)
        return RemovedTile([[copy_tile(tile), None]], level)
    headpos = tile.headpos if isinstance(tile, PlacedTileBody) else pos
    headlayer = tile.headlayer if isinstance(tile, PlacedTileBody) else layer
    headtile = level.l_tiles[headpos][headlayer]
    if not isinstance(headtile, PlacedTileHead):
        return None
    changes = []
    tilesize = headtile.tile.size
    tl = headpos - headtile.tile.top_left
    for x in range(tl.x(), tl.x() + tilesize.width()):
        for y in range(tl.y(), tl.y() + tilesize.height()):
            # searching for tilebodies
            tb = level.l_tiles[QPoint(x, y)][layer]
            if QPoint(x, y) == headpos and isinstance(tb, PlacedTileHead):
                tb.remove_graphics(level, True)
                changes.append([copy_tile(tb), None])
                level.l_tiles[QPoint(x, y)][layer] = None
                continue
            if not isinstance(tb, PlacedTileBody):
                continue
            if strict and tb.headpos != headpos:
                continue
            changes.append([copy_tile(tb), None])
            level.l_tiles[QPoint(x, y)][layer] = None
    if not headtile.tile.multilayer or layer >= 2:
        return RemovedTile(changes, level)
    for x in range(tl.x(), tl.x() + tilesize.width()):
        for y in range(tl.y(), tl.y() + tilesize.height()):
            # searching for tilebodies
            tb = level.l_tiles[QPoint(x, y)][layer + 1]
            if not isinstance(tb, PlacedTileBody):
                continue
            if strict and tb.headpos != headpos:
                continue
            changes.append([copy_tile(tb), None])
            level.l_tiles[QPoint(x, y)][layer + 1] = None
    return RemovedTile(changes, level)


class BaseTileChangelist:
    def __init__(self, changes, level: RWELevel):
        self.changes = changes  # [before, after]
        self.level = level
        self.module = level.viewport.modulenames["tiles"]

    def undo(self):
        layers2redraw = [False, False, False]
        for i in self.changes:
            before: PlacedTileHead | PlacedTileBody | PlacedMaterial | None = i[0]
            after: PlacedTileHead | PlacedTileBody | PlacedMaterial | None = i[1]
            if before is None:
                if after is None:
                    continue
                pos = after.pos
                layer = after.layer
                if self.level.l_tiles[pos][layer] is not None:
                    self.level.l_tiles[pos][layer].remove_graphics(self.level, False)
                self.level.l_tiles[pos][layer] = None
                layers2redraw[layer] = True
                continue
            pos = before.pos
            layer = before.layer
            if self.level.l_tiles[pos][layer] is not None:
                self.level.l_tiles[pos][layer].remove_graphics(self.level, False)
            self.level.l_tiles[pos][layer] = before.copy()
            self.level.l_tiles[pos][layer].add_graphics(self.level, False)
            layers2redraw[layer] = True
        [self.module.get_layer(i).redraw() for i in layers2redraw if i]

    def redo(self):
        layers2redraw = [False, False, False]
        for i in self.changes:
            before: PlacedTileHead | PlacedTileBody | PlacedMaterial | None = i[0]
            after: PlacedTileHead | PlacedTileBody | PlacedMaterial | None = i[1]
            if after is None:
                if before is None:
                    continue
                pos = before.pos
                layer = before.layer
                if self.level.l_tiles.tiles[pos.x()][pos.y()][layer] is not None:
                    self.level.l_tiles.tiles[pos.x()][pos.y()][layer].remove_graphics(self.level, False)
                self.level.l_tiles.tiles[pos.x()][pos.y()][layer] = None
                layers2redraw[layer] = True
                continue
            pos = after.pos
            layer = after.layer
            if self.level.l_tiles[pos][layer] is not None:
                self.level.l_tiles[pos][layer].remove_graphics(self.level, False)
            self.level.l_tiles.tiles[pos.x()][pos.y()][layer] = after.copy()
            self.level.l_tiles.tiles[pos.x()][pos.y()][layer].add_graphics(self.level, False)
            layers2redraw[layer] = True
        [self.module.get_layer(i).redraw() for i in layers2redraw if i]


class PlacedTile(BaseTileChangelist):
    def __init__(self, level, changes, geochanges=None):
        super().__init__(changes, level)
        if geochanges is None:
            geochanges = []
        self.geochanges = geochanges  # [pos, layer, after, before]

    def undo(self):
        super().undo()
        for i in self.geochanges:
            self.level.l_geo.blocks[i[0].x(), i[0].y(), i[1]] = np.uint8(i[2])
            # element.history.level.data["GE"][i[0].x()][i[0].y()][i[1]][0] = i[3]
            self.level.viewport.modulenames["geo"].get_layer(i[1]).draw_geo(i[0].x(), i[0].y(), True)

    def redo(self):
        super().redo()
        for i in self.geochanges:
            self.level.history.level.l_geo.blocks[i[0].x(), i[0].y(), i[1]] = np.uint8(i[3])
            # element.history.level.data["GE"][i[0].x()][i[0].y()][i[1]][0] = i[2]
            self.level.viewport.modulenames["geo"].get_layer(i[1]).draw_geo(i[0].x(), i[0].y(), True)


class RemovedTile(BaseTileChangelist):
    pass


class TileHistory(HistoryElement):
    def __init__(self, history, tile: Tile, layer: int, force_place=False, force_geometry=False):
        super().__init__(history)
        self.area = np.ones([self.history.level.level_width, self.history.level.level_height], np.bool)
        self.area2 = np.ones([self.history.level.level_width, self.history.level.level_height], np.bool)
        self.layer = layer
        self.tile = tile
        self.savedtiles: list[BaseTileChangelist] = []
        self.fp = force_place
        self.fg = force_geometry
        self.tilemodule = self.level.viewport.modulenames["tiles"]
        self.geomodule = self.level.viewport.modulenames["geo"]

    def redraw(self):
        self.tilemodule.get_layer(self.layer).redraw()
        if self.fg:
            self.geomodule.get_layer(self.layer).redraw()
        if self.layer < 2:
            if self.fg:
                self.geomodule.get_layer(self.layer + 1).redraw()
            self.tilemodule.get_layer(self.layer + 1).redraw()

    def undo_changes(self):
        for i in self.savedtiles:
            i.undo()
        self.redraw()

    def redo_changes(self):
        for i in self.savedtiles:
            i.redo()
        self.redraw()
