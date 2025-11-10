from PySide6.QtCore import QPointF, QPoint

from RWESharp.widgets.SimpleViewport import SimpleViewport
from RWS.Core import CELLSIZE, SPRITESIZE
from PySide6.QtGui import QPixmap


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
        self.colortable = self.manager.basemod.tileview.colortable
        tile = self.manager.tiles["Four Holes"]
        self.tilel1.setPixmap(tile.return_tile_pixmap(self.drawoption, 0, self.colortable))
        self.tilel2.setPixmap(tile.return_tile_pixmap(self.drawoption, 1, self.colortable))
        self.tilel3.setPixmap(tile.return_tile_pixmap(self.drawoption, 2, self.colortable))
        self.update_preview()

    @property
    def current_layer(self):
        return self.ui.ui.LayerSlider.value()

    def update_preview(self):
        if self.drawoption > 2:
            self.tilel1.setOpacity((self.rp if self.current_layer == 0 else self.rs) / 255)
            self.tilel2.setOpacity((self.rp if self.current_layer == 1 else self.rs) / 255)
            self.tilel3.setOpacity((self.rp if self.current_layer == 2 else self.rs) / 255)
            return
        self.tilel1.setOpacity((self.np if self.current_layer == 0 else self.ns) / 255)
        if self.current_layer == 1 and not self.ui.renderall.value:
            self.tilel1.setOpacity(0)
        self.tilel2.setOpacity((self.np if self.current_layer == 1 else self.ns) / 255)
        if self.current_layer == 2 and not self.ui.renderall.value:
            self.tilel1.setOpacity(0)
            self.tilel2.setOpacity(0)
        self.tilel3.setOpacity((self.np if self.current_layer == 2 else self.ns) / 255)
        self.set_mapzoom()

    @property
    def rp(self):
        return self.ui.rp.value if self.ui.ui.Pshow.isChecked() else 0

    @property
    def np(self):
        return self.ui.np.value if self.ui.ui.Pshow.isChecked() else 0

    @property
    def rs(self):
        return self.ui.rs.value if self.ui.ui.Sshow.isChecked() else 0

    @property
    def ns(self):
        return self.ui.ns.value if self.ui.ui.Sshow.isChecked() else 0

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
