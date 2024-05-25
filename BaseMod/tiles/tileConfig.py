from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *


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

        self.add_config(self.drawl1)
        self.add_config(self.drawl2)
        self.add_config(self.drawl3)
        self.add_config(self.drawlheads)
        self.add_config(self.drawlmats)
        self.add_config(self.drawoption)
