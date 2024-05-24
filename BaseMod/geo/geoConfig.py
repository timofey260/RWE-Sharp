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