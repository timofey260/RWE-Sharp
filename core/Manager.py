from core import info
from core.ItemData import ItemData
from core import TileLoader
from core import PropLoader


class Manager:
    def __init__(self, file=None):
        if file is not None:
            pass
        # todo init some tiles and assets

        self.tiles = TileLoader.loadTiles(info.PATH_DRIZZLE)
        self.props = ItemData()
        self.effects = ItemData()
        self.effect_colors = ItemData()

    def new_process(self, file=None):
        pass