from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *
from core.configTypes.QtTypes import *


class globalConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "global")

    def register_config(self):
        self.opacityl1 = FloatConfigurable("opacityl1", .9, "opacity of the first layer")
        self.add_config(self.opacityl1)
        self.opacityl2 = FloatConfigurable("opacityl2", .5, "opacity of the second layer")
        self.add_config(self.opacityl2)
        self.opacityl3 = FloatConfigurable("opacityl3", .2, "opacity of the third layer")
        self.add_config(self.opacityl3)

        self.backgroundcolor = ColorConfigurable("bgcolor", QColor(150, 150, 150), "color of the background")
        self.add_config(self.backgroundcolor)