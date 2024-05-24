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
        self.ui.VTilesLayer1.checkStateChanged.connect(self.mod.tilemodule.check_l2_change)
        self.ui.VTilesLayer1.checkStateChanged.connect(self.mod.tilemodule.check_l3_change)