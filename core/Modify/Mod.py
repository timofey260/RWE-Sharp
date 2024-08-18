from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from abc import ABC
if TYPE_CHECKING:
    from core.Modify.ConfigModule import ConfigModule
    from core.Modify.ui import UI, ViewUI
    from core.Modify.EditorMode import EditorMode
    from core.Modify.baseModule import Module
    from PySide6.QtWidgets import QWidget
    from core.Modify.Theme import Theme
    from core.Manager import Manager
    from core.TreeElement import SettingElement, HotkeyElement


@dataclass(frozen=True, init=True)
class ModInfo:
    title: str
    name: str
    author: str
    version: str
    description: str = "No description provided"
    tags: list[str] = field(default_factory=list)
    requirements: list[str] = field(default_factory=list)


class Mod(ABC):

    def __init__(self, manager: Manager, modinfo: ModInfo, path=""):
        """
        Base Mod class to load
        :param manager: manager to use
        :param modinfo: mod info, should be filled with class
        :param path: path to mod
        """
        self.manager = manager
        self.modinfo = modinfo
        self.path = path
        self.configs = []

    @property
    def author_name(self) -> str:
        return f"{self.modinfo.author}.{self.modinfo.name}"

    def mod_init(self):
        """
        Called when mod is enabled
        :return:
        """

    def add_editor(self, editor: EditorMode, ui: UI):
        self.manager.add_editor(editor, ui)

    def add_module(self, module: Module):
        self.manager.add_module(module)

    def add_vis_ui(self, ui: ViewUI):
        self.manager.add_view(ui)

    def add_quickview_option(self, element: QWidget):
        self.manager.add_quick_option(element)

    def add_config_module(self, config_module: ConfigModule):
        self.manager.config.add_module(config_module)

    def add_palette(self, palette: Theme):
        self.manager.palettes.append(palette)

    def add_setting(self, setting: SettingElement):
        self.manager.add_setting(setting)

    def add_hotkey(self, hotkey: HotkeyElement):
        self.manager.add_hotkeytree(hotkey)
