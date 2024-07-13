from __future__ import annotations
from PySide6.QtWidgets import QDialog, QTreeWidgetItem
from PySide6.QtCore import Slot, Qt
from ui.uiscripts.hotkeys import Ui_Hotkeys
from ui.KeyDialog import KeyDialog
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Manager import Manager


class HotkeysUI(QDialog):
    def __init__(self, manager: Manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_Hotkeys()
        self.ui.setupUi(self)
        for i in self.manager.hotkey_trees:
            self.ui.treeWidget.addTopLevelItem(i.construct_tree())
        self.ui.treeWidget.itemDoubleClicked.connect(self.change)
        self.dialog: KeyDialog | None = None
        self.ui.treeWidget.expandAll()
        self.ui.treeWidget.resizeColumnToContents(0)
        self.ui.treeWidget.collapseAll()
        self.ui.treeWidget.setAlternatingRowColors(True)

    @Slot(QTreeWidgetItem, int)
    def change(self, item: QTreeWidgetItem, column: int):
        # opening thing
        data = item.data(0, Qt.ItemDataRole.UserRole)
        if len(data) <= 1:
            return
        if column != 1:
            return
        if self.dialog is not None:
            self.dialog.close()
            self.dialog = None
        self.dialog = KeyDialog(data[1], item, self)
        self.dialog.show()
