from core.Modify.ConfigModule import ConfigModule
from core.configTypes.BaseTypes import *
from core.configTypes.QtTypes import *
from PySide6.QtGui import QKeySequence


class globalConfig(ConfigModule):
    def __init__(self, mod):
        super().__init__(mod, "global")

    def register_config(self):
        self.opacityl1 = FloatConfigurable(self, "opacityl1", .9, "opacity of the first layer")
        self.opacityl2 = FloatConfigurable(self, "opacityl2", .5, "opacity of the second layer")
        self.opacityl3 = FloatConfigurable(self, "opacityl3", .2, "opacity of the third layer")

        self.backgroundcolor = ColorConfigurable(self, "bgcolor", QColor(150, 150, 150), "color of the background")

        self.undo_key = KeyConfigurable(self, "undo", QKeySequence("Ctrl+z"), "Key to undo")
        self.redo_key = KeyConfigurable(self, "redo", QKeySequence("Ctrl+Shift+z"), "Key to redo")

        self.save_key = KeyConfigurable(self, "save", QKeySequence("Ctrl+s"), "Key to save the level")