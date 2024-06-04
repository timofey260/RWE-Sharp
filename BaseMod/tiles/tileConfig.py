import os.path
from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *
from core.configTypes.QtTypes import KeyConfigurable
from core.info import PATH_FILES_IMAGES_PALETTES
from PySide6.QtGui import QKeySequence


class TileViewConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "tileView")

    def config_init(self):
        self.drawl1 = BoolConfigurable(self, "drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable(self, "drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable(self, "drawl3", True, "Draw layer 3")
        self.drawlheads = BoolConfigurable(self, "drawlheads", True, "Draw tile heads")
        self.drawlmats = BoolConfigurable(self, "drawlmats", True, "Draw materials")

        self.drawoption = IntConfigurable(self, "drawoption", 0, "Option how to draw tiles")
        self.palettepath = StringConfigurable(self, "palettepath", os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"), "Path to palettes")

        self.drawl1notrendered = FloatConfigurable(self, "drawl1notrend", .9, "Layer 1 draw opacity(classic and henry)")
        self.drawl2notrendered = FloatConfigurable(self, "drawl2notrend", .5, "Layer 2 draw opacity(classic and henry)")
        self.drawl3notrendered = FloatConfigurable(self, "drawl3notrend", .2, "Layer 3 draw opacity(classic and henry)")

        self.drawl1rendered = FloatConfigurable(self, "drawl1rend", 1, "Layer 1 draw opacity(rendered)")
        self.drawl2rendered = FloatConfigurable(self, "drawl2rend", 1, "Layer 2 draw opacity(rendered)")
        self.drawl3rendered = FloatConfigurable(self, "drawl3rend", 1, "Layer 3 draw opacity(rendered)")

        self.drawl1_key = KeyConfigurable(self, "drawl1_key", QKeySequence("Alt+Shift+1"), "layer 1 key")
        self.drawl2_key = KeyConfigurable(self, "drawl2_key", QKeySequence("Alt+Shift+2"), "layer 2 key")
        self.drawl3_key = KeyConfigurable(self, "drawl3_key", QKeySequence("Alt+Shift+3"), "layer 3 key")
