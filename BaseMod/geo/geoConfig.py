from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *
from core.configTypes.QtTypes import *


class GeoConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "geo")

    def config_init(self):
        self.selectedTool = StringConfigurable(self, "tool", "wall", "Current geo tool")
        self.drawl1 = BoolConfigurable(self, "drawl1", True, "Draw blocks on 1st layer")
        self.drawl2 = BoolConfigurable(self, "drawl2", False, "Draw blocks on 2nd layer")
        self.drawl3 = BoolConfigurable(self, "drawl3", False, "Draw blocks on 3rd layer")

        self.drawl1_key = KeyConfigurable(self, "drawl1_key", QKeySequence("Ctrl+1"), "key to draw on 1st layer")
        self.drawl2_key = KeyConfigurable(self, "drawl2_key", QKeySequence("Ctrl+2"), "key to draw on 2nd layer")
        self.drawl3_key = KeyConfigurable(self, "drawl3_key", QKeySequence("Ctrl+3"), "key to draw on 3rd layer")


class GeoViewConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "geoView")

    def config_init(self):
        self.drawAll = BoolConfigurable(self, "drawall", False, "Draw all layers")
        self.drawl1 = BoolConfigurable(self, "drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable(self, "drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable(self, "drawl3", True, "Draw layer 3")
        self.opacityl1 = FloatConfigurable(self, "opacityl1", .9, "opacity of the first layer")
        self.opacityl2 = FloatConfigurable(self, "opacityl2", .5, "opacity of the second layer")
        self.opacityl3 = FloatConfigurable(self, "opacityl3", .2, "opacity of the third layer")
        self.opacityrgb = FloatConfigurable(self, "opacityrgb", .5, "opacity of all layers on old rendering option")

        self.drawlbeams = BoolConfigurable(self, "drawlbeams", True, "Draw Beams")
        self.drawlpipes = BoolConfigurable(self, "drawlpipes", True, "Draw pipes")
        self.drawlmisc = BoolConfigurable(self, "drawlmisc", True, "Draw rocks, spears etc")

        self.drawoption = IntConfigurable(self, "drawOption", 0, "method of drawing")

        self.drawl1_key = KeyConfigurable(self, "drawl1_key", QKeySequence("Alt+1"), "key to show 1st layer")
        self.drawl2_key = KeyConfigurable(self, "drawl2_key", QKeySequence("Alt+2"), "key to show 2nd layer")
        self.drawl3_key = KeyConfigurable(self, "drawl3_key", QKeySequence("Alt+3"), "key to show 3rd layer")
        self.drawlbeams_key = KeyConfigurable(self, "drawl3beamskey", QKeySequence("Alt+b"), "key to show 3rd layer")
        self.drawlpipes_key = KeyConfigurable(self, "drawlpipes_key", QKeySequence("Alt+v"), "key to show 3rd layer")
        self.drawlmisc_key = KeyConfigurable(self, "drawlmisc_key", QKeySequence("Alt+c"), "key to show 3rd layer")
