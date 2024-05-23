from core.ItemData import ItemData
from core.Loaders import TileLoader
from core.RWELevel import RWELevel
from core.Modify.RenderTexture import RenderTexture
from core.Modify.EditorMode import EditorMode
from core.Modify.Mod import Mod
from core.Modify.baseModule import Module
from core.Config import Config
from BaseMod.baseMod import BaseMod
from widgets.Viewport import ViewPort
from ui.splashuiconnector import SplashDialog
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot


class Manager:
    '''
    Manager of all RWE#
    '''
    def __init__(self, window, file=None):
        """
        :param window: RWE# window(main window with viewport and stuff)
        :param file: file to load by default
        """
        # todo init some tiles and assets (and mods in future)
        self.window = window

        self.splashwindow = SplashDialog(self)
        self.splashwindow.show()

        self.tiles = TileLoader.loadTiles(self.splashwindow)
        self.props = ItemData()
        self.effects = ItemData()
        self.effect_colors = ItemData()

        self.splashwindow.close()

        if file is not None:
            self.level = RWELevel.openfile(file)
        else:
            self.level = RWELevel()

        self.viewport: ViewPort = window.ui.viewPort

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

        self.editorlayers = []

        self.init_mods()
        self.config.init_configs()  # mounting configs and applying them
        print(self.mods[0].config.geo_selectedTool.value)
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

        for i in self.modules:
            i.init_module_textures()


    def init_editors(self):
        if len(self.editors) <= 0:
            print("No editors found!!!")
            return
        self.editors[0].init_scene_items()

    def init_mods(self):
        self.mods.append(BaseMod(self))

    def add_editor(self, editor, ui: QWidget):
        self.editors.append(editor)
        self.window.ui.ToolsTabs.addTab(ui, ui.objectName())
        # ui.setParent(self.window.ui.ToolsTabs)

    def add_module(self, module):
        self.modules.append(module)

    def add_view(self, ui: QWidget):
        self.window.ui.ViewTab.addTab(ui, ui.objectName())

    def add_quick_option(self, element: QWidget):
        self.window.ui.QuickOverlay.addWidget(element)

    def set_status(self, message: str):
        self.window.ui.viewPort.setStatusTip(message)
        pass

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
