from RWESharp.Ui import UI
from RWESharp.Configurable import KeyConfigurable
from BaseMod.props.ui.props_ui import Ui_Props


class PropsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.editor = mod.propeditor
        self.ui = Ui_Props()
        self.ui.setupUi(self)
        self.ui.Notes.setText("\n".join(self.editor.prop.notes))

        self.free_transform = KeyConfigurable(mod, "EDIT_props.free_transform", "f", "Free transform")

        self.free_transform.link_button(self.ui.FreeTransform)
        self.ui.FreeTransform.clicked.connect(self.editor.free_transform)
