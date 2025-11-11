from __future__ import annotations
from PySide6.QtWidgets import QWidget, QAbstractButton, QAbstractSlider
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from RWESharp.info import PATH_FILES_CACHE
import os
if TYPE_CHECKING:
    from BaseMod.baseMod import BaseMod
    from RWESharp.widgets.SettingsViewer import SettingsViewer
    from RWESharp.widgets.Viewport import ViewPort
    from RWESharp.Configurable.Configurable import Configurable
    from RWESharp.Modify.Mod import Mod
    from RWESharp.Modify.Theme import Theme
    from RWESharp.Level.RWELevel import RWELevel

logfile = open(os.path.join(PATH_FILES_CACHE, "log.txt"), "a+")


class UI(QWidget):
    """
    UI base for creating Editor UI's
    todo add more
    """
    def __init__(self, mod: Mod, parent=None):
        super().__init__(parent)
        self.mod = mod

    def begin_recording(self) -> None:
        """Records all of your actions if Debug mode is set
        
        :return: None
        """
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

    def editor_linked(self, editor) -> None:
        """Gets called whenever Editor with this UI is being added
        
        :param editor: Editor that was added
        :return: None
        """

    @property
    def basemod(self) -> BaseMod:
        return self.mod.manager.basemod

    @property
    def selected_viewport(self) -> ViewPort:
        return self.mod.manager.selected_viewport

    @property
    def level(self) -> RWELevel:
        return self.mod.manager.selected_viewport.level

    @property
    def level_loaded(self) -> bool:
        """Returns if level was loaded
        
        :return: if viewport is available
        :rtype: bool
        """
        return self.mod.manager.selected_viewport is not None


class ViewUI(UI):
    """
    Addition to `UI` that allows to create View tabs
    todo add more
    """
    def add_myself(self) -> ViewUI:
        """Adds `ViewUI` to View tab
        
        :return: self
        :rtype: ViewUI
        """
        self.mod.add_view(self)
        self.begin_recording()
        return self


class SettingUI(ABC):
    """
    SettingUI is UI for Preferences menu
    todo add more
    """
    def __init__(self, mod: Mod):
        self.mod = mod
        self.settings: list[SettingUI.ManageableSetting] = []

    @abstractmethod
    def init_ui(self, viewer: SettingsViewer) -> None:
        """Called when ui is being initiated
        
        :param viewer: SettingsViewer
        :return: None
        """

    def reset_values(self):
        """Called when values need to be reset to the saved ones
        
        :return: None
        """
        for i in self.settings:
            i.source2setting()
            i.apply_setting()

    def reset_values_default(self):
        """Called when values need to be reset to default
        
        :return: None
        """
        for i in self.settings:
            i.reset_values_default()

    def apply_values(self):
        """Called when values need to be applied
        
        :return: None
        """
        for i in self.settings:
            i.setting2source()
            i.apply_setting()

    @property
    def is_changed(self):
        """Returns whenever settings values were changed
        
        :return: If settings were changed
        :rtype: bool
        """
        for i in self.settings:
            if i.setting.value != i.setting.default:
                return True
        return False

    @property
    def basemod(self) -> BaseMod:
        return self.mod.manager.basemod

    class ManageableSetting:
        """
        todo this
        """
        def __init__(self, setting: Configurable | None = None, source: Configurable | None = None, source2setting=lambda x: x, setting2source=lambda x: x):
            self.setting = setting
            self.source = source
            self.source2settingfunc = source2setting
            self.setting2sourcefunc = setting2source

        def source2setting(self) -> None:
            """Updated default value of source `Configurable` to settings `Configurable` 
            
            :return: None
            """
            if self.setting is None:
                return
            if self.source is None:
                self.setting.update_value_default(self.source2settingfunc(None))
                return
            self.setting.update_value_default(self.source2settingfunc(self.source.value))

        def setting2source(self) -> None:
            """Updated default value of setting `Configurable` to sources `Configurable`
            
            :return: None
            """
            if self.source is None:
                return
            if self.setting is None:
                self.source.update_value(self.setting2sourcefunc(None))
                return
            self.source.update_value(self.setting2sourcefunc(self.setting.value))

        def reset_values_default(self) -> None:
            """Reset settings value

            :return: None
            """
            if self.setting is None:
                return
            if self.source is None:
                self.setting.update_value_default(self.source2settingfunc(None))
                return
            self.setting.update_value(self.source2settingfunc(self.source.default))

        def apply_setting(self) -> None:
            """Applies new settings value as settings default

            :return: None
            """
            if self.setting is not None:
                self.setting.update_value_default(self.setting.value)

        def add_myself(self, settingui: SettingUI) -> SettingUI.ManageableSetting:
            """Adds itself onto Settings Ui

            :param settingui: Ui to add to
            :return: self
            :rtype: SettingUI.ManageableSetting
            """
            settingui.settings.append(self)
            return self

        @property
        def value(self):
            """Settings value

            :return: Value
            """
            return self.setting.value


class ThemeUI(UI):
    """
    Ui for custom Themes
    todo add more
    """
    def __init__(self, theme: Theme, parent=None):
        super().__init__(theme.mod, parent)
        self.theme = theme
        self.mod = theme.mod

    @abstractmethod
    def setup_ui(self, viewer):
        pass