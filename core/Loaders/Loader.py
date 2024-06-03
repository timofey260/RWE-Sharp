from PySide6.QtCore import QThread
from .TileLoader import loadTiles
from core.ItemData import ItemData


class Loader(QThread):
    def __init__(self, splash, parent=None):
        super().__init__(parent)
        self.splashwindow = splash
        self.tiles = None
        self.props = None
        self.effects = None
        self.effect_colors = None

    def run(self):
        self.tiles = loadTiles(self.splashwindow)
        self.props = ItemData()
        self.effects = ItemData()
        self.effect_colors = ItemData()
        self.finished.emit()
