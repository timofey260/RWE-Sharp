from __future__ import annotations
from PySide6.QtWidgets import QDialog, QTreeWidgetItem
from PySide6.QtCore import Slot, Qt
from ui.uiscripts.hotkeys import Ui_Hotkeys
from ui.KeyDialog import KeyDialog
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from RWESharp.Core.Manager import Manager


class HotkeysUI(QDialog):
    def __init__(self, manager: Manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_Hotkeys()
        self.ui.setupUi(self)
        self.loaditems()
        self.ui.treeWidget.itemDoubleClicked.connect(self.change)
        self.dialog: KeyDialog | None = None
        self.ui.treeWidget.expandAll()
        self.ui.treeWidget.resizeColumnToContents(0)
        self.ui.treeWidget.collapseAll()
        self.ui.treeWidget.setAlternatingRowColors(True)
        self.ui.Search.textChanged.connect(self.update_filters)
        self.found = []
        self.ui.spinBox.valueChanged.connect(self.spinfounditems)
        self.ui.spinBox.hide()

    def spinfounditems(self):
        if len(self.found) == 0:
            return
        self.ui.treeWidget.setCurrentItem(self.found[self.ui.spinBox.value() - 1])

    def loaditems(self):
        for i in self.manager.hotkey_trees:
            self.ui.treeWidget.addTopLevelItem(i.construct_tree())

    def update_filters(self, text: str):
        # self.loaditems()
        # self.ui.treeWidget.clearSelection()
        # self.ui.treeWidget.collapseAll()
        if text == "":
            self.ui.spinBox.hide()
            return
        self.found = [*self.ui.treeWidget.findItems(text, Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchRecursive, 1),
                      *self.ui.treeWidget.findItems(text, Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchRecursive, 0)]
        # self.found = [i for i in self.found if len(i.data(0, Qt.ItemDataRole.UserRole)) > 1]
        self.ui.spinBox.setMinimum(1)
        self.ui.spinBox.setMaximum(len(self.found))
        self.ui.spinBox.setSuffix(f"/{len(self.found)}")
        self.ui.spinBox.setVisible(len(self.found) > 0)
        self.spinfounditems()

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
        self.dialog.exec()

