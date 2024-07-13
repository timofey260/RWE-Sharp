from __future__ import annotations
from PySide6.QtCore import Signal, QObject
from typing import TYPE_CHECKING
from core.Modify.Mod import Mod
from core.Modify.ui import SettingUI
if TYPE_CHECKING:
    from core.Modify.ui import SettingUI


class Configurable(QObject):
    valueChanged: Signal | None = None
    """
    Activated when value is changed
    """

    def __init__(self, mod: Mod | SettingUI | None, name: str, default: ..., description: str = ""):
        """
        Abstract object for creating custom config parameters and storing them
        :param config: config to link, can be None
        :param name: name of object. should not contain spaces or any special characters
        :param default: default value of variable
        :param description: description in config menu
        """
        super().__init__()
        self.name = name
        self.default = default
        self.value = default
        self.description = description
        self.mod = mod
        if isinstance(mod, Mod):
            self.link_mod(mod)
        elif isinstance(mod, SettingUI):
            self.link_setting(mod)

    def link_mod(self, mod):
        self.mod = mod
        mod.configs.append(self)
        value = mod.manager.config.values.get(f"{mod.author_name}.{self.name}")
        if value is not None:
            self.load_str_value(value)

    def load_str_value(self, text: str) -> None:
        self.valueChanged.emit(self.value)

    def save_str_value(self) -> str:
        ...

    def update_value(self, value: ...):
        if self.value == value:
            return
        self.value = value
        self.valueChanged.emit(self.value)

    def update_value_default(self, value:...):
        self.update_value(value)
        self.default = value

    def reset_value(self):
        self.update_value(self.default)

    def __call__(self, *args, **kwargs):
        return self.value

    def link_setting(self, setting: SettingUI):
        setting.settings.append(self)
        return self

    def __repr__(self):
        return f"{self.name}={self.value}"
