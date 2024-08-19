from PySide6.QtGui import QColor
from RWESharp.Modify import Theme
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import PATH_BASEMOD
from BaseMod.palettes.theme_palettes.MoonlightDark import moonlight_dark_palette
from BaseMod.palettes.theme_palettes.MintDark import mint_dark_palette
import os

from core.configTypes.QtTypes import ColorConfigurable


class RaspberryDark(Theme):
    def __init__(self, mod):
        from BaseMod.palettes.paletteuiconnector import RPDarkUI
        super().__init__("Raspberry Dark", mod)
        self.styleindex = IntConfigurable(mod, "rpdark.styleoption", 0, description="Style file")
        self.styleindex.valueChanged.connect(self.theme_enable)
        self.stylepalette = IntConfigurable(mod, "rpdark.stylepalette", 0, description="Style palette")
        self.stylepalette.valueChanged.connect(self.theme_enable)
        self.themefiles = ["circular", "sharp", "atmoled", "darkeum"]
        self.settings = RPDarkUI(self)
        self.currentstyle = ""
        self.multiple = False

        self.colors = mint_dark_palette

        for i in self.colors:
            i.valueChanged.connect(self.theme_reenable)

    def theme_reenable(self):
        if self.multiple:
            return
        newtext = self.currentstyle
        for i in self.colors:
            newtext = newtext.replace(i.name, i.value.name())
        self.mod.manager.application.setStyleSheet(newtext)

    def theme_enable(self):
        with open(os.path.join(PATH_BASEMOD, "palettes", "qssfiles", self.themefiles[self.styleindex.value]) + ".txt") as f:
            newtext = f.read()
            self.currentstyle = newtext
            for i in self.colors:
                newtext = newtext.replace(i.name, i.value.name())
            self.mod.manager.application.setStyleSheet(newtext)
            print ("Applied " + self.themefiles[self.styleindex.value])
            print (newtext)
    def theme_disable(self):
        self.mod.manager.application.setStyleSheet("")
