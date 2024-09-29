from RWESharp.Ui import UI
from BaseMod.props.ui.props_ui import Ui_Props


class PropsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_Props()
        self.ui.setupUi(self)
