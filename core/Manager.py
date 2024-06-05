from core.RWELevel import RWELevel, defaultlevel
from core.Modify.RenderTexture import RenderTexture
from core.Modify.EditorMode import EditorMode
from core.Modify.Mod import Mod
from core.Modify.baseModule import Module
from core.Config import Config
from BaseMod.baseMod import BaseMod
from widgets.Viewport import ViewPort
from ui.splashuiconnector import SplashDialog
from PySide6.QtWidgets import QWidget, QMenuBar, QMenu
from PySide6.QtCore import Slot
from ui.mainuiconnector import MainWindow


class Manager:
    '''
    Manager that controls all of RWE#(except for gui)
    '''
    def __init__(self, window: MainWindow, splash: SplashDialog, file=None):
        """
        :param window: RWE# window(main window with viewport and stuff)
        :param file: file to load by default
        """
        # todo init some tiles and assets (and mods in future)
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

        self.editorlayers = []

        self.basemod = BaseMod(self)

        self.pre_init_mods()
        self.config.init_configs()  # mounting configs and applying them
        self.init_mods()
        self.init_layers()
        self.init_editors()


    def init_layers(self):
        editorlayers: list[tuple[int, RenderTexture]] = []
        # mod editor layers

        for i in self.modules:
            for l in i.editorlayers:
                editorlayers.append(l)
        editorlayers.sort(key=lambda x: x[0])
        self.editorlayers: list[RenderTexture] = list(map(lambda x: x[1], editorlayers))

        for i in self.editorlayers:
            img = self.viewport.add_texture(i.image)
            i.renderedtexture = img
            i.field_init()

        for i in self.modules:
            i.init_module_textures()
            i.render_module()


    def init_editors(self):
        if len(self.editors) <= 0:
            print("No editors found!!!")
            return
        self.editors[0].init_scene_items()

    def init_mods(self):
        for i in self.mods:
            i.mod_init()

    def pre_init_mods(self):
        self.mods.append(self.basemod)
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

    @property
    def view_menu(self) -> QMenu:
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
