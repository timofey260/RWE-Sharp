from PySide6.QtWidgets import QWidget
from ui.uiscripts.PenPicker import Ui_Penpicker


class PenPicker(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Penpicker()
        self.ui.setupUi(self)
        # todo