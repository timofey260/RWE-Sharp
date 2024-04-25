from PySide6.QtWidgets import QDialog
from ui.uiscripts.about import Ui_Dialog


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)