from __future__ import annotations

from BaseMod.tiles.tileUtils import can_place, place_tile, TileHistory, remove_tile
from RWESharp.Utils import draw_line
from RWESharp.Loaders import Tile

from PySide6.QtCore import QPoint


class TilePen(TileHistory):
    def __init__(self, history, start: QPoint, tile: Tile, layer: int, delete=False):
        super().__init__(history, tile, layer)
        self.positions = []
        self.start = start
        self.delete = delete

        if delete:
            tile = remove_tile(history.level, start, layer)
            if tile is not None:
                self.savedtiles.append(tile)
        elif can_place(self.history.level, start, layer, tile, self.area, self.area2, False, False):
            tile = place_tile(self.history.level, start, layer, tile, self.area, self.area2, False, False)
            if tile is not None:
                self.savedtiles.append(tile)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()
        if layer + 1 < 3:
            self.history.level.manager.basemod.tilemodule.get_layer(self.layer + 1).redraw()

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
                tile = remove_tile(self.history.level, point, self.layer)
                if tile is not None:
                    self.savedtiles.append(tile)
            elif can_place(self.history.level, point, self.layer, self.tile, self.area, self.area2, False, False):
                tile = place_tile(self.history.level, point, self.layer, self.tile, self.area, self.area2, False, False)
                if tile is not None:
                    self.savedtiles.append(tile)
        self.history.level.manager.basemod.tilemodule.get_layer(self.layer).redraw()
        if self.layer + 1 < 3:
            self.history.level.manager.basemod.tilemodule.get_layer(self.layer + 1).redraw()
