from __future__ import annotations

from BaseMod.tiles.tileUtils import can_place, place_tile, TileHistory, remove_tile
from RWESharp.Utils import draw_line, draw_rect, draw_ellipse
from RWESharp.Loaders import Tile

from PySide6.QtCore import QPoint, QRect


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


class TileLine(TileHistory):  # todo make it better
    def __init__(self, history, start: QPoint, end: QPoint, tile: Tile, layer: int,
                 delete=False, force_place=False, force_geometry=False, strict=True):
        super().__init__(history, tile, layer, force_place, force_geometry)
        self.positions = []
        self.start = start
        self.end = end
        self.delete = delete
        self.strict = strict

        draw_line(start, end, self.place_tile)
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