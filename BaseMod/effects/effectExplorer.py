from RWESharp.Core import ViewDockWidget
from BaseMod.effects.ui.effectexplorer_ui import Ui_EffectExplorer


class EffectExplorer(ViewDockWidget):
    def __init__(self, mod, parent=None):
        super().__init__(parent)
        self.mod = mod
        self.ui = Ui_EffectExplorer()
        self.ui.setupUi(self)
