from RWESharp.Ui import UI
from BaseMod.props.ui.props_ui import Ui_Props


class PropsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.editor = mod.propeditor
        self.ui = Ui_Props()
        self.ui.setupUi(self)
        self.ui.Notes.setText("\n".join(self.editor.prop.notes))
