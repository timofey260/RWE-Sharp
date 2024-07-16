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
        if parent is not None:
            self.parent.add_child(self)

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
        self.set_data(me)
        for i in self.children:
            me.addChild(i.construct_tree())
        return me

    def set_data(self, item):
        item.setData(0, Qt.ItemDataRole.UserRole, [self.name])


class SettingElement(TreeElement):
    def __init__(self, mod: Mod, text: str, name: str, ui: SettingUI = None, parent=None, children: list[SettingElement] = None):
        super().__init__(mod, text, name, parent, children)
        self.ui: SettingUI = ui

    def add_myself(self):
        self.mod.add_setting(self)
        return self

    def set_data(self, item):
        item.setData(0, Qt.ItemDataRole.UserRole, [self.name, self.ui])


class HotkeyElement(TreeElement):
    def __init__(self, mod: Mod, text: str, name: str, key: KeyConfigurable | None = None, parent=None, children: list[HotkeyElement] = None):
        super().__init__(mod, text, name, parent, children)
        self.key: KeyConfigurable | None = key

    def add_myself(self):
        self.mod.add_hotkey(self)
        return self

    def set_data(self, item):
        if self.key is None:
            item.setData(0, Qt.ItemDataRole.UserRole, [self.name])
            return
        item.setData(0, Qt.ItemDataRole.UserRole, [self.name, self.key])
        item.setText(1, self.key.value.toString())

    def add_children_configurables(self, *keys: KeyConfigurable):
        for i in keys:
            HotkeyElement(self.mod, i.shortdesc, i.name, i, self)


def get_hotkeys_from_pattern(mod: Mod, pattern: str) -> list[KeyConfigurable]:
    keys = []
    for i in mod.configs:
        if isinstance(i, KeyConfigurable) and pattern in i.name:
            keys.append(i)
    return keys
