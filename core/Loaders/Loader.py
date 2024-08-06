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
        from core.Loaders.TileLoader import load_tiles
        from core.Loaders.EffectLoader import load_effects
        self.tiles = load_tiles(self.splashwindow)
        self.props = ItemData()
        self.effects = load_effects(self.splashwindow)
        self.effect_colors = ItemData()
        # self.finished.emit()
