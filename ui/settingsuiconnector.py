from __future__ import annotations
from ui.uiscripts.settings import Ui_Settings
from PySide6.QtWidgets import QDialog, QTreeWidgetItem
from PySide6.QtCore import Qt, Slot
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Manager import Manager


class SettingsUI(QDialog):
    def __init__(self, manager: Manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        print(self.manager.settings)
        self.ui.SettingsViewer.load_ui(self.manager.settings[0])
        for i in self.manager.settings:
            self.objectName()

        wd = QTreeWidgetItem(["BaseMod", "Timofey26", "BaseMod", "basemod"])
        wd.addChild(QTreeWidgetItem(["geo", "Timofey26", "BaseMod", "basemod.geo"]))
        wd.setData(0, Qt.ItemDataRole.UserRole, 100)
        print(wd.data(0, Qt.ItemDataRole.UserRole))
        self.ui.treeWidget.addTopLevelItem(wd)
        self.ui.treeWidget.itemClicked.connect(self.change)
        print(self.ui.treeWidget.findItems("lmao", Qt.MatchFlag.MatchExactly, 2))

    @Slot(QTreeWidgetItem, int)
    def change(self, item: QTreeWidgetItem, column: int):
        for i in self.manager.settings:
            if i.reference == item.text(3):
                self.ui.SettingsViewer.load_ui(i)
                item.setData()
                return
