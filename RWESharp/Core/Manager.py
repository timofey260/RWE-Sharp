from RWESharp.Level.RWELevel import RWELevel
from RWESharp.Modify.Editor import Editor
from RWESharp.Modify.Mod import Mod
from RWESharp.Core.Config import Config
from RWESharp.Core.TreeElement import SettingElement, HotkeyElement
from RWESharp.Modify.Ui import UI, ViewUI
from RWESharp.info import PATH_MODS
from RWESharp.Core.ModLoader import load_mod
from RWESharp.utils import log
from RWESharp.Loaders.Tile import Tiles
from RWESharp.Loaders.Prop import Props
from RWESharp.Loaders.Effect import Effects
from RWESharp.Core.Application import Application
from RWESharp.ui.mainuiconnector import MainWindow
from RWESharp.widgets.Viewport import ViewPort
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu
from PySide6.QtCore import Slot
import os


class Manager:
    """
    Manager that controls Behavior of RWE#
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
        self.prop_colors: list[list] = splash.loader.prop_colors
        """Loaded Prop Colors"""

        # self.levelpath: str = "" if file is None else file

        # self.viewports: list[ViewPort] = []

        self._current_editor: int = 0
        self.editors: list[Editor] = []
        """List of loaded Editors"""

        # self.modules: list[Module] = []
        # """
        # Modules are made for viewport modifying
        # """
        self.mods: list[Mod] = []
        """List of all mods enabled"""
        self.config: Config = Config(self)
        """Config system"""
        self.setting_trees: list[SettingElement] = []
        """Setting trees for settings"""
        self.hotkey_trees: list[HotkeyElement] = []
        """Hotkey trees for hotkeys"""

        self.mod_types: list[type] = []
        """List of loaded mod types"""
        from RWESharp.Configurable.PythonTypes import IntConfigurable
        self.layer: IntConfigurable = IntConfigurable(None, "layer", 0, "Current layer")
        """Current layer"""

        from BaseMod.baseMod import BaseMod

        self.config.init_configs(self.application.parser.isSet(self.application.args.reset))  # mounting configs and applying them
        self.basemod: BaseMod = BaseMod(self, "")
        """Check `BaseMod.BaseMod`"""

        self.mods.append(self.basemod)
        self.pre_init_mods()
        self.init_mods()

        v = self.open_level(RWELevel(self, file))

        self.init_editors(v)
        self.basemod.preferences.update_themes()
        log("Finished initiating")

    def open_level(self, level: RWELevel) -> None:
        """Opens RWELevel in new tab

        :param level: Level to load
        :return: None
        """
        v = ViewPort(level, self)
        self.window.add_viewport(v)
        return v

    def open_level_from_path(self, path: str) -> None:
        """Opens level from path in new tab

        :param path: Path to level
        :return: None
        """
        if not os.path.exists(path):
            return
        self.open_level(RWELevel(self, path))

    def init_editors(self, v: RWELevel) -> None:
        """Initiates all editors from mods

        Shouldn't be used in a mod

        :param v: level
        :return: None
        """
        if len(self.editors) <= 0:
            log("No editors found!!!", True)  # fucking explode idk
            return
        self.mount_editor()
        #self.editors[0].init_scene_items(self.selected_viewport)

    def init_mods(self) -> None:
        """Initiates mods"""
        for i in self.mod_types:
            self.mods.append(i[0](self, i[1]))

    def pre_init_mods(self) -> None:
        """Loads mods from mods folder"""
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


    def add_editor(self, editor, ui: UI) -> None:
        """Adds Editor to Manager, connected with ui

        :deprecated: You should use `Mod.add_editor` instead

        :param editor: Editor to add
        :param ui: Ui connected to editor
        :return: None
        """
        self.editors.append(editor)
        self.window.ui.ToolsTabs.addTab(ui, ui.objectName())
        ui.editor_linked(editor)
        #self.window.ui.menuEditors.addAction()
        # ui.setParent(self.window.ui.ToolsTabs)

    def add_view(self, ui: ViewUI) -> None:
        """Adds View Ui to Manager

        :deprecated: You should use `Mod.add_view` instead

        :param ui: View ui
        :return: None
        """
        self.window.ui.ViewTab.addTab(ui, ui.objectName())

    def add_quick_option(self, element: QWidget) -> None:
        """Adds quick option in "Quick" tab

        :deprecated: use `Mod.add_quick_option` instead

        :param element: Element to add
        :return: None
        """
        self.window.ui.QuickOverlay.addWidget(element)

    def add_setting(self, setting: SettingElement) -> None:
        """Adds setting in Preferences menu

        :deprecated: Use `Mod.add_setting` instead

        :param setting: Setting to add
        :return: None
        """
        self.setting_trees.append(setting)

    def add_hotkeytree(self, hotkey: HotkeyElement) -> None:
        """Adds HotkeyTree to Hotkeys menu

        :param hotkey: Tree to add
        :return: None
        """
        self.hotkey_trees.append(hotkey)

    def undo(self):
        """Undoes change on current level"""
        self.selected_viewport.level.undo()
        self.selected_viewport.clean()

    def redo(self):
        """Redoes change on current level"""
        self.selected_viewport.level.redo()
        self.selected_viewport.clean()

    @property
    def view_menu(self) -> QMenu:
        """View menu on menu bar

        :return: View menu
        :rtype: QMenu
        """
        return self.window.ui.menuView

    @property
    def tool_menu(self) -> QMenu:
        """Tool menu on menu bar

        :return: Tool menu
        :rtype: QMenu
        """
        return self.window.ui.menutools

    @property
    def window_menu(self) -> QMenu:
        """Window menu on menu bar

        :return: Window menu
        :rtype: QMenu
        """
        return self.window.ui.menuWindow

    @property
    def edit_menu(self) -> QMenu:
        """Edit menu on menu bar

        :return: Edit menu
        :rtype: QMenu
        """
        return self.window.ui.menuedit

    @property
    def editors_menu(self) -> QMenu:
        """Editors menu on menu bar

        :return: Editors menu
        :rtype: QMenu
        """
        return self.window.ui.menuEditors

    @property
    def menu_bar(self) -> QMenuBar:
        """Menu Bar that holds all the menus
        
        :return: Menu Bar
        :rtype: QMenuBar
        """
        return self.window.ui.menubar

    def set_status(self, message: str) -> None:
        """Changes status of status bar
        
        :param message: Message to show
        :return: None
        """
        # self.window.ui.viewPort.setStatusTip(message)
        self.window.statusBar().showMessage(message)

    @property
    def editor(self) -> Editor:
        """Currently used Editor
        
        :return: Current Editor in use
        :rtype: Editor
        """
        return self.editors[self._current_editor]

    def change_editor_name(self, name: str) -> None:
        """Changes editor based on name
        
        :param name: Name of new editor
        :return: None
        """
        for i in range(self.window.ui.ToolsTabs.count()):
            if self.window.ui.ToolsTabs.tabText(i).lower() == name.lower():
                self.window.ui.ToolsTabs.setCurrentIndex(i)
                # self.change_editor(i)
                return
        log(f"Couldn't find editor {name}", True)

    def change_editor(self, value: int) -> None:
        """Changes editor to new one, based on editor order in Editors panel
        
        :param value: New editor index
        :return: None
        """
        self.selected_viewport.remove_module(self.editor)
        self._current_editor = value
        self.mount_editor()

    def mount_editor(self) -> None:
        """Mounts graphical elements of editor onto current Viewport
        
        :return: None
        """
        if self.window.ui.tabWidget.count() == 0:
            return
        # self.selected_viewport.remove_module(self.editor)
        self.selected_viewport.add_module(self.editor, editor=True)
        self.selected_viewport.clean()

    @property
    def level_width(self) -> int:
        """Width of level, in cells
        
        :return: Level Width
        :rtype: int
        """
        return self.selected_viewport.level.level_width

    @property
    def level_height(self) -> int:
        """Height of level, in cells
        
        :return: Level Height
        :rtype: int
        """
        return self.selected_viewport.level.level_height

    @Slot()
    def save_level(self) -> None:
        """Saves current level and RWE#'s config

        :return: None
        """
        self.selected_viewport.save_level()
        self.config.save_configs()

    @Slot()
    def save_level_as(self) -> None:
        """Lets you specify levels save path and saves RWE#'s config

        :return: None
        """
        self.selected_viewport.save_level_as()
        self.config.save_configs()

    @property
    def selected_viewport(self) -> ViewPort:
        """Currently shown Viewport

        :return: Current Viewport
        :rtype: ViewPort
        """
        return self.window.ui.tabWidget.currentWidget()
