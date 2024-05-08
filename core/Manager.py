from core import info
from core.ItemData import ItemData
from core.Loaders import TileLoader
from core.RWELevel import RWELevel
from core.renderTextures.rtBase import RenderTexture
from core.renderTextures.GeoRenderTexture import GeoRenderTexture
from core.Modules.baseModule import Module
from core.Modules.geometryModule import GeoModule
from widgets.Viewport import ViewPort
from core.EditorModes.EditorMode import EditorMode
from core.EditorModes.GeometryEditor import GeometryEditor


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

        self.tiles = TileLoader.loadTiles(info.PATH_DRIZZLE)
        self.props = ItemData()
        self.effects = ItemData()
        self.effect_colors = ItemData()

        if file is not None:
            self.level = RWELevel.load_from_file(file)
        else:
            self.level = RWELevel()

        self.viewport: ViewPort = window.ui.viewPort

        self.currenteditor = 0
        self.editors: list[EditorMode] = []
        """
        Editors made to edit specific stuff in level depending on editor
        """
        self.modules: list[Module] = []
        """
        All modules work* at the same time so they arent limited by current editor
            *they arent exactly working, just doing stuff when they need to
        Modules are made to split size of manager and provide more availability to mod
        """

        self.editorlayers = []
        self.init_layers()
        self.init_editors()
        print(self.editorlayers)

    def init_layers(self):
        editorlayers: list[tuple[int, RenderTexture]] = []

        self.modules.append(GeoModule(self))
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
        self.editors.append(GeometryEditor(self))

        self.editors[0].init_scene_items()


    @property
    def level_width(self):
        return self.level.levelwidth

    @property
    def level_height(self):
        return self.level.levelheight

    def new_process(self, file=None):
        pass