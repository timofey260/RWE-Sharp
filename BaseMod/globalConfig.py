from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *


class globalConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod)

    def register_config(self):
        self.geo_selectedTool = StringConfigObject("tool", "wall", "wall")

        self.add_config(self.geo_selectedTool)