from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import BoolConfigurable, FloatConfigurable
from core.configTypes.QtTypes import KeyConfigurable, QKeySequence


class GridConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "grid")

    def config_init(self):
        self.enablegrid = BoolConfigurable(self, "enablegrid", False, "Enable grid")
        self.gridopacity = FloatConfigurable(self, "gridopacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(self, "enablegrid_key", QKeySequence("Ctrl+G"), "Grid key")