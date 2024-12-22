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

    def editor_linked(self, editor):
        pass

    @property
    def basemod(self):
        return self.mod.manager.basemod

    @property
    def selected_viewport(self):
        return self.mod.manager.selected_viewport

    @property
    def level(self):
        return self.mod.manager.selected_viewport.level

    @property
    def level_loaded(self):
        return self.mod.manager.selected_viewport is not None


class ViewUI(UI):
    def add_myself(self):
        self.mod.add_vis_ui(self)
        self.begin_recording()
        return self


class SettingUI(ABC):
    def __init__(self, mod: Mod):
        self.mod = mod
        self.settings: list[SettingUI.ManageableSetting] = []

    @abstractmethod
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
        for i in self.settings:
            i.source2setting()

    def reset_values_default(self):
        """
        Called when values need to be reset to the default
        :return: None
        """
        for i in self.settings:
            i.reset_values_default()

    def apply_values(self):
        """
        Called when values need to be applied
        :return: None
        """
        for i in self.settings:
            i.setting2source()

    @property
    def is_changed(self):
        for i in self.settings:
            if i.setting.value != i.setting.default:
                return True
        return False

    @property
    def basemod(self):
        return self.mod.manager.basemod

    class ManageableSetting:
        def __init__(self, setting: Configurable | None = None, source: Configurable | None = None, source2setting=lambda x: x, setting2source=lambda x: x):
            self.setting = setting
            self.source = source
            self.source2settingfunc = source2setting
            self.setting2sourcefunc = setting2source

        def source2setting(self):
            if self.setting is None:
                return
            if self.source is None:
                self.setting.update_value_default(self.source2settingfunc(None))
                return
            self.setting.update_value_default(self.source2settingfunc(self.source.value))

        def setting2source(self):
            if self.source is None:
                return
            if self.setting is None:
                self.source.update_value(self.setting2sourcefunc(None))
                return
            self.source.update_value(self.setting2sourcefunc(self.setting.value))

        def reset_values_default(self):
            if self.setting is None:
                return
            if self.source is None:
                self.setting.update_value_default(self.source2settingfunc(None))
                return
            self.setting.update_value(self.source2settingfunc(self.source.default))

        def add_myself(self, settingui: SettingUI):
            settingui.settings.append(self)
            return self

        @property
        def value(self):
            return self.setting.value


class ThemeUI(UI):
    def __init__(self, theme: Theme, parent=None):
        super().__init__(theme.mod, parent)
        self.theme = theme
        self.mod = theme.mod

    @abstractmethod
    def setup_ui(self, viewer):
        pass