from PySide6.QtCore import QPointF, QPoint

from RWESharpWidgets import SimpleViewport
from RWESharp.Loaders import Tile, collisions_image, return_tile_pixmap, palette_to_colortable
from RWESharp.Core import CELLSIZE, SPRITESIZE
from PySide6.QtGui import QPixmap, QImage


class TileSettingsViewport(SimpleViewport):
    def __init__(self, parent=None):
        super().__init__(parent)
        from BaseMod.tiles.tileUIConnectors import TileSettings
        self.tilel1 = self.workscene.addPixmap(QPixmap())
        self.tilel2 = self.workscene.addPixmap(QPixmap())
        self.tilel3 = self.workscene.addPixmap(QPixmap())
        self.colortable = None
        self.drawoption = 0
        self.ui: TileSettings | None = None
        self.set_mappos()

    def add_manager(self, manager, ui):
        super().add_manager(manager)
        self.ui = ui
        self.redraw()

    def redraw(self):
        self.colortable = self.manager.basemod.tilemodule.colortable
        tile = self.manager.tiles["Four Holes"]
        self.tilel1.setPixmap(return_tile_pixmap(tile, self.drawoption, 0, self.colortable))
        self.tilel2.setPixmap(return_tile_pixmap(tile, self.drawoption, 1, self.colortable))
        self.tilel3.setPixmap(return_tile_pixmap(tile, self.drawoption, 2, self.colortable))
        self.update_preview()

    def update_preview(self):
        opacityl1 = (self.ui.rl1.value if self.drawoption > 2 else self.ui.nl1.value) / 255
        opacityl2 = (self.ui.rl2.value if self.drawoption > 2 else self.ui.nl2.value) / 255
        opacityl3 = (self.ui.rl3.value if self.drawoption > 2 else self.ui.nl3.value) / 255

        self.tilel1.setOpacity(0 if not self.ui.showl1.value else opacityl1)
        self.tilel2.setOpacity(0 if not self.ui.showl2.value else (opacityl2 if self.ui.showl1.value else opacityl1))
        self.tilel3.setOpacity(0 if not self.ui.showl3.value else (opacityl3 if self.ui.showl1.value and self.ui.showl2.value else opacityl2 if self.ui.showl1.value != self.ui.showl2.value else opacityl1))
        self.set_mapzoom()

    def set_pos(self, pos: QPointF | QPoint):
        super().set_pos(pos)
        self.set_mappos()

    def set_mappos(self):
        self.tilel1.setPos(self.topleft.pos())
        self.tilel2.setPos(self.topleft.pos() + QPoint(CELLSIZE, 0) * self.zoom)
        self.tilel3.setPos(self.topleft.pos() + QPoint(CELLSIZE * 2, 0) * self.zoom)

    def wheelEvent(self, event):
        super().wheelEvent(event)
        self.set_mapzoom()

    def set_mapzoom(self):
        self.tilel1.setScale(self.zoom * ((CELLSIZE / SPRITESIZE) if self.drawoption == 0 else 1))
        self.tilel2.setScale(self.zoom * ((CELLSIZE / SPRITESIZE) if self.drawoption == 0 else 1))
        self.tilel3.setScale(self.zoom * ((CELLSIZE / SPRITESIZE) if self.drawoption == 0 else 1))
        self.tilel2.setData(0, 100)

    def update_option(self, option):
        self.drawoption = option
        self.redraw()
