from PySide6.QtGui import QColor
from RWESharp.Modify import Theme
from RWESharp.Configurable import IntConfigurable
from RWESharp.Core import PATH_BASEMOD
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
            ColorConfigurable(mod, "@base_very_dark", QColor.fromString("#050a0e"), "Base color"),
            ColorConfigurable(mod, "@base_dark", QColor.fromString("#151a1e"), "Base dark color"),
            ColorConfigurable(mod, "@base_medium", QColor.fromString("#000000"), "Base medium color"),
            ColorConfigurable(mod, "@base_light", QColor.fromString("#1e1e1e"), "Base light color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@base_very_light", QColor.fromString("#2e2e2e"), "Base very light color"),
            # Placeholder value updated
            # background colors
            ColorConfigurable(mod, "@background_very_dark", QColor.fromString("#000000"), "Background color"),
            ColorConfigurable(mod, "@background_dark", QColor.fromString("#151a1e"), "Background dark color"),
            ColorConfigurable(mod, "@background_medium", QColor.fromString("#1e1e1e"), "Background medium color"),
            ColorConfigurable(mod, "@background_light", QColor.fromString("#2e2e2e"), "Background light color"),
            ColorConfigurable(mod, "@background_very_light", QColor.fromString("#3e3e3e"),
                              "Background very light color"),  # Placeholder value updated
            # border colors
            ColorConfigurable(mod, "@border_dark", QColor.fromString("#2e2e2e"), "Border dark color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@border_medium", QColor.fromString("#3e3e3e"), "Border medium color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@border_light", QColor.fromString("#4e4e4e"), "Border light color"),
            # Placeholder value updated
            # text colors
            ColorConfigurable(mod, "@text_dark", QColor.fromString("#000000"), "Text dark color"),
            ColorConfigurable(mod, "@text_medium", QColor.fromString("#333333"), "Text medium color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@text_light", QColor.fromString("#cccccc"), "Text light color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@text_disabled", QColor.fromString("#666666"), "Text disabled color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@text_enabled", QColor.fromString("#ffffff"), "Text enabled color"),
            # Placeholder value updated
            # accent colors
            ColorConfigurable(mod, "@accent_light", QColor.fromString("#60A996"), "Accent light color"),
            ColorConfigurable(mod, "@accent_medium", QColor.fromString("#F00FFF"), "Accent medium color"),
            ColorConfigurable(mod, "@accent_dark", QColor.fromString("#316558"), "Accent dark color"),
            # alternative colors
            ColorConfigurable(mod, "@alt_base_dark", QColor.fromString("#0A0A0A"), "Alternative base dark color"),
            ColorConfigurable(mod, "@alt_base_medium", QColor.fromString("#1e1e1e"), "Alternative base medium color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_base_light", QColor.fromString("#2e2e2e"), "Alternative base light color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_text_misc", QColor.fromString("#333333"),
                              "Alternative miscellaneous text color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_border_dark", QColor.fromString("#2e2e2e"), "Alternative border dark color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_border_medium", QColor.fromString("#3e3e3e"),
                              "Alternative border medium color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_border_light", QColor.fromString("#4e4e4e"), "Alternative border light color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_text_dark", QColor.fromString("#000000"), "Alternative text dark color"),
            ColorConfigurable(mod, "@alt_text_medium", QColor.fromString("#333333"), "Alternative text medium color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_text_light", QColor.fromString("#cccccc"), "Alternative text light color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_text_disabled", QColor.fromString("#666666"),
                              "Alternative text disabled color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_text_enabled", QColor.fromString("#ffffff"), "Alternative text enabled color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_accent_light", QColor.fromString("#60A996"), "Alternative accent light color"),
            # Placeholder value updated
            ColorConfigurable(mod, "@alt_accent_medium", QColor.fromString("#F00FFF"),
                              "Alternative accent medium color"),  # Placeholder value updated
            ColorConfigurable(mod, "@alt_accent_dark", QColor.fromString("#316558"), "Alternative accent dark color"),
            # Placeholder value updated
            # misc colors
            ColorConfigurable(mod, "@misc_color_30", QColor.fromString("#000000"), "Miscellaneous color 30"),
            ColorConfigurable(mod, "@misc_color_31", QColor.fromString("#000000"), "Miscellaneous color 31"),
            ColorConfigurable(mod, "@misc_color_32", QColor.fromString("#000000"), "Miscellaneous color 32"),
            ColorConfigurable(mod, "@misc_color_33", QColor.fromString("#000000"), "Miscellaneous color 33"),
            ColorConfigurable(mod, "@misc_color_34", QColor.fromString("#000000"), "Miscellaneous color 34"),
            ColorConfigurable(mod, "@misc_color_35", QColor.fromString("#000000"), "Miscellaneous color 35"),
            ColorConfigurable(mod, "@misc_color_36", QColor.fromString("#000000"), "Miscellaneous color 36"),
            ColorConfigurable(mod, "@misc_color_37", QColor.fromString("#000000"), "Miscellaneous color 37"),
            ColorConfigurable(mod, "@misc_color_38", QColor.fromString("#000000"), "Miscellaneous color 38"),
            ColorConfigurable(mod, "@misc_color_39", QColor.fromString("#000000"), "Miscellaneous color 39"),
            ColorConfigurable(mod, "@misc_color_40", QColor.fromString("#000000"), "Miscellaneous color 40"),
            ColorConfigurable(mod, "@misc_color_41", QColor.fromString("#000000"), "Miscellaneous color 41"),
            ColorConfigurable(mod, "@misc_color_42", QColor.fromString("#000000"), "Miscellaneous color 42"),
            ColorConfigurable(mod, "@misc_color_43", QColor.fromString("#000000"), "Miscellaneous color 43"),
            ColorConfigurable(mod, "@misc_color_44", QColor.fromString("#000000"), "Miscellaneous color 44"),
            ColorConfigurable(mod, "@misc_color_45", QColor.fromString("#000000"), "Miscellaneous color 45"),
            ColorConfigurable(mod, "@misc_color_46", QColor.fromString("#000000"), "Miscellaneous color 46"),
            ColorConfigurable(mod, "@misc_color_47", QColor.fromString("#000000"), "Miscellaneous color 47"),
            ColorConfigurable(mod, "@misc_color_48", QColor.fromString("#000000"), "Miscellaneous color 48"),
            ColorConfigurable(mod, "@misc_color_49", QColor.fromString("#000000"), "Miscellaneous color 49"),
            ColorConfigurable(mod, "@misc_color_50", QColor.fromString("#000000"), "Miscellaneous color 50"),
            ColorConfigurable(mod, "@misc_color_51", QColor.fromString("#000000"), "Miscellaneous color 51"),
            ColorConfigurable(mod, "@misc_color_52", QColor.fromString("#000000"), "Miscellaneous color 52"),
            ColorConfigurable(mod, "@misc_color_53", QColor.fromString("#000000"), "Miscellaneous color 53"),
            ColorConfigurable(mod, "@misc_color_54", QColor.fromString("#000000"), "Miscellaneous color 54"),
            ColorConfigurable(mod, "@misc_color_55", QColor.fromString("#000000"), "Miscellaneous color 55"),
            ColorConfigurable(mod, "@misc_color_56", QColor.fromString("#000000"), "Miscellaneous color 56"),
            ColorConfigurable(mod, "@misc_color_57", QColor.fromString("#000000"), "Miscellaneous color 57"),
            ColorConfigurable(mod, "@misc_color_58", QColor.fromString("#000000"), "Miscellaneous color 58"),
            ColorConfigurable(mod, "@misc_color_59", QColor.fromString("#000000"), "Miscellaneous color 59"),
        ]
#penis
    def palette_enable(self):
        with open(os.path.join(PATH_BASEMOD, "palettes", "qssfiles", self.themefiles[self.styleindex.value]) + ".txt") as f:
            newtext = f.read()
            for i in self.colors:
                newtext = newtext.replace(i.name, i.value.name())
            self.mod.manager.application.setStyleSheet(newtext)

    def palette_disable(self):
        self.mod.manager.application.setStyleSheet("")
