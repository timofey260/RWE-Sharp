from ui.uiscripts.settings import Ui_Settings
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem


class SettingsModel(QStandardItemModel):
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """Returns the appropriate header string depending on the orientation of
           the header and the section. If anything other than the display role is
           requested, we return an invalid variant."""
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ["Setting", "Author"][section]
        return None


class SettingsUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.itemmodel = SettingsModel()
        main = QStandardItem("RWE#")
        main.appendRow(QStandardItem("Viewport"))
        self.itemmodel.appendRow([main, QStandardItem("timofey26")])
        self.itemmodel.appendRow([QStandardItem("BaseMod"), QStandardItem("timofey26")])

        self.ui.settingsTree.setModel(self.itemmodel)
        self.ui.settingsTree.doubleClicked.connect(self.change)
        # self.ui.settingsTree.setcol

    @Slot()
    def change(self):
        print("click")