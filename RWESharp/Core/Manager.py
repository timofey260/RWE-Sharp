from RWESharp.Level.RWELevel import RWELevel
from RWESharp.Modify.Editor import Editor
from RWESharp.Modify.Mod import Mod
from RWESharp.Core.Config import Config
from RWESharp.Core.TreeElement import SettingElement, HotkeyElement
from RWESharp.info import PATH_MODS
from RWESharp.Core.ModLoader import load_mod
from RWESharp.utils import log
from RWESharp.Loaders.Tile import Tiles
from RWESharp.Loaders.Prop import Props
from RWESharp.Loaders.Effect import Effects
from RWESharp.Core.Application import Application
from ui.mainuiconnector import MainWindow
from widgets.Viewport import ViewPort
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu
from PySide6.QtCore import Slot
import os


class Manager:
    """
    Manager that controls all of RWE#(except for gui)
    """
    def __init__(self, window: MainWindow, app: Application, file=None):
        """
        :param window: RWE# window(main window with viewport and stuff)
        :param app: RWE# application class
        :param file: file to load by default
        """
        splash = app.splash

        self.window: MainWindow = window
        """Main RWE#'s window"""
        self.application: Application = app
        """RWE#'s Application"""

        self.tiles: Tiles = splash.loader.tiles
        """Loaded Tiles"""
        self.props: Props = splash.loader.props
        """Loaded Props"""
        self.effects: Effects = splash.loader.effects
        """Loaded Effects"""
        self.prop_colors = splash.loader.prop_colors
        """Loaded Prop Colors"""

        # self.levelpath: str = "" if file is None else file

        # self.viewports: list[ViewPort] = []

        self._current_editor = 0
        self.editors: list[Editor] = []
        """List of loaded Editors"""

        # self.modules: list[Module] = []
        # """
        # Modules are made for viewport modifying
        # """
        self.mods: list[Mod] = []
        """List of all mods enabled"""
        self.config = Config(self)
        """Config system"""
        self.setting_trees: list[SettingElement] = []
        """Setting trees for settings"""
        self.hotkey_trees: list[HotkeyElement] = []
        """Hotkey trees for hotkeys"""

        self.mod_types: list[type] = []
        """List of loaded mod types"""
        from RWESharp.Configurable.PythonTypes import IntConfigurable
        self.layer = IntConfigurable(None, "layer", 0, "Current layer")
        """Current layer"""

        from BaseMod.baseMod import BaseMod

        self.config.init_configs(self.application.parser.isSet(self.application.args.reset))  # mounting configs and applying them
        self.basemod = BaseMod(self, "")
        """BaseMod.BaseMod"""

        self.mods.append(self.basemod)
        self.pre_init_mods()
        self.init_mods()

        v = self.open_level(RWELevel(self, file))

        self.init_editors(v)
        self.basemod.preferences.update_themes()
        log("Finished initiating")

    def open_level(self, level):
        v = ViewPort(level, self)
        self.window.add_viewport(v)
        return v

    def open_level_from_path(self, path):  # obsolete?
        if not os.path.exists(path):
            return
        self.open_level(RWELevel(self, path))

    def init_editors(self, v):
        if len(self.editors) <= 0:
            log("No editors found!!!", True)  # fucking explode idk
            return
        self.mount_editor()
        #self.editors[0].init_scene_items(self.selected_viewport)

    def init_mods(self):
        for i in self.mod_types:
            self.mods.append(i[0](self, i[1]))

    def pre_init_mods(self):
        if self.application.parser.isSet(self.application.args.nomods):
            log("Mod loading is Disabled")
            return
        # mods adding
        log("Loading mods...")
        for indx, i in enumerate(os.listdir(PATH_MODS)):
            if not os.path.isdir(os.path.join(PATH_MODS, i)):
                continue
            mod = load_mod(os.path.join(PATH_MODS, i), self, indx)
            if mod is not None:
                self.mod_types.append(mod)
        log("Mod loading finished!")


    def add_editor(self, editor, ui: QWidget):
        self.editors.append(editor)
        self.window.ui.ToolsTabs.addTab(ui, ui.objectName())
        #self.window.ui.menuEditors.addAction()
        # ui.setParent(self.window.ui.ToolsTabs)

    def add_view(self, ui: QWidget) -> None:
        self.window.ui.ViewTab.addTab(ui, ui.objectName())

    def add_quick_option(self, element: QWidget) -> None:
        self.window.ui.QuickOverlay.addWidget(element)

    def add_setting(self, setting: SettingElement):
        self.setting_trees.append(setting)

    def add_hotkeytree(self, hotkey: HotkeyElement):
        self.hotkey_trees.append(hotkey)

    def undo(self):
        self.selected_viewport.level.undo()
        self.selected_viewport.clean()

    def redo(self):
        self.selected_viewport.level.redo()
        self.selected_viewport.clean()

    @property
    def view_menu(self) -> QMenu:
        return self.window.ui.menuView

    @property
    def tool_menu(self) -> QMenu:
        return self.window.ui.menutools

    @property
    def window_menu(self) -> QMenu:
        return self.window.ui.menuWindow

    @property
    def edit_menu(self) -> QMenu:
        return self.window.ui.menuedit

    @property
    def editors_menu(self) -> QMenu:
        return self.window.ui.menuEditors

    @property
    def menu_bar(self) -> QMenuBar:
        return self.window.ui.menubar

    def set_status(self, message: str) -> None:
        # self.window.ui.viewPort.setStatusTip(message)
        self.window.statusBar().showMessage(message)

    @property
    def editor(self) -> Editor:
        return self.editors[self._current_editor]

    def change_editor_name(self, name: str):
        for i in range(self.window.ui.ToolsTabs.count()):
            if self.window.ui.ToolsTabs.tabText(i).lower() == name.lower():
                self.window.ui.ToolsTabs.setCurrentIndex(i)
                # self.change_editor(i)
                return
        log(f"Couldn't find editor {name}", True)

    def change_editor(self, value: int):
        self.selected_viewport.remove_module(self.editor)
        self._current_editor = value
        self.mount_editor()

    def mount_editor(self):
        if self.window.ui.tabWidget.count() == 0:
            return
        self.selected_viewport.remove_module(self.editor)
        self.selected_viewport.add_module(self.editor, editor=True)
        self.selected_viewport.clean()

    @property
    def level_width(self):
        return self.selected_viewport.level.level_width

    @property
    def level_height(self):
        return self.selected_viewport.level.level_height

    @Slot()
    def save_level(self):
        self.selected_viewport.save_level()
        self.config.save_configs()

    @Slot()
    def save_level_as(self):
        self.selected_viewport.save_level_as()
        self.config.save_configs()

    @property
    def selected_viewport(self) -> ViewPort:
        return self.window.ui.tabWidget.currentWidget()
