from __future__ import annotations
from RWESharp.Modify import EditorMode
from RWESharp.Loaders import Tile
from RWESharp.Core import CELLSIZE
from PySide6.QtGui import QPixmap, QColor, QPainter
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtCore import QPoint
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BaseMod.baseMod import BaseMod


class EditorTile:
    def __init__(self, editor: TileEditor):
        self.editor = editor
        self.tile: Tile | None
        self.image = QPixmap(1, 1)
        self.painter = QPainter(self.image)

    def load_tile(self, tile):
        self.image = QPixmap((tile.size.x() + tile.bfTiles) * CELLSIZE, (tile.size.y() + tile.bfTiles) * CELLSIZE)
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.drawPixmap(QPoint(0, 0), tile.image2)


class TileEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        mod: BaseMod
        self.collisions = []
        self.explorer = mod.tile_explorer
        self.tile = EditorTile(self)
        self.explorer.tileSelected.connect(self.add_tile)
        self.tile_image: QGraphicsPixmapItem | None = None

    def add_tile(self, tiles):
        self.tile.load_tile(tiles[0])
        if self.tile_image is not None:
            self.tile_image.setPixmap(self.tile.image)

    def init_scene_items(self):
        self.tile_image = self.workscene.addPixmap(self.tile.image)
        print("lol")

    def remove_items_from_scene(self):
        self.tile_image.removeFromIndex()