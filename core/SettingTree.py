from __future__ import annotations
from core.Modify.ui import SettingUI
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Modify.Mod import Mod


class SettingElement:
    def __init__(self, mod: Mod, text: str, name: str, ui: SettingUI = None, parent=None, children: list[SettingUI] = None):
        self.mod: Mod = mod
        self.text: str = text
        self.name: str = name
        self.ui: SettingUI | None = ui
        self.children: list[SettingElement] = []
        self.parent: SettingElement | None = parent
        if children is not None:
            self.add_children(*children)

    def add_children(self, *children: SettingElement):
        for i in children:
            self.add_child(i)

    def add_child(self, child: SettingElement):
        child.parent = self
        self.children.append(child)

    def add_myself(self):
        self.mod.add_setting(self)
        return self

    def find_child(self, id, recursive=False) -> SettingElement | None:
        for i in self.children:
            if id == i.name:
                return i
            if recursive:
                return i.find_child(id, True)
        return None

    def construct_tree(self) -> QTreeWidgetItem:
        me = QTreeWidgetItem([self.text])
        me.setData(0, Qt.ItemDataRole.UserRole, [self.name, self.ui])
        for i in self.children:
            me.addChild(i.construct_tree())
        return me
