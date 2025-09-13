from __future__ import annotations

import json
import os.path
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from abc import ABC
if TYPE_CHECKING:
    from core.Level.RWELevel import RWELevel
    from core.Modify.ConfigModule import ConfigModule
    from core.Modify.ui import UI, ViewUI
    from core.Modify.Editor import Editor
    from PySide6.QtWidgets import QWidget
    from core.Manager import Manager
    from core.TreeElement import SettingElement, HotkeyElement
    from widgets.Viewport import ViewPort


@dataclass(frozen=True, init=True)
class ModInfo:
    title: str
    id: str
    author: str
    version: str
    description: str = "No description provided"
    tags: list[str] = field(default_factory=list)
    required_modules: list[str] = field(default_factory=list)
    required_mods: list[str] = field(default_factory=list)
    mod_class: str = "NOTFOUND"

    @staticmethod
    def import_from_file(file) -> ModInfo | None:
        d: dict = json.load(file)
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
        with open(os.path.join(path, "modinfo.json")) as f:
            return ModInfo.import_from_file(f)


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
    def author_id(self) -> str:
        return f"{self.modinfo.author}.{self.modinfo.id}"

    def add_editor(self, editor: Editor, ui: UI):
        self.manager.add_editor(editor, ui)
        ui.editor_linked(editor)

    def add_vis_ui(self, ui: ViewUI):
        self.manager.add_view(ui)

    def add_quickview_option(self, element: QWidget):
        self.manager.add_quick_option(element)

    def add_config_module(self, config_module: ConfigModule):
        self.manager.config.add_module(config_module)

    def add_setting(self, setting: SettingElement):
        self.manager.add_setting(setting)

    def add_hotkey(self, hotkey: HotkeyElement):
        self.manager.add_hotkeytree(hotkey)

    def on_save(self, viewport: ViewPort):
        """
        Gets called before save
        :return:
        """

    def level_opened(self, viewport: ViewPort):
        """
        Gets called whenever user opens level
        :param viewport: viewport the level was opened in
        :return:
        """

    def mount_levelparts(self, level: RWELevel):
        pass
