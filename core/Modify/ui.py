from __future__ import annotations
from PySide6.QtWidgets import QWidget, QAbstractButton, QAbstractSlider
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from core.info import PATH_FILES_CACHE
import os
if TYPE_CHECKING:
    from core.Modify.Mod import Mod
    from widgets.SettingsViewer import SettingsViewer
    from core.configTypes.ConfigBase import Configurable
    from core.Modify.Theme import Theme

logfile = open(os.path.join(PATH_FILES_CACHE, "log.txt"), "a+")


class UI(QWidget):
    def __init__(self, mod: Mod, parent=None):
        super().__init__(parent)
        self.mod = mod

    def begin_recording(self):
        if not self.mod.manager.application.debug:
            return
        ch: list[QWidget] = self.findChildren(QWidget)
        for i in ch:
            if isinstance(i, QAbstractButton):
                i.clicked.connect(self._answer(i, f"b {i.objectName()} pressed"))  # todo
            elif isinstance(i, QAbstractSlider):
                i.valueChanged.connect(self._answer(i, f"s {i.objectName()} changed {i.value()}"))  # todo

    def _answer(self, obj, text):
        return lambda x: print(text, file=logfile, flush=True)


class ViewUI(UI):
    def add_myself(self):
        self.mod.add_vis_ui(self)
        self.begin_recording()
        return self


class SettingUI(ABC):
    def __init__(self, mod: Mod):
        self.mod = mod
        self.settings: list[Configurable] = []

    @abstractmethod
    def init_ui(self, viewer: SettingsViewer):
        """
        Called when ui is being initiated
        :param viewer:
        :return: None
        """

    @abstractmethod
    def reset_values(self):
        """
        Called when values need to be reset to the saved ones
        :return: None
        """

    @abstractmethod
    def reset_values_default(self):
        """
        Called when values need to be reset to the default
        :return: None
        """

    @abstractmethod
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


class ThemeUI(UI):
    def __init__(self, theme: Theme, parent=None):
        super().__init__(theme.mod, parent)
        self.theme = theme
        self.mod = theme.mod

    @abstractmethod
    def setup_ui(self, viewer):
        pass