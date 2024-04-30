from core import info
from core.ItemData import ItemData
from core.Loaders import TileLoader
from core.RWELevel import RWELevel
from core.renderTextures import GeoRenderTexture
from core.renderTextures import rtBase

class Manager:
    def __init__(self, file=None):
        # todo init some tiles and assets (and mods in future)

        self.tiles = TileLoader.loadTiles(info.PATH_DRIZZLE)
        self.props = ItemData()
        self.effects = ItemData()
        self.effect_colors = ItemData()

        if file is not None:
            self.level = RWELevel.load_from_file(file)
        else:
            self.level = RWELevel()
        self.rendertextures: list[rtBase.RenderTexture] = []

        self.rendertextures.append(GeoRenderTexture.GeoRenderTexture(self, 2))
        self.rendertextures.append(GeoRenderTexture.GeoRenderTexture(self, 1))
        self.rendertextures.append(GeoRenderTexture.GeoRenderTexture(self, 0))

    @property
    def level_width(self):
        return self.level.levelwidth

    @property
    def level_height(self):
        return self.level.levelheight

    def new_process(self, file=None):
        pass