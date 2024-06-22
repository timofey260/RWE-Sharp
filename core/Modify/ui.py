from __future__ import annotations
from PySide6.QtWidgets import QWidget
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Modify.Mod import Mod
    from widgets.SettingsViewer import SettingsViewer
    from core.configTypes.ConfigBase import Configurable


class UI(QWidget):
    def __init__(self, mod: Mod, parent=None):
        super().__init__(parent)
        self.mod = mod


class ViewUI(UI):
    def add_myself(self):
        self.mod.add_vis_ui(self)
        return self


class SettingUI:
    def __init__(self, mod: Mod):
        self.mod = mod
        self.settings: list[Configurable] = []

    def init_ui(self, viewer: SettingsViewer):
        """
        Called when ui is being initiated
        :param viewer:
        :return: None
        """

    def reset_values(self):
        """
        Called when values need to be reset to the saved ones
        :return: None
        """

    def reset_values_default(self):
        """
        Called when values need to be reset to the default
        :return: None
        """

    def apply_values(self):
        """
        Called when values need to be applied
        :return: None
        """

    @property
    def is_changed(self):
        for i in self.settings:
            if i.value != i.default:
                return True
        return False
