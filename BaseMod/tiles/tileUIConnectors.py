from .tiles_vis_ui import Ui_TilesView
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Qt
from ..baseMod import BaseMod


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
                self.ui.VTilesMaterialClassic,
                self.ui.VTilesMaterialHenry,
                self.ui.VTilesMaterialUnrendered,
                self.ui.VTilesMaterialRendered
            ])

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.ui.VTilesLayer1.setChecked(True)
            self.ui.VTilesLayer2.setChecked(True)
            self.ui.VTilesLayer3.setChecked(True)
            self.ui.VTilesHeads.setChecked(True)
            self.ui.VTilesMaterials.setChecked(True)