from PySide6.QtCore import QThread
from core.ItemData import ItemData


class Loader(QThread):
    def __init__(self, splash):
        super().__init__(splash)
        self.splashwindow = splash
        self.tiles = None
        self.props = None
        self.effects = None
        self.effect_colors = None

    def run(self):
        from .TileLoader import loadTiles
        self.tiles = loadTiles(self.splashwindow)
        self.props = ItemData()
        self.effects = ItemData()
        self.effect_colors = ItemData()
        # self.finished.emit()
