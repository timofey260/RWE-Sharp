from core.RWELevel import RWELevel, defaultlevel
from core.Modify.EditorMode import EditorMode
from core.Modify.Mod import Mod
from core.Modify.baseModule import Module
from core.Modify.Palette import Palette
from core.Config import Config
from core.SettingTree import SettingElement
from core.info import PATH_MODS
from core.ModLoader import load_mod
from widgets.Viewport import ViewPort
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu
from PySide6.QtCore import Slot
from ui.mainuiconnector import MainWindow
from ui.splashuiconnector import SplashDialog
import os


class Manager:
    '''
    Manager that controls all of RWE#(except for gui)
    '''
    def __init__(self, window: MainWindow, splash: SplashDialog, file=None):
        """
        :param window: RWE# window(main window with viewport and stuff)
        :param file: file to load by default
        """
        self.window: MainWindow = window

        self.tiles = splash.loader.tiles
        self.props = splash.loader.props
        self.effects = splash.loader.effects
        self.effect_colors = splash.loader.effect_colors

        # self.splashwindow.close()

        self.levelpath: str = "" if file is None else file
        if file is not None:
            self.level = RWELevel.openfile(self, file)
        else:
            self.level = RWELevel.turntoproject(self, defaultlevel)

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
        self.viewfolders: list[str] = []
        """
        list of strings for view specific menu items
        """
        self.palettes: list[Palette] = []
        """
        neat color visuals
        """
        self.setting_trees: list[SettingElement] = []
        """
        Collection of ui's for settings window
        """
        from BaseMod.baseMod import BaseMod
        self.basemod = BaseMod(self)

        self.mods.append(self.basemod)
        self.pre_init_mods()
        self.config.init_configs()  # mounting configs and applying them
        self.init_mods()
        self.init_modules()
        self.init_editors()
        self.change_pallete()

    def change_pallete(self):
        if self.basemod.palette.value == "":
            return
        for i in self.palettes:
            if self.basemod.palette.value == f"{i.mod.author_name}.{i.name}":
                self.window.setPalette(i.palette)

    def init_modules(self):
        for i in self.modules:
            self.viewport.add_module(i)
        for i in self.modules:
            i.render_module()

    def init_editors(self):
        if len(self.editors) <= 0:
            print("No editors found!!!")  # fucking explode idk
            return
        self.editors[0].init_scene_items()

    def init_mods(self):
        for i in self.mods:
            i.mod_init()

    def pre_init_mods(self):
        # mods adding
        for i in os.listdir(PATH_MODS):
            if not os.path.isdir(os.path.join(PATH_MODS, i)):
                continue
            mod = load_mod(os.path.join(PATH_MODS, i), self)
            print(f"Loaded {mod.modinfo.title} by {mod.modinfo.author} v{mod.modinfo.version}")
            if mod is not None:
                self.mods.append(mod)
        for i in self.mods:
            # check if mod is enabled
            i.pre_mod_init()

    def add_editor(self, editor, ui: QWidget):
        self.editors.append(editor)
        self.window.ui.ToolsTabs.addTab(ui, ui.objectName())
        # ui.setParent(self.window.ui.ToolsTabs)

    def add_module(self, module):
        self.modules.append(module)

    def add_view(self, ui: QWidget) -> None:
        self.window.ui.ViewTab.addTab(ui, ui.objectName())

    def add_quick_option(self, element: QWidget) -> None:
        self.window.ui.QuickOverlay.addWidget(element)

    def add_setting(self, setting: SettingElement):
        self.setting_trees.append(setting)

    @property
    def view_menu(self) -> QMenu:
        return self.window.ui.menuView

    @property
    def tool_menu(self) -> QMenu:
        return self.window.ui.menuView

    @property
    def edit_menu(self) -> QMenu:
        return self.window.ui.menuView

    @property
    def menu_bar(self) -> QMenuBar:
        return self.window.ui.menubar

    def set_status(self, message: str) -> None:
        # self.window.ui.viewPort.setStatusTip(message)
        self.window.statusBar().showMessage(message)

    @property
    def editor(self) -> EditorMode:
        return self.editors[self.current_editor]

    def change_editor(self, value: int):
        self.editor.remove_items_from_scene()
        self.current_editor = value
        self.editor.init_scene_items()

    @property
    def level_width(self):
        return self.level.level_width

    @property
    def level_height(self):
        return self.level.level_height

    @Slot()
    def save_level(self):
        print("saving")
        # todo level saving
        # config saving
        self.config.save_configs()
