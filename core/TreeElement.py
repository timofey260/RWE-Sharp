from __future__ import annotations
from core.Modify.ui import SettingUI
from core.configTypes.QtTypes import KeyConfigurable
from PySide6.QtWidgets import QTreeWidgetItem
from PySide6.QtCore import Qt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Modify.Mod import Mod


class TreeElement:
    def __init__(self, mod: Mod, text: str, name: str, parent=None, children: list[TreeElement] = None):
        self.mod: Mod = mod
        self.text: str = text
        self.name: str = name
        self.children: list[TreeElement] = []
        self.parent: TreeElement | None = parent
        if children is not None:
            self.add_children(*children)

    def add_children(self, *children: TreeElement):
        for i in children:
            self.add_child(i)

    def add_child(self, child: TreeElement):
        child.parent = self
        self.children.append(child)

    def find_child(self, name: str, recursive=False) -> TreeElement | None:
        for i in self.children:
            if name == i.name:
                return i
            if recursive:
                return i.find_child(name, True)
        return None

    def construct_tree(self) -> QTreeWidgetItem:
        me = QTreeWidgetItem([self.text])
        me.setData(0, Qt.ItemDataRole.UserRole, self.store_data)
        for i in self.children:
            me.addChild(i.construct_tree())
        return me

    @property
    def store_data(self):
        return [self.name]


class SettingElement(TreeElement):
    def __init__(self, mod: Mod, text: str, name: str, ui: SettingUI = None, parent=None, children: list[SettingElement] = None):
        super().__init__(mod, text, name, parent, children)
        self.ui: SettingUI = ui

    def add_myself(self):
        self.mod.add_setting(self)

    @property
    def store_data(self):
        return [self.name, self.ui]


class HotkeyElement(TreeElement):
    def __init__(self, mod: Mod, text: str, name: str, key: KeyConfigurable = None, parent=None, children: list[HotkeyElement] = None):
        super().__init__(mod, text, name, parent, children)
        self.key: KeyConfigurable = key

    def add_myself(self):
        self.mod.add_hotkey(self)

    @property
    def store_data(self):
        return [self.name, self.key]
