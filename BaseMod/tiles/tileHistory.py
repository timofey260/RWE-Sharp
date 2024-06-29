from __future__ import annotations

from BaseMod.tiles.tileEditor import can_place, place_tile, remove_tile
from RWESharp.Modify import HistoryElement
from RWESharp.Loaders import Tile
from RWESharp.Utils import draw_line
from PySide6.QtCore import QPoint


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


class TilePen(TileHistory):
    def __init__(self, history, start: QPoint, tile: Tile, layer: int):
        super().__init__(history, tile, layer)
        self.positions = []
        self.start = start

        if can_place(self.history.level, self.start, self.layer, self.tile, self.area, self.area2, False, False):
            tile = place_tile(self.history.level, self.start, self.layer, self.tile, self.area, self.area2, False, False)
            if tile is not None:
                self.savedtiles.append(tile)

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            canplace = can_place(self.history.level, point, self.layer, self.tile, self.area, self.area2, False, False)
            if canplace:
                tile = place_tile(self.history.level, point, self.layer, self.tile, self.area, self.area2, False, False)
                if tile is not None:
                    self.savedtiles.append(tile)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()
