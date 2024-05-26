from .tiles_vis_ui import Ui_TilesView
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Slot, Qt
from ..baseMod import BaseMod
from core.info import PATH_FILES_IMAGES_PALETTES


class TileViewUI(QWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod: BaseMod = mod
        self.ui = Ui_TilesView()
        self.ui.setupUi(self)

        self.mod.tileviewconfig.drawl1.connect_checkbox(self.ui.VTilesLayer1)
        self.mod.tileviewconfig.drawl2.connect_checkbox(self.ui.VTilesLayer2)
        self.mod.tileviewconfig.drawl3.connect_checkbox(self.ui.VTilesLayer3)
        self.ui.VTilesAllTiles.checkStateChanged.connect(self.all_layers)
        self.mod.tileviewconfig.drawoption.connect_radio(
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