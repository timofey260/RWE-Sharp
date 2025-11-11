from __future__ import annotations

import json
import os.path
from dataclasses import dataclass, field
from io import TextIOWrapper
from typing import TYPE_CHECKING
from abc import ABC
if TYPE_CHECKING:
    from RWESharp.Level.RWELevel import RWELevel
    from RWESharp.Modify.ConfigModule import ConfigModule
    from RWESharp.Modify.Ui import UI, ViewUI
    from RWESharp.Modify.Editor import Editor
    from PySide6.QtWidgets import QWidget
    from RWESharp.Core.Manager import Manager
    from RWESharp.Core.TreeElement import SettingElement, HotkeyElement
    from RWESharp.widgets import ViewPort


@dataclass(frozen=True, init=True)
class ModInfo:
    """
    ModInfo stores all information about the `Mod`
    """
    title: str
    """Mod Title"""
    id: str
    """Mod Id"""
    author: str
    """Mod Author"""
    version: str
    """Mod Version"""
    description: str = "No description provided"
    """Mod Description"""
    tags: list[str] = field(default_factory=list)
    """Mod Tags"""
    required_modules: list[str] = field(default_factory=list)
    """Mod's required Modules"""
    required_mods: list[str] = field(default_factory=list)
    """Mod's required Mods"""
    mod_class: str = "NOTFOUND"
    """Mod's class to search through in mod's script"""

    @staticmethod
    def import_from_file(file: TextIOWrapper) -> ModInfo | None:
        """Imports ModInfo from file

        :param file: Json file
        :return: ModInfo if found
        :rtype: ModInfo
        """
        try:
            d: dict = json.load(file)
        except (IOError, ValueError):
            return None
        return ModInfo(d.get("title", "UNNAMED"),
                       d["id"],
                       d.get("authors", "idk like someone"),
                       d.get("version", "0.1.0"),
                       d.get("description", "No description provided"),
                       d.get("tags", []),
                       d.get("required_modules", []),
                       d.get("required_mods", []),
                       d["mod_class"])

    @staticmethod
    def import_from_mod_path(path) -> ModInfo | None:
        """Imports file from mod's path

        :param path: Path to mod
        :return: ModInfo if found
        :rtype: ModInfo
        """
        with open(os.path.join(path, "modinfo.json")) as f:
            return ModInfo.import_from_file(f)


class Mod(ABC):
    """
    Main part that changes RWE#
    todo make this part
    """

    def __init__(self, manager: Manager, modinfo: ModInfo, path=""):
        """Base Mod class to load

        :param manager: manager to use
        :param modinfo: mod info, should be filled with class
        :param path: path to mod
        """
        self.manager = manager
        self.modinfo = modinfo
        self.path = path
        self.configs = []

    @property
    def author_id(self) -> str:
        """Returns string formatted as "author.id"

        :return: Formatted string
        :rtype: str
        """
        return f"{self.modinfo.author}.{self.modinfo.id}"

    def add_editor(self, editor: Editor, ui: UI) -> None:
        """Adds Editor to Manager, connected with ui

        :param editor: Editor to add
        :param ui: Ui connected to editor
        :return: None
        """
        self.manager.add_editor(editor, ui)

    def add_view(self, ui: ViewUI) -> None:
        """Adds View Ui to Manager

        :param ui: View ui
        :return: None
        """
        self.manager.add_view(ui)

    def add_quickview_option(self, element: QWidget) -> None:
        """Adds quick option in "Quick" tab

        :param element: Element to add
        :return: None
        """
        self.manager.add_quick_option(element)

    def add_config_module(self, config_module: ConfigModule) -> None:
        """Adds Config module to `Manager`
        
        Called by ConfigModule automatically so you don't need to use it
        
        :param config_module: 
        :return: None
        """
        self.manager.config.add_module(config_module)

    def add_setting(self, setting: SettingElement) -> None:
        """Adds setting in Preferences menu

        :param setting: Setting to add
        :return: None
        """
        self.manager.add_setting(setting)

    def add_hotkey(self, hotkey: HotkeyElement) -> None:
        """Adds HotkeyTree to Hotkeys menu
        
        :param hotkey: Tree to add
        :return: None
        """
        self.manager.add_hotkeytree(hotkey)

    def on_save(self, viewport: ViewPort) -> None:
        """Gets called before save

        :return: None
        """

    def level_opened(self, viewport: ViewPort) -> None:
        """Gets called whenever user opens level

        :param viewport: viewport the level was opened in

        :return: None
        """

    def mount_levelparts(self, level: RWELevel) -> None:
        """Used to mount all Mod's LevelParts to level

        :param level: Level to mount on
        :return: None
        """
        pass
