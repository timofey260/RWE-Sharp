from core.RWELevel import RWELevel
from core.Modify.Editor import Editor
from core.Modify.Mod import Mod
from core.Modify.baseModule import Module
from core.Modify.Theme import Theme
from core.Config import Config
from core.TreeElement import SettingElement, HotkeyElement
from core.info import PATH_MODS, PATH_LEVELS
from core.ModLoader import load_mod
from core.utils import log
from core.Loaders.Tile import Tiles
from core.Loaders.Prop import Props
from core.Loaders.Effect import Effects
from core.Application import Application
from ui.mainuiconnector import MainWindow
from widgets.Viewport import ViewPort
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu, QFileDialog
from PySide6.QtCore import Slot
import os


class Manager:
    '''
    Manager that controls all of RWE#(except for gui)
    '''
    def __init__(self, window: MainWindow, app: Application, file=None):
        """
        :param window: RWE# window(main window with viewport and stuff)
        :param app: RWE# application class
        :param file: file to load by default
        """
        splash = app.splash
        self.window: MainWindow = window
        self.application: Application = app

        self.tiles: Tiles = splash.loader.tiles
        self.props: Props = splash.loader.props
        self.effects: Effects = splash.loader.effects
        self.effect_colors = splash.loader.effect_colors

        # self.levelpath: str = "" if file is None else file

        # self.viewports: list[ViewPort] = []

        self.current_editor = 0
        self.editors: list[Editor] = []
        """
        Editors made to edit specific stuff in level depending on editor
        """

        # self.modules: list[Module] = []
        # """
        # Modules are made for viewport modifying
        # """
        self.mods: list[Mod] = []
        """
        Mods are what powers RWE#
        """
        self.config = Config(self)
        """
        Configs are used to store editor-specific data
        """
        self.themes: list[Theme] = []
        """
        neat color visuals
        """
        self.setting_trees: list[SettingElement] = []
        """
        Collection of ui's for settings window
        """
        self.hotkey_trees: list[HotkeyElement] = []
        """
        Collection of ui's for hotkey window
        """
        self.current_theme: Theme | None = None
        self.mod_types = []
        from BaseMod.baseMod import BaseMod

        self.config.init_configs(self.application.args.reset)  # mounting configs and applying them
        self.basemod = BaseMod(self, "")

        self.mods.append(self.basemod)
        self.pre_init_mods()
        self.init_mods()

        v = self.open_level(RWELevel(self, file))

        self.init_editors(v)
        self.change_theme()
        log("Finished initiating")

    def open_level(self, level):
        v = ViewPort(level, self)
        self.window.add_viewport(v)
        return v

    def change_level(self, path):  # obsolete?
        self.open_level(RWELevel(self, path))

    def change_theme(self):
        if self.basemod.bmconfig.theme.value == "":
            if self.current_theme is not None:
                self.current_theme.theme_disable()
                log("Theme is Disabled")
                self.current_theme = None
            return
        for i in self.themes:
            if self.basemod.bmconfig.theme.value == f"{i.mod.author_name}.{i.name}":
                if self.current_theme is not None:
                    self.current_theme.theme_disable()
                i.theme_enable()
                self.current_theme = i
                log(f"Using Theme {i.name}")
                return

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
        # mods adding
        for indx, i in enumerate(os.listdir(PATH_MODS)):
            if not os.path.isdir(os.path.join(PATH_MODS, i)):
                continue
            mod = load_mod(os.path.join(PATH_MODS, i), self, indx)
            if mod is not None:
                self.mod_types.append(mod)

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
        return self.editors[self.current_editor]

    def change_editor_name(self, name: str):
        for i in range(self.window.ui.ToolsTabs.count()):
            if self.window.ui.ToolsTabs.tabText(i).lower() == name.lower():
                self.window.ui.ToolsTabs.setCurrentIndex(i)
                # self.change_editor(i)
                return
        log(f"Couldn't find editor {name}", True)

    def change_editor(self, value: int):
        self.selected_viewport.remove_module(self.editor)
        self.current_editor = value
        self.mount_editor()

    def mount_editor(self):
        self.selected_viewport.remove_module(self.editor)
        self.selected_viewport.add_module(self.editor)

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
