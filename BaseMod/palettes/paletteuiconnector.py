from BaseMod.palettes.paletteui import Ui_Paletteui
from BaseMod.palettes.RaspberryDark import RaspberryDark
from RWESharp.Ui import ThemeUI


class RPDarkUI(ThemeUI):
    def setup_ui(self, viewer):
        self.ui = Ui_Paletteui()
        self.ui.setupUi(viewer)
        self.theme.styleindex.link_combobox(self.ui.Style)
        self.theme.stylepalette.link_combobox(self.ui.Palette)