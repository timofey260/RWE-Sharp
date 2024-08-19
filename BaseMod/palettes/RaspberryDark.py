from PySide6.QtGui import QColor

from RWESharp.Modify import Theme
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import PATH_BASEMOD
import re
import os

from core.configTypes.QtTypes import ColorConfigurable


class RaspberryDark(Theme):
    def __init__(self, mod):
        from BaseMod.palettes.paletteuiconnector import RPDarkUI
        super().__init__("Raspberry Dark", mod)
        self.styleindex = IntConfigurable(mod, "rpdark.styleoption", 0, description="Style file")
        self.styleindex.valueChanged.connect(self.palette_enable)
        self.stylepalette = IntConfigurable(mod, "rpdark.stylepalette", 0, description="Style palette")
        self.stylepalette.valueChanged.connect(self.palette_enable)
        self.themefiles = ["circular", "sharp", "atmoled", "darkeum"]
        self.settings = RPDarkUI(self)

        self.colors = [
            # base colors
            ColorConfigurable(mod, "@base_dark", QColor.fromString("#000000"), "Base dark color"),
            ColorConfigurable(mod, "@base_medium", QColor.fromString("#333333"), "Base medium color"),
            ColorConfigurable(mod, "@base_light", QColor.fromString("#666666"), "Base light color"),


            # border colors
            ColorConfigurable(mod, "@border_dark", QColor.fromString("#000000"), "Border dark color"),
            ColorConfigurable(mod, "@border_medium", QColor.fromString("#333333"), "Border medium color"),
            ColorConfigurable(mod, "@border_light", QColor.fromString("#666666"), "Border light color"),
            # text colors
            ColorConfigurable(mod, "@text_dark", QColor.fromString("#000000"), "Text dark color"),
            ColorConfigurable(mod, "@text_medium", QColor.fromString("#333333"), "Text medium color"),
            ColorConfigurable(mod, "@text_light", QColor.fromString("#666666"), "Text light color"),
            ColorConfigurable(mod, "@text_disabled", QColor.fromString("#999999"), "Text disabled color"),
            ColorConfigurable(mod, "@text_enabled", QColor.fromString("#FFFFFF"), "Text enabled color"),
            # accent colors
            ColorConfigurable(mod, "@accent_light", QColor.fromString("#4fa08b"), "Accent light color"),
            ColorConfigurable(mod, "@accent_medium", QColor.fromString("#4fa08b"), "Accent medium color"),
            ColorConfigurable(mod, "@accent_dark", QColor.fromString("#316558"), "Accent dark color"),

            # alternative colors
            ColorConfigurable(mod, "@alt_base_dark", QColor.fromString("#0A0A0A"), "Alternative base dark color"),
            ColorConfigurable(mod, "@alt_base_medium", QColor.fromString("#3A3A3A"), "Alternative base medium color"),
            ColorConfigurable(mod, "@alt_base_light", QColor.fromString("#6A6A6A"), "Alternative base light color"),
            ColorConfigurable(mod, "@alt_text_misc", QColor.fromString("#9A9A9A"),"Alternative miscellaneous text color"),
            ColorConfigurable(mod, "@alt_border_dark", QColor.fromString("#0A0A0A"), "Alternative border dark color"),
            ColorConfigurable(mod, "@alt_border_medium", QColor.fromString("#3A3A3A"),"Alternative border medium color"),
            ColorConfigurable(mod, "@alt_border_light", QColor.fromString("#6A6A6A"), "Alternative border light color"),
            ColorConfigurable(mod, "@alt_text_dark", QColor.fromString("#0A0A0A"), "Alternative text dark color"),
            ColorConfigurable(mod, "@alt_text_medium", QColor.fromString("#3A3A3A"), "Alternative text medium color"),
            ColorConfigurable(mod, "@alt_text_light", QColor.fromString("#6A6A6A"), "Alternative text light color"),
            ColorConfigurable(mod, "@alt_text_disabled", QColor.fromString("#9A9A9A"), "Alternative text disabled color"),
            ColorConfigurable(mod, "@alt_text_enabled", QColor.fromString("#FAFAFA"), "Alternative text enabled color"),
            ColorConfigurable(mod, "@alt_accent_light", QColor.fromString("#FFAAAA"), "Alternative accent light color"),
            ColorConfigurable(mod, "@alt_accent_medium", QColor.fromString("#FF5555"),  "Alternative accent medium color"),
            ColorConfigurable(mod, "@alt_accent_dark", QColor.fromString("#AA0000"), "Alternative accent dark color"),
            # misc colors
            ColorConfigurable(mod, "@misc_color_30", QColor.fromString("#123456"), "Miscellaneous color 30"),
            ColorConfigurable(mod, "@misc_color_31", QColor.fromString("#654321"), "Miscellaneous color 31"),
            ColorConfigurable(mod, "@misc_color_32", QColor.fromString("#abcdef"), "Miscellaneous color 32"),
            ColorConfigurable(mod, "@misc_color_33", QColor.fromString("#fedcba"), "Miscellaneous color 33"),
            ColorConfigurable(mod, "@misc_color_34", QColor.fromString("#112233"), "Miscellaneous color 34"),
            ColorConfigurable(mod, "@misc_color_35", QColor.fromString("#334455"), "Miscellaneous color 35"),
            ColorConfigurable(mod, "@misc_color_36", QColor.fromString("#556677"), "Miscellaneous color 36"),
            ColorConfigurable(mod, "@misc_color_37", QColor.fromString("#778899"), "Miscellaneous color 37"),
            ColorConfigurable(mod, "@misc_color_38", QColor.fromString("#99aabb"), "Miscellaneous color 38"),
            ColorConfigurable(mod, "@misc_color_39", QColor.fromString("#bbaacc"), "Miscellaneous color 39"),
            ColorConfigurable(mod, "@misc_color_40", QColor.fromString("#ccbbdd"), "Miscellaneous color 40"),
            ColorConfigurable(mod, "@misc_color_41", QColor.fromString("#ddeeff"), "Miscellaneous color 41"),
            ColorConfigurable(mod, "@misc_color_42", QColor.fromString("#ffccaa"), "Miscellaneous color 42"),
            ColorConfigurable(mod, "@misc_color_43", QColor.fromString("#aabbcc"), "Miscellaneous color 43"),
            ColorConfigurable(mod, "@misc_color_44", QColor.fromString("#cceeff"), "Miscellaneous color 44"),
            ColorConfigurable(mod, "@misc_color_45", QColor.fromString("#ffaaee"), "Miscellaneous color 45"),
            ColorConfigurable(mod, "@misc_color_46", QColor.fromString("#bbccdd"), "Miscellaneous color 46"),
            ColorConfigurable(mod, "@misc_color_47", QColor.fromString("#ccddee"), "Miscellaneous color 47"),
            ColorConfigurable(mod, "@misc_color_48", QColor.fromString("#ddeeff"), "Miscellaneous color 48"),
            ColorConfigurable(mod, "@misc_color_49", QColor.fromString("#eeffaa"), "Miscellaneous color 49"),
            ColorConfigurable(mod, "@misc_color_50", QColor.fromString("#ffddaa"), "Miscellaneous color 50"),
            ColorConfigurable(mod, "@misc_color_51", QColor.fromString("#ffddee"), "Miscellaneous color 51"),
            ColorConfigurable(mod, "@misc_color_52", QColor.fromString("#aaffdd"), "Miscellaneous color 52"),
            ColorConfigurable(mod, "@misc_color_53", QColor.fromString("#bbddff"), "Miscellaneous color 53"),
            ColorConfigurable(mod, "@misc_color_54", QColor.fromString("#ccffee"), "Miscellaneous color 54"),
            ColorConfigurable(mod, "@misc_color_55", QColor.fromString("#ddffee"), "Miscellaneous color 55"),
            ColorConfigurable(mod, "@misc_color_56", QColor.fromString("#aaddff"), "Miscellaneous color 56"),
            ColorConfigurable(mod, "@misc_color_57", QColor.fromString("#bbeeaa"), "Miscellaneous color 57"),
            ColorConfigurable(mod, "@misc_color_58", QColor.fromString("#ccbbaa"), "Miscellaneous color 58"),
            ColorConfigurable(mod, "@misc_color_59", QColor.fromString("#ddccbb"), "Miscellaneous color 59"),
        ]
    def palette_enable(self):
        with open(os.path.join(PATH_BASEMOD, "palettes", "qssfiles", self.themefiles[self.styleindex.value]) + ".txt") as f:
            newtext = f.read()
            for i in self.colors:
                newtext = newtext.replace(i.name, i.value.name())
            self.mod.manager.application.setStyleSheet(newtext)

    def palette_disable(self):
        self.mod.manager.application.setStyleSheet()
