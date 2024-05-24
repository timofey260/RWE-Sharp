from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *


class GeoConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "geo")

    def register_config(self):
        self.selectedTool = StringConfigurable("tool", "wall", "Current geo tool")
        self.drawl1 = BoolConfigurable("drawl1", True, "Draw blocks on 1st layer")
        self.drawl2 = BoolConfigurable("drawl2", False, "Draw blocks on 2nd layer")
        self.drawl3 = BoolConfigurable("drawl3", False, "Draw blocks on 3rd layer")

        self.add_config(self.selectedTool)
        self.add_config(self.drawl1)
        self.add_config(self.drawl2)
        self.add_config(self.drawl3)

class GeoViewConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "geoView")

    def register_config(self):
        self.drawl1 = BoolConfigurable("drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable("drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable("drawl3", True, "Draw layer 3")
        self.drawlbeams = BoolConfigurable("drawlbeams", True, "Draw Beams")
        self.drawlpipes = BoolConfigurable("drawlpipes", True, "Draw pipes")
        self.drawlmisc = BoolConfigurable("drawlmisc", True, "Draw rocks, spears etc")

        self.add_config(self.drawl1)
        self.add_config(self.drawl2)
        self.add_config(self.drawl3)
        self.add_config(self.drawlbeams)
        self.add_config(self.drawlpipes)
        self.add_config(self.drawlmisc)