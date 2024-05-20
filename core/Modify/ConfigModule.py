from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Slot, Signal

class ConfigObject:
    def __init__(self, path, object, default):
        self.path = path
        self.object = object
        self.default = default
        self.value = default

    def load_value(self):
        ...

    def save_value(self):
        ...


class ConfigModule:
    """
    Base for creating custom mod configs
    all data we store is either level related or editor related
    config module provides easy way to store editor specific data
    """
    def __init__(self, mod):
        self.mod = mod
        self.manager = mod.manager
        self.values: dict[str, ConfigObject] = {}

    def register_value(self, path, value) -> None:
        """
        registers value to be saved
        """

    def register_widgets(self):
        ...

    def register_checkbox(self, path, object: QCheckBox, default):
        self.values[path] = ConfigObject(path, object, default)
        object.stateChanged.connect()
