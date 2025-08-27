from RWESharp.Ui import UI
from BaseMod.properties.ui.properties_ui import Ui_Properties

class PropertiesUI(UI):
    def __init__(self, mod):
        super().__init__(mod)
        self.ui = Ui_Properties()
        self.ui.setupUi(self)
