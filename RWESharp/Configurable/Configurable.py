from __future__ import annotations
from PySide6.QtCore import Signal, QObject
from RWESharp.Modify.Mod import Mod
from abc import abstractmethod


class Configurable(QObject):
    valueChanged: Signal | None = None
    """
    Activated when value is changed
    """

    def __init__(self, mod: Mod | None, name: str, default: ..., description: str = ""):
        """
        Abstract object for creating custom config parameters and storing them
        :param mod: mod to link configurable
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

    def link_mod(self, mod):
        self.mod = mod
        mod.configs.append(self)
        value = mod.manager.config.settings.value(f"{mod.author_id}/{self.name.replace(".", "/")}")
        if value is not None:
            self.load_str_value(value)

    def load_str_value(self, text: str) -> None:
        self.valueChanged.emit(self.value)

    @abstractmethod
    def save_str_value(self) -> str:
        pass

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

    def __repr__(self):
        return f"{self.name}={self.value}"
