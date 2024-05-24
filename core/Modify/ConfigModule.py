from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Slot, Signal
from core.configTypes.ConfigBase import Configurable


class ConfigModule:
    """
    Base for creating custom mod configs
    all data we store is either level related or editor related
    config module provides easy way to store editor specific data between rwe# sessions
    """
    def __init__(self, mod, subeditor=""):
        self.mod = mod
        self.manager = mod.manager
        self.values: dict[str, Configurable] = {}
        self.subeditor = subeditor

    def register_config(self):
        """
        Registering custom config
        Made to be overridden
        :return: None
        """

    def add_config(self, configObj: Configurable):
        self.values[configObj.name] = configObj

