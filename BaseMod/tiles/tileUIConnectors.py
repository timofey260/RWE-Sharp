from .tiles_vis_ui import Ui_TilesView
from PySide6.QtWidgets import QWidget, QFileDialog, QMenu
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QAction
from ..baseMod import BaseMod
from core.info import PATH_FILES_IMAGES_PALETTES


class TileViewUI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod: BaseMod = mod
        self.ui = Ui_TilesView()
        self.ui.setupUi(self)

        self.menu = QMenu("Tiles")

        self.menu_drawl1 = QAction("Layer 1")
        self.mod.tileviewconfig.drawl1.link_button_action(self.ui.VTilesLayer1, self.menu_drawl1, self.mod.tileviewconfig.drawl1_key)
        self.menu.addAction(self.menu_drawl1)
        self.menu_drawl2 = QAction("Layer 2")
        self.mod.tileviewconfig.drawl2.link_button_action(self.ui.VTilesLayer2, self.menu_drawl2, self.mod.tileviewconfig.drawl2_key)
        self.menu.addAction(self.menu_drawl2)
        self.menu_drawl3 = QAction("Layer 3")
        self.mod.tileviewconfig.drawl3.link_button_action(self.ui.VTilesLayer3, self.menu_drawl3, self.mod.tileviewconfig.drawl3_key)
        self.menu.addAction(self.menu_drawl3)
        self.ui.VTilesAllTiles.checkStateChanged.connect(self.all_layers)
        self.mod.manager.view_menu.addMenu(self.menu)
        self.mod.tileviewconfig.drawoption.link_radio(
            [
                self.ui.VTilesClassic,
                self.ui.VTilesImage,
                self.ui.VTilesHenry,
                self.ui.VTilesUnrendered,
                self.ui.VTilesRendered,
                self.ui.VTilesRendered_shade,
                self.ui.VTilesRendered_rain
            ])
        self.ui.PaletteSelectButton.clicked.connect(self.change_palette)

    @Slot()
    def change_palette(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a Palette", PATH_FILES_IMAGES_PALETTES)
        print(file)
        self.mod.tileviewconfig.palettepath.update_value(file)
        self.mod.tileviewconfig.drawoption.update_value(4)

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.ui.VTilesLayer1.setChecked(True)
            self.ui.VTilesLayer2.setChecked(True)
            self.ui.VTilesLayer3.setChecked(True)
            self.ui.VTilesHeads.setChecked(True)
            self.ui.VTilesMaterials.setChecked(True)

    @Slot(Qt.CheckState)
    def toggle_tiles(self, state: Qt.CheckState):
        v = state == Qt.CheckState.Checked
        self.mod.tileviewconfig.drawl1.update_value(v)
        self.mod.tileviewconfig.drawl2.update_value(v)
        self.mod.tileviewconfig.drawl3.update_value(v)