from __future__ import annotations
from PySide6.QtCore import QPoint, Qt, QPointF
from PySide6.QtGui import QPixmap
from RWESharp.Core import CELLSIZE, SPRITESIZE
from RWESharp.Loaders import Tile, collisions_image, return_tile_pixmap
from typing import TYPE_CHECKING

from widgets.SimpleViewport import SimpleViewport

if TYPE_CHECKING:
    pass


class TilePreview(SimpleViewport):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.tile: Tile | None = None
        self.drawoption = 0
        self.layer = 0
        self.colortable = []
        self.tileimage = self.workscene.addPixmap(QPixmap())
        self.tilecolsimage = self.workscene.addPixmap(QPixmap())

    def preview_tile(self, tile, drawoption=0, layer=0, colortable=None):
        self.tile = tile
        self.drawoption = drawoption
        self.layer = layer
        if colortable is not None:
            self.colortable = colortable
        self.tileimage.setOpacity(1)
        self.tileimage.setPixmap(return_tile_pixmap(self.tile, self.drawoption, self.layer, self.colortable))
        self.tilecolsimage.setPixmap(collisions_image(tile))
        if self.drawoption == 0:
            self.tileimage.setScale(self.zoom * (CELLSIZE / SPRITESIZE))
        else:
            self.tileimage.setScale(self.zoom)
        self.set_pos(QPoint(0, 0))
        self.verticalScrollBar().setValue(0)
        self.horizontalScrollBar().setValue(0)

    def set_pos(self, pos: QPointF | QPoint):
        if self.tile is None:
            return
        super().set_pos(pos)
        if self.drawoption != 0:
            self.tileimage.setPos(self.topleft.pos() - QPoint(self.tile.bfTiles, self.tile.bfTiles) * CELLSIZE * self.zoom)
        else:
            self.tileimage.setPos(self.topleft.pos())
        self.tilecolsimage.setPos(self.topleft.pos())

    def wheelEvent(self, event):
        super().wheelEvent(event)
        if self.drawoption == 0:
            self.tileimage.setScale(self.zoom * (CELLSIZE / SPRITESIZE))
        else:
            self.tileimage.setScale(self.zoom)
        self.tilecolsimage.setScale(self.zoom)

