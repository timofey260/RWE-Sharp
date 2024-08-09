from BaseMod.tiles.ui.tilepin import Ui_TilePin
from widgets.ViewDockWidget import ViewDockWidget
from RWESharp.Configurable import IntConfigurable
from PySide6.QtCore import Qt


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
        self.change_preview()

        self.setFloating(True)

    def hideEvent(self, event):
        super().hideEvent(event)
        self.explorer.remove_pin(self)

    def select_tile(self):
        self.explorer.mod.tileeditor.add_tile([self.tile])

    def change_preview(self):
        self.ui.Preview.preview_tile(self.tile, self.drawoption.value, self.layer.value - 1, self.explorer.colortable)
        self.ui.Preview.tilecolsimage.setOpacity(self.ui.Collisions.isChecked())
