import os.path
from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *
from core.info import PATH_FILES_IMAGES_PALETTES


class TileViewConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "tileView")

    def register_config(self):
        self.drawl1 = BoolConfigurable("drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable("drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable("drawl3", True, "Draw layer 3")
        self.drawlheads = BoolConfigurable("drawlheads", True, "Draw tile heads")
        self.drawlmats = BoolConfigurable("drawlmats", True, "Draw materials")

        self.drawoption = IntConfigurable("drawoption", 0, "Option how to draw tiles")
        self.palettepath = StringConfigurable("palettepath", os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"), "Path to palettes")

        self.drawl1notrendered = FloatConfigurable("drawl1notrend", .9, "Layer 1 draw opacity(classic and henry)")
        self.drawl2notrendered = FloatConfigurable("drawl2notrend", .5, "Layer 2 draw opacity(classic and henry)")
        self.drawl3notrendered = FloatConfigurable("drawl3notrend", .2, "Layer 3 draw opacity(classic and henry)")

        self.drawl1rendered = FloatConfigurable("drawl1rend", 1, "Layer 1 draw opacity(rendered)")
        self.drawl2rendered = FloatConfigurable("drawl2rend", 1, "Layer 2 draw opacity(rendered)")
        self.drawl3rendered = FloatConfigurable("drawl3rend", 1, "Layer 3 draw opacity(rendered)")

        self.add_config(self.drawl1)
        self.add_config(self.drawl2)
        self.add_config(self.drawl3)
        self.add_config(self.drawlheads)
        self.add_config(self.drawlmats)
        self.add_config(self.drawoption)
        self.add_config(self.palettepath)

        self.add_config(self.drawl1notrendered)
        self.add_config(self.drawl2notrendered)
        self.add_config(self.drawl3notrendered)

        self.add_config(self.drawl1rendered)
        self.add_config(self.drawl2rendered)
        self.add_config(self.drawl3rendered)
