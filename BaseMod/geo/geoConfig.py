from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *
from core.configTypes.QtTypes import *


class GeoConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "geo")

    def register_config(self):
        self.selectedTool = StringConfigurable("tool", "wall", "Current geo tool")
        self.drawl1 = BoolConfigurable("drawl1", True, "Draw blocks on 1st layer")
        self.drawl2 = BoolConfigurable("drawl2", False, "Draw blocks on 2nd layer")
        self.drawl3 = BoolConfigurable("drawl3", False, "Draw blocks on 3rd layer")

        self.drawl1_key = KeyConfigurable("drawl1_key", QKeySequence("Ctrl+1"), "key to draw on 1st layer")
        self.drawl2_key = KeyConfigurable("drawl2_key", QKeySequence("Ctrl+2"), "key to draw on 2nd layer")
        self.drawl3_key = KeyConfigurable("drawl3_key", QKeySequence("Ctrl+3"), "key to draw on 3rd layer")

        self.add_config(self.selectedTool)
        self.add_config(self.drawl1)
        self.add_config(self.drawl2)
        self.add_config(self.drawl3)

class GeoViewConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "geoView")

    def register_config(self):
        self.drawAll = BoolConfigurable("drawall", False, "Draw all layers")
        self.drawl1 = BoolConfigurable("drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable("drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable("drawl3", True, "Draw layer 3")
        self.drawlbeams = BoolConfigurable("drawlbeams", True, "Draw Beams")
        self.drawlpipes = BoolConfigurable("drawlpipes", True, "Draw pipes")
        self.drawlmisc = BoolConfigurable("drawlmisc", True, "Draw rocks, spears etc")

        self.drawl1_key = KeyConfigurable("drawl1_key", QKeySequence("Alt+1"), "key to show 1st layer")
        self.drawl2_key = KeyConfigurable("drawl2_key", QKeySequence("Alt+2"), "key to show 2nd layer")
        self.drawl3_key = KeyConfigurable("drawl3_key", QKeySequence("Alt+3"), "key to show 3rd layer")
        self.drawlbeams_key = KeyConfigurable("drawl3beamskey", QKeySequence("Alt+b"), "key to show 3rd layer")
        self.drawlpipes_key = KeyConfigurable("drawlpipes_key", QKeySequence("Alt+v"), "key to show 3rd layer")
        self.drawlmisc_key = KeyConfigurable("drawlmisc_key", QKeySequence("Alt+c"), "key to show 3rd layer")


        self.add_config(self.drawAll)
        self.add_config(self.drawl1)
        self.add_config(self.drawl1_key)
        self.add_config(self.drawl2)
        self.add_config(self.drawl3)
        self.add_config(self.drawlbeams)
        self.add_config(self.drawlpipes)
        self.add_config(self.drawlmisc)