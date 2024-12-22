from __future__ import annotations
from ui.uiscripts.settings import Ui_Settings
from PySide6.QtWidgets import QDialog, QTreeWidgetItem, QDialogButtonBox
from PySide6.QtCore import Qt, Slot
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Manager import Manager


class SettingsDialogUI(QDialog):
    def __init__(self, manager: Manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.SettingsViewer.got_buttons(self)
        if parent is not None:
            self.setPalette(parent.palette())

        # self.ui.SettingsViewer.load_ui(self.manager.setting_trees[0].ui)
        for i in self.manager.setting_trees:
            self.ui.treeWidget.addTopLevelItem(i.construct_tree())

        self.ui.treeWidget.expandAll()
        self.ui.treeWidget.itemClicked.connect(self.change)

        self.apply_button = self.ui.buttonBox.button(QDialogButtonBox.StandardButton.Apply)
        self.apply_button.clicked.connect(self.manager.config.save_configs)

    @Slot(QTreeWidgetItem, int)
    def change(self, item: QTreeWidgetItem, column: int):
        data = item.data(0, Qt.ItemDataRole.UserRole)
        if data[1] is None:
            self.ui.SettingsViewer.clear_settings()
            return
        self.ui.SettingsViewer.load_ui(data[1])
