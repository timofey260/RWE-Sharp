from PySide6.QtCore import QThread
from RWESharp.Loaders.Tile import Tiles
from RWESharp.Loaders.Prop import Props
from RWESharp.Loaders.Effect import Effects


class Loader(QThread):
    def __init__(self, splash):
        super().__init__(splash)
        self.splashwindow = splash
        self.load_success = False
        self.tiles: Tiles | None = None
        self.props: Props | None = None
        self.effects: Effects | None = None
        self.prop_colors: list[list] | None = None

    def run(self):
        from RWESharp.Loaders.TileLoader import load_tiles
        from RWESharp.Loaders.EffectLoader import load_effects
        from RWESharp.Loaders.PropLoader import load_props, getcolors

        if not self.splashwindow.hasdrizzle:
            return

        self.tiles = load_tiles(self.splashwindow)
        self.props = load_props(self.tiles, self.splashwindow)
        self.effects = load_effects(self.splashwindow)
        self.prop_colors = getcolors()
        self.load_success = True
        print("Exit")
        # self.finished.emit()
