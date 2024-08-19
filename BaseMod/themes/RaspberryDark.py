from PySide6.QtGui import QColor
from RWESharp.Modify import Theme
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import PATH_BASEMOD
import os

from core.configTypes.QtTypes import ColorConfigurable


class RaspberryDark(Theme):
    def __init__(self, mod):
        from BaseMod.themes.paletteuiconnector import RPDarkUI
        super().__init__("Raspberry Dark", mod)
        self.styleindex = IntConfigurable(mod, "rpdark.styleoption", 0, description="Style file")
        self.styleindex.valueChanged.connect(self.theme_enable)
        self.stylepalette = IntConfigurable(mod, "rpdark.stylepalette", 0, description="Style palette")
        self.stylepalette.valueChanged.connect(self.palette_change)
        self.themefiles = ["sharp", "circular", "atmoled", "darkeum"]
        self.palettefiles = ["RaspberryDark", "MintDark", "MoonlightDark"]
        self.settings = RPDarkUI(self)
        self.currentstyle = ""
        self.multiple = False

        self.colors = [
            # base colors
            ColorConfigurable(mod, "@base_very_dark", "#050a0e", "Base color"),
            ColorConfigurable(mod, "@base_dark", "#9F2E34", "Base dark color"),
            ColorConfigurable(mod, "@base_medium", "#242424", "Base medium color"),
            ColorConfigurable(mod, "@base_light", "#555555", "Base light color"),
            ColorConfigurable(mod, "@base_very_light", "#C2C7CB", "Base very light color"),
            # background colors
            ColorConfigurable(mod, "@background_very_dark", "#050a0e", "Background color"),
            ColorConfigurable(mod, "@background_dark", "#151a1e", "Background dark color"),
            ColorConfigurable(mod, "@background_medium", "#1e282c", "Background medium color"),
            ColorConfigurable(mod, "@background_light", "#555555", "Background light color"),
            ColorConfigurable(mod, "@background_very_light", "#C2C7CB",
                              "Background very light color"),  # Placeholder value updated
            # border colors
            ColorConfigurable(mod, "@border_dark", "#424242", "Border dark color"),
            ColorConfigurable(mod, "@border_medium", "#AC2D3A", "Border medium color"),
            ColorConfigurable(mod, "@border_light", "#656565", "Border light color"),
            # text colors
            ColorConfigurable(mod, "@text_dark", "#757575", "Text dark color"),
            ColorConfigurable(mod, "@text_medium", "#9E9E9E", "Text medium color"),
            ColorConfigurable(mod, "@text_light", "#C4C4C4", "Text light color"),
            ColorConfigurable(mod, "@text_disabled", "#424242", "Text disabled color"),
            ColorConfigurable(mod, "@text_enabled", "#C4C4C4", "Text enabled color"),
            # accent colors
            ColorConfigurable(mod, "@accent_light", "#D81B43", "Accent light color"),
            ColorConfigurable(mod, "@accent_medium", "#C71F35", "Accent medium color"),
            ColorConfigurable(mod, "@accent_dark", "#A51D2D", "Accent dark color"),
            # alternative colors
            ColorConfigurable(mod, "@alt_base_dark", "#0A0A0A", "Alternative base dark color"),
            ColorConfigurable(mod, "@alt_base_medium", QColor.fromString("#1e1e1e"), "Alternative base medium color"),
            ColorConfigurable(mod, "@alt_base_light", "#2e2e2e", "Alternative base light color"),
            ColorConfigurable(mod, "@alt_text_misc", "#333333",
                              "Alternative miscellaneous text color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_border_dark", "#2e2e2e", "Alternative border dark color"),
            ColorConfigurable(mod, "@alt_border_medium", "#3e3e3e",
                              "Alternative border medium color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_border_light", "#4e4e4e", "Alternative border light color"),
            ColorConfigurable(mod, "@alt_text_dark", "#000000", "Alternative text dark color"),
            ColorConfigurable(mod, "@alt_text_medium", "#333333", "Alternative text medium color"),
            ColorConfigurable(mod, "@alt_text_light", "#cccccc", "Alternative text light color"),
            ColorConfigurable(mod, "@alt_text_disabled", "#666666",
                              "Alternative text disabled color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_text_enabled", "#ffffff", "Alternative text enabled color"),
            ColorConfigurable(mod, "@alt_accent_light", "#CF4465", "Alternative accent light color"),
            ColorConfigurable(mod, "@alt_accent_medium", "#F00FFF",
                          "Alternative accent medium color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_accent_dark", "#90293B", "Alternative accent dark color"),
            # misc colors
            ColorConfigurable(mod, "@misc_color_30", "#000000", "Miscellaneous color 30"),
            ColorConfigurable(mod, "@misc_color_31", "#000000", "Miscellaneous color 31"),
            ColorConfigurable(mod, "@misc_color_32", "#000000", "Miscellaneous color 32"),
            ColorConfigurable(mod, "@misc_color_33", "#000000", "Miscellaneous color 33"),
            ColorConfigurable(mod, "@misc_color_34", "#000000", "Miscellaneous color 34"),
            ColorConfigurable(mod, "@misc_color_35", "#000000", "Miscellaneous color 35"),
            ColorConfigurable(mod, "@misc_color_36", "#000000", "Miscellaneous color 36"),
            ColorConfigurable(mod, "@misc_color_37", "#000000", "Miscellaneous color 37"),
            ColorConfigurable(mod, "@misc_color_38", "#000000", "Miscellaneous color 38"),
            ColorConfigurable(mod, "@misc_color_39", "#000000", "Miscellaneous color 39"),
            ColorConfigurable(mod, "@misc_color_40", "#000000", "Miscellaneous color 40"),
            ColorConfigurable(mod, "@misc_color_41", "#000000", "Miscellaneous color 41"),
            ColorConfigurable(mod, "@misc_color_42", "#000000", "Miscellaneous color 42"),
            ColorConfigurable(mod, "@misc_color_43", "#000000", "Miscellaneous color 43"),
            ColorConfigurable(mod, "@misc_color_44", "#000000", "Miscellaneous color 44"),
            ColorConfigurable(mod, "@misc_color_45", "#000000", "Miscellaneous color 45"),
            ColorConfigurable(mod, "@misc_color_46", "#000000", "Miscellaneous color 46"),
            ColorConfigurable(mod, "@misc_color_47", "#000000", "Miscellaneous color 47"),
            ColorConfigurable(mod, "@misc_color_48", "#000000", "Miscellaneous color 48"),
            ColorConfigurable(mod, "@misc_color_49", "#000000", "Miscellaneous color 49"),
            ColorConfigurable(mod, "@misc_color_50", "#000000", "Miscellaneous color 50"),
            ColorConfigurable(mod, "@misc_color_51", "#000000", "Miscellaneous color 51"),
            ColorConfigurable(mod, "@misc_color_52", "#000000", "Miscellaneous color 52"),
            ColorConfigurable(mod, "@misc_color_53", "#000000", "Miscellaneous color 53"),
            ColorConfigurable(mod, "@misc_color_54", "#000000", "Miscellaneous color 54"),
            ColorConfigurable(mod, "@misc_color_55", "#000000", "Miscellaneous color 55"),
            ColorConfigurable(mod, "@misc_color_56", "#000000", "Miscellaneous color 56"),
            ColorConfigurable(mod, "@misc_color_57", "#000000", "Miscellaneous color 57"),
            ColorConfigurable(mod, "@misc_color_58", "#000000", "Miscellaneous color 58"),
            ColorConfigurable(mod, "@misc_color_59", "#000000", "Miscellaneous color 59"),
        ]
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
        with open(os.path.join(PATH_BASEMOD, "themes", "qssfiles", self.themefiles[self.styleindex.value]) + ".txt") as f:
            newtext = f.read()
            self.currentstyle = newtext
            for i in self.colors:
                newtext = newtext.replace(i.name, i.value.name())
            self.mod.manager.application.setStyleSheet(newtext)
            #print("Applied " + self.themefiles[self.styleindex.value])
            #print(newtext)

    def open_palette(self, file):
        self.multiple = True
        with open(file) as f:
            for i, v in enumerate(f.readlines()):
                self.colors[i].update_value(QColor.fromString(v.replace("\n", "")))
        self.multiple = False
        self.theme_reenable()

    def theme_disable(self):
        self.mod.manager.application.setStyleSheet("")

    def palette_change(self):
        self.open_palette(os.path.join(PATH_BASEMOD, "themes", "palettes", self.palettefiles[self.stylepalette.value]) + ".txt")
