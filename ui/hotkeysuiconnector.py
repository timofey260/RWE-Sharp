from PySide6.QtWidgets import QDialog
from ui.uiscripts.hotkeys import Ui_Hotkeys


class HotkeysUI(QDialog):
    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_Hotkeys()
        self.ui.setupUi(self)
        self.ui.keySequenceEdit.keySequence()
