from __future__ import annotations

from PySide6.QtCore import QPoint, QRect

from BaseMod.tiles.tileUtils import can_place, place_tile, TileHistory, remove_tile, PlacedTileBody
from RWESharp.Modify.HistoryElement import HistoryElement
from RWESharp2.Loaders import Tile
from RWESharp2.Utils import draw_line, draw_rect, draw_ellipse


class TilePen(TileHistory):
    def __init__(self, history, start: QPoint, tile: Tile, layer: int,
                 delete=False, force_place=False, force_geometry=False, strict=True):
        super().__init__(history, tile, layer, force_place, force_geometry)
        self.positions = []
        self.start = start
        self.delete = delete
        self.strict = strict

        if delete:
            tile = remove_tile(history.level, start, layer, strict)
            if tile is not None:
                self.savedtiles.append(tile)
        elif can_place(self.history.level, start, layer, tile, self.fp, self.fg, self.area, self.area2):
            tile = place_tile(self.history.level, start, layer, tile, self.area, self.area2, self.fp, self.fg)
            if tile is not None:
                self.savedtiles.append(tile)
        self.redraw()

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            if self.delete:
                tile = remove_tile(self.history.level, point, self.layer, self.strict)
                if tile is not None:
                    self.savedtiles.append(tile)
            elif can_place(self.history.level, point, self.layer, self.tile, self.fp, self.fg, self.area, self.area2):
                tile = place_tile(self.history.level, point, self.layer, self.tile, self.area, self.area2, self.fp, self.fg)
                if tile is not None:
                    self.savedtiles.append(tile)
        self.redraw()

class TileBrush(TileHistory):
    def __init__(self, history, start: QPoint, tile: Tile, layer: int, radius: float,
                 delete=False, force_place=False, force_geometry=False, strict=True):
        super().__init__(history, tile, layer, force_place, force_geometry)
        self.positions = []
        self.start = start
        self.delete = delete
        self.strict = strict
        self.radius = radius

        r2 = round(self.radius / 2)
        rect = QRect(start.x() - r2, start.y() - r2, self.radius, self.radius)
        draw_ellipse(rect, False, self.paint_circle)
        self.redraw()

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        r2 = round(self.radius / 2)
        for point in points:
            rect = QRect(point.x() - r2, point.y() - r2, self.radius, self.radius)
            draw_ellipse(rect, False, self.paint_circle)
        self.redraw()

    def paint_circle(self, point: QPoint):
        if self.delete:
            tile = remove_tile(self.history.level, point, self.layer, self.strict)
            if tile is not None:
                self.savedtiles.append(tile)
        elif can_place(self.history.level, point, self.layer, self.tile, self.fp, self.fg, self.area, self.area2):
            tile = place_tile(self.history.level, point, self.layer, self.tile, self.area, self.area2, self.fp, self.fg)
            if tile is not None:
                self.savedtiles.append(tile)


class TileRectangle(TileHistory):
    def __init__(self, history, rect: QRect, tile: Tile, layer: int, hollow=False,
                 delete=False, force_place=False, force_geometry=False, strict=True):
        super().__init__(history, tile, layer, force_place, force_geometry)
        self.positions = []
        self.rect = rect
        self.delete = delete
        self.strict = strict
        self.hollow = hollow

        draw_rect(rect, hollow, self.place_tile)
        self.redraw()

    def place_tile(self, point: QPoint):
        if self.delete:
            tile = remove_tile(self.history.level, point, self.layer, self.strict)
            if tile is not None:
                self.savedtiles.append(tile)
        elif can_place(self.history.level, point, self.layer, self.tile, self.fp, self.fg, self.area, self.area2):
            tile = place_tile(self.history.level, point, self.layer, self.tile, self.area, self.area2, self.fp, self.fg)
            if tile is not None:
                self.savedtiles.append(tile)


class TileEllipse(TileHistory):
    def __init__(self, history, rect: QRect, tile: Tile, layer: int, hollow=False,
                 delete=False, force_place=False, force_geometry=False, strict=True):
        super().__init__(history, tile, layer, force_place, force_geometry)
        self.positions = []
        self.rect = rect
        self.delete = delete
        self.strict = strict
        self.hollow = hollow

        draw_ellipse(rect, hollow, self.place_tile)
        self.redraw()

    def place_tile(self, point: QPoint):
        if self.delete:
            tile = remove_tile(self.history.level, point, self.layer, self.strict)
            if tile is not None:
                self.savedtiles.append(tile)
        elif can_place(self.history.level, point, self.layer, self.tile, self.fp, self.fg, self.area, self.area2):
            tile = place_tile(self.history.level, point, self.layer, self.tile, self.area, self.area2, self.fp, self.fg)
            if tile is not None:
                self.savedtiles.append(tile)


class TileLine(TileBrush):
    def __init__(self, history, start: QPoint, end: QPoint, tile: Tile, layer: int,
                 radius: int, delete=False, force_place=False, force_geometry=False, strict=True):
        super().__init__(history, start, tile, layer, radius, delete, force_place, force_geometry, strict)
        self.start = start
        self.end = end

        self.add_move(end)
        self.redraw()


class LevelResizedTiles(HistoryElement):
    def __init__(self, history, changerect: QRect):
        super().__init__(history)
        self.changerect = changerect
        self.oldtiles = None
        self.module = self.level.viewport.modulenames["tiles"]
        self.redo_changes()

    def undo_changes(self):
        self.module.l1.clear_scene()
        self.module.l2.clear_scene()
        self.module.l3.clear_scene()
        self.level.l_tiles.tiles = self.oldtiles  # definitely gonna have some memory issues later
        self.module.l1.fill_scene()
        self.module.l2.fill_scene()
        self.module.l3.fill_scene()

    def redo_changes(self):
        self.module.l1.clear_scene()
        self.module.l2.clear_scene()
        self.module.l3.clear_scene()
        newtiles = []
        for x in range(self.changerect.width()):
            newtiles.append([])
            for y in range(self.changerect.height()):
                newtiles[-1].append(self.getnewpixel(x, y))
        self.oldtiles, self.level.l_tiles.tiles = self.level.l_tiles.tiles, newtiles
        self.module.l1.fill_scene()
        self.module.l2.fill_scene()
        self.module.l3.fill_scene()

    def getnewpixel(self, x, y):
        if x < -self.changerect.x() or y < -self.changerect.y():
            return [None, None, None]
        newpoints = [x + self.changerect.x(), y + self.changerect.y()]
        if newpoints[0] >= len(self.level.l_tiles.tiles) or newpoints[1] >= len(self.level.l_tiles.tiles[0]):
            return [None, None, None]
        return [self.copytile(newpoints[0], newpoints[1], 0),
                self.copytile(newpoints[0], newpoints[1], 1),
                self.copytile(newpoints[0], newpoints[1], 2)]

    def copytile(self, x, y, l):
        thing = self.level.l_tiles.tiles[x][y][l]
        if isinstance(thing, PlacedTileBody) and not self.level.inside(thing.headpos):
            return None
        if thing is None:
            return None
        return thing.copy()

class DefaultMaterialChange(HistoryElement):
    def __init__(self, history, material: str):
        super().__init__(history)
        self.before = self.level.l_tiles.default_material
        self.after = material
        self.redo_changes()

    def undo_changes(self):
        self.level.l_tiles.default_material = self.before
        self.manager.basemod.tileui.set_default_material()

    def redo_changes(self):
        self.level.l_tiles.default_material = self.after
        self.manager.basemod.tileui.set_default_material()