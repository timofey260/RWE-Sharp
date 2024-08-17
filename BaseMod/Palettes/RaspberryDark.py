from RWESharp.Modify import Palette
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import PATH_BASEMOD
import re
import os


class RaspberryDark(Palette):
    def __init__(self, mod):
        super().__init__("Raspberry Dark", mod)
        self.styleindex = IntConfigurable(mod, "rpdar.styleoption", 1, description="Style file")

    def palette_enable(self):
        with open(os.path.join(PATH_BASEMOD, "Palettes", "qssfiles", ["Circular.txt", "Sharp.txt"][self.styleindex.value])) as f:
            self.mod.manager.application.setStyleSheet(f.read())
