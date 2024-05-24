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

        self.ui.VTilesLayer1.checkStateChanged.connect(self.mod.tilemodule.check_l1_change)
        self.ui.VTilesLayer2.checkStateChanged.connect(self.mod.tilemodule.check_l2_change)
        self.ui.VTilesLayer3.checkStateChanged.connect(self.mod.tilemodule.check_l3_change)
        self.ui.VTilesAllTiles.checkStateChanged.connect(self.all_layers)

    @Slot(Qt.CheckState)
    def all_layers(self, state: Qt.CheckState):
        if state == Qt.CheckState.Checked:
            self.ui.VTilesLayer1.setChecked(True)
            self.ui.VTilesLayer2.setChecked(True)
            self.ui.VTilesLayer3.setChecked(True)
            self.ui.VTilesHeads.setChecked(True)
            self.ui.VTilesMaterials.setChecked(True)