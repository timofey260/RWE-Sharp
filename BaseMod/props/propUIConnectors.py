from RWESharp.Ui import UI
from RWESharp.Configurable import KeyConfigurable
from BaseMod.props.ui.props_ui import Ui_Props

from PySide6.QtWidgets import QTreeWidgetItem


class PropsUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.editor = mod.propeditor
        self.editor.propsui = self
        self.ui = Ui_Props()
        self.ui.setupUi(self)
        self.ui.Notes.setText("\n".join(self.editor.prop.notes))

        self.free_transform = KeyConfigurable(mod, "EDIT_props.free_transform", "f", "Free transform")
        self.reset_transform = KeyConfigurable(mod, "EDIT_props.reset_transform", "r", "Reset transform")
        self.explorer_key = KeyConfigurable(mod, "EDIT_props.explorer", "Ctrl+e", "Open Prop Explorer")

        self.explorer_key.link_button(self.ui.Explorer)

        self.free_transform.link_button(self.ui.FreeTransform)
        self.ui.FreeTransform.clicked.connect(self.editor.free_transform)
        self.free_transform.link_button(self.ui.ResetTransform)
        self.ui.ResetTransform.clicked.connect(self.editor.reset_transform)
        self.ui.Explorer.clicked.connect(self.open_explorer)
        self.ui.PropOptions.setColumnCount(2)
        self.display_settings()

    def display_settings(self):
        self.ui.PropOptions.clear()
        for k, v in self.editor.prop_settings.items():
            self.ui.PropOptions.addTopLevelItem(QTreeWidgetItem([k, str(v)]))

        self.ui.Notes.setText("\n".join(self.editor.prop.notes))

    def open_explorer(self):
        self.editor.explorer.change_visibility(True)
