from RWESharp.Ui import UI
from BaseMod.effects.ui.effects_ui import Ui_Effects


class EffectsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_Effects()
        self.ui.setupUi(self)
