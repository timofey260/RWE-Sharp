from BaseMod.tiles.ui.tilepin import Ui_TilePin
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import ViewDockWidget, CELLSIZE, SPRITESIZE
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPixmap


class TilePin(ViewDockWidget):
    def __init__(self, tile, explorer, parent=None):
        super().__init__(parent)
        self.ui = Ui_TilePin()
        self.ui.setupUi(self)
        self.tile = tile
        parent.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self)
        self.explorer = explorer
        self.layer = IntConfigurable(None, "layer", 1, "layer of tiles")
        self.drawoption = IntConfigurable(None, "option", explorer.synced_draw_option, "Drawing option")
        self.layer.link_spinbox(self.ui.Layer)
        self.drawoption.link_combobox(self.ui.RenderOption)
        self.layer.valueChanged.connect(self.change_preview)
        self.drawoption.valueChanged.connect(self.change_preview)
        self.setWindowTitle(self.tile.name)
        self.ui.Collisions.setChecked(explorer.tile_cols.value)
        self.ui.Collisions.toggled.connect(self.change_preview)
        self.ui.Select.clicked.connect(self.select_tile)
        self.preview = self.ui.Preview

        self.setFloating(True)
        self.tileimage = self.preview.workscene.addPixmap(QPixmap(1, 1))
        self.tilecolsimage = self.preview.workscene.addPixmap(QPixmap(1, 1))
        self.preview.items.append(self.tileimage)
        self.preview.items.append(self.tilecolsimage)
        self.change_preview()

    def closeEvent(self, event):
        super().closeEvent(event)
        self.explorer.remove_pin(self)

    def select_tile(self):
        self.explorer.mod.tileeditor.add_tile([self.tile])

    def change_preview(self):
        #self.ui.Preview.preview_tile(self.tile, self.drawoption.value, self.layer.value - 1, self.explorer.colortable)
        #self.ui.Preview.tilecolsimage.setOpacity(self.ui.Collisions.isChecked())

        self.tileimage.setOpacity(1)
        self.tilecolsimage.setOpacity(self.ui.Collisions.isChecked())
        self.tileimage.setPixmap(self.tile.return_tile_pixmap(self.drawoption.value, self.layer.value - 1, self.explorer.colortable))
        self.tilecolsimage.setPixmap(self.tile.collisions_image())
        self.tileimage.setData(2, (CELLSIZE / SPRITESIZE) if self.drawoption.value == 0 else 1)

        self.tileimage.setData(1, QPoint(0, 0) if self.drawoption.value == 0 else (-QPoint(self.tile.bfTiles, self.tile.bfTiles) * CELLSIZE))
        self.preview.set_zoom()
        self.preview.set_pos()
