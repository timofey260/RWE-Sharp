from core.RWELevel import RWELevel
from core.Modify.EditorMode import EditorMode
from core.Modify.Mod import Mod
from core.Modify.baseModule import Module
from core.Modify.Palette import Palette
from core.Config import Config
from core.TreeElement import SettingElement, HotkeyElement
from core.info import PATH_MODS
from core.ModLoader import load_mod
from core.utils import log
from widgets.Viewport import ViewPort
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu
from PySide6.QtCore import Slot
from ui.mainuiconnector import MainWindow
from core.ItemData import ItemData
from core.Loaders.Tile import Tiles
from core.Loaders.Effect import Effects
from core.Application import Application
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
        self.props: ItemData = splash.loader.props
        self.effects: Effects = splash.loader.effects
        self.effect_colors = splash.loader.effect_colors

        # self.splashwindow.close()

        # self.levelpath: str = "" if file is None else file
        self.level = RWELevel(self, file)

        self.viewport: ViewPort = self.window.ui.viewPort

        self.current_editor = 0
        self.editors: list[EditorMode] = []
        """
        Editors made to edit specific stuff in level depending on editor
        """

        self.modules: list[Module] = []
        """
        Modules are made for viewport modifying
        """
        self.mods: list[Mod] = []
        """
        Mods are what powers RWE#
        """
        self.config = Config(self)
        """
        Configs are used to store editor-specific data
        """
        self.palettes: list[Palette] = []
        """
        neat color visuals
        """
        self.setting_trees: list[SettingElement] = []
        """
        Collection of ui's for settings window
        """
        self.hotkey_trees: list[HotkeyElement] = []
        """
        Collection of ui's for settings window
        """
        from BaseMod.baseMod import BaseMod
        self.basemod = BaseMod(self, "")

        self.mods.append(self.basemod)
        self.pre_init_mods()
        self.config.init_configs()  # mounting configs and applying them
        self.init_mods()
        self.init_modules()
        self.init_editors()
        self.change_pallete()

    def change_level(self, path):
        self.level = None
        self.level = RWELevel(self, path)
        self.viewport.levelchanged()

    def change_pallete(self):
        if self.basemod.bmconfig.palette.value == "":
            return
        for i in self.palettes:
            if self.basemod.bmconfig.palette.value == f"{i.mod.author_name}.{i.name}":
                if i.palette is not None:
                    self.application.app.setPalette(i.palette)
                if i.style is not None:
                    self.application.app.setStyleSheet(i.style)
                log(f"Using palette {i.name}")
                return

    def init_modules(self):
        for i in self.modules:
            self.viewport.add_module(i)
        for i in self.modules:
            i.render_module()

    def init_editors(self):
        if len(self.editors) <= 0:
            log("No editors found!!!", True)  # fucking explode idk
            return
        self.editors[0].init_scene_items()

    def init_mods(self):
        for i in self.mods:
            i.mod_init()

    def pre_init_mods(self):
        # mods adding
        for indx, i in enumerate(os.listdir(PATH_MODS)):
            if not os.path.isdir(os.path.join(PATH_MODS, i)):
                continue
            mod = load_mod(os.path.join(PATH_MODS, i), self, indx)
            if mod is not None:
                log(f"Loaded {mod.modinfo.title} by {mod.modinfo.author} v{mod.modinfo.version}")
                self.mods.append(mod)

    def add_editor(self, editor, ui: QWidget):
        self.editors.append(editor)
        self.window.ui.ToolsTabs.addTab(ui, ui.objectName())
        #self.window.ui.menuEditors.addAction()
        # ui.setParent(self.window.ui.ToolsTabs)

    def add_module(self, module):
        self.modules.append(module)

    def add_view(self, ui: QWidget) -> None:
        self.window.ui.ViewTab.addTab(ui, ui.objectName())

    def add_quick_option(self, element: QWidget) -> None:
        self.window.ui.QuickOverlay.addWidget(element)

    def add_setting(self, setting: SettingElement):
        self.setting_trees.append(setting)

    def add_hotkeytree(self, hotkey: HotkeyElement):
        self.hotkey_trees.append(hotkey)

    def undo(self):
        self.level.undo()

    def redo(self):
        self.level.redo()

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
    def editor(self) -> EditorMode:
        return self.editors[self.current_editor]

    def change_editor_name(self, name: str):
        for i in range(self.window.ui.ToolsTabs.count()):
            if self.window.ui.ToolsTabs.tabText(i).lower() == name.lower():
                self.window.ui.ToolsTabs.setCurrentIndex(i)
                # self.change_editor(i)
                return
        log(f"Couldn't find editor {name}", True)

    def change_editor(self, value: int):
        self.editor.remove_items_from_scene()
        self.current_editor = value
        self.editor.init_scene_items()
        self.viewport.repaint()
        self.editor.zoom_event(self.viewport.zoom)
        self.editor.move_event(self.viewport.topleft.pos())
        for i in self.modules:
            i.zoom_event(self.viewport.zoom)
            i.move_event(self.viewport.topleft.pos())

    @property
    def level_width(self):
        return self.level.level_width

    @property
    def level_height(self):
        return self.level.level_height

    @Slot()
    def save_level(self):
        self.level.save_file()
        # config saving
        self.config.save_configs()
