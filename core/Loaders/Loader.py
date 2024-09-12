from PySide6.QtCore import QThread
from core.ItemData import ItemData
from core.Loaders.Tile import Tiles
from core.Loaders.Prop import Props
from core.Loaders.Effect import Effects


class Loader(QThread):
    def __init__(self, splash):
        super().__init__(splash)
        self.splashwindow = splash
        self.tiles: Tiles | None = None
        self.props: Props | None = None
        self.effects: Effects | None = None
        self.effect_colors = None

    def run(self):
        from core.Loaders.TileLoader import load_tiles
        from core.Loaders.EffectLoader import load_effects
        from core.Loaders.PropLoader import load_props
        self.tiles = load_tiles(self.splashwindow)
        self.props = load_props(self.tiles, self.splashwindow)
        self.effects = load_effects(self.splashwindow)
        self.effect_colors = ItemData()
        # self.finished.emit()
