from ui.uiscripts.settings import Ui_Settings
from PySide6.QtWidgets import QDialog, QTreeWidgetItem
from PySide6.QtCore import Qt, Slot


class SettingsUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        wd = QTreeWidgetItem(["ye"])
        wd.addChild(QTreeWidgetItem(wd, ["ye"]))
        self.ui.treeWidget.addTopLevelItem(wd)
        self.ui.treeWidget.itemClicked.connect(self.change)
        # self.ui.treeWidget.setModel()

    @Slot(QTreeWidgetItem, int)
    def change(self, item: QTreeWidgetItem, column: int):
        print("click")
        print(QTreeWidgetItem)
        item.setText(0, "yo mama")
