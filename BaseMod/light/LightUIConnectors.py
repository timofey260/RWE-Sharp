from RWESharp.Ui import UI, ViewUI
from BaseMod.light.ui.light_ui import Ui_Light


class LightUI(UI):
    def __init__(self, mod):
        super().__init__(mod)
        self.ui = Ui_Light()
        self.ui.setupUi(self)
