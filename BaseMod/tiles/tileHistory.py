from __future__ import annotations

from BaseMod.tiles.tileUtils import can_place, place_tile, TileHistory
from RWESharp.Utils import draw_line
from RWESharp.Loaders import Tile

from PySide6.QtCore import QPoint


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
