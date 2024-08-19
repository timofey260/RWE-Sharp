from RWESharp.Modify import Theme
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import PATH_BASEMOD
import re
import os


class RaspberryDark(Theme):
    def __init__(self, mod):
        super().__init__("Raspberry Dark", mod)
        self.styleindex = IntConfigurable(mod, "rpdar.styleoption", 0, description="Style file")


    def palette_enable(self):
        with open(os.path.join(PATH_BASEMOD, "palettes", "qssfiles", ["circular.txt", "sharp.txt", "atmoled.txt", "darkeum.txt"][self.styleindex.value])) as f:
            self.mod.manager.application.setStyleSheet(f.read())

    def palette_disable(self):
        self.mod.manager.application.setStyleSheet()
