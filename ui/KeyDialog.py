from PySide6.QtWidgets import QDialog, QDialogButtonBox, QTreeWidgetItem
from ui.uiscripts.keydialog import Ui_keyDialog
from RWESharp.Configurable.QtTypes import KeyConfigurable


class KeyDialog(QDialog):
    def __init__(self, key: KeyConfigurable, settingkey: QTreeWidgetItem | None = None, parent=None):
        super().__init__(parent)
        self.key = key
        self.settingkey = settingkey
        self.tempkey = KeyConfigurable(None, "Temp", key.value, "default value")
        self.ui = Ui_keyDialog()
        self.ui.setupUi(self)
        self.tempkey.link_keysequenceedit(self.ui.keySequenceEdit)
        self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Ok).clicked.connect(self.ok)

    def accept(self):
        super().accept()

    def ok(self):
        self.key.update_value(self.tempkey.value)
        if self.settingkey is not None:
            self.settingkey.setText(1, self.key.value.toString())
