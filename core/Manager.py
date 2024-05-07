from core import info
from core.ItemData import ItemData
from core.Loaders import TileLoader
from core.RWELevel import RWELevel


class Manager:
    '''
    Manager of all RWE#
    '''
    def __init__(self, window, file=None):
        """
        :param window: RWE# window
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


    @property
    def level_width(self):
        return self.level.levelwidth

    @property
    def level_height(self):
        return self.level.levelheight

    def new_process(self, file=None):
        pass