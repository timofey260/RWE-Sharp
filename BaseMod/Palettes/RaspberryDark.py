from RWESharp.Modify import Palette
from PySide6.QtGui import QPalette, QColor


class RaspberryDark(Palette):
    def __init__(self, mod):
        super().__init__("Raspberry Dark", mod)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, QColor.fromString("#DADADA"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, QColor.fromString("#FFFFFF2A"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor.fromString("#6D6D6D"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, QColor.fromString("#3D3D3D"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, QColor.fromString("#2b2b2b"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, QColor.fromString("#717171"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, QColor.fromString("#4C4C4C"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, QColor.fromString("#343434"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, QColor.fromString("#737373"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, QColor.fromString("#454545"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Midlight, QColor.fromString("#363636"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Midlight, QColor.fromString("#656565"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, QColor.fromString("#363636"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Dark, QColor.fromString("#222222"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Dark, QColor.fromString("#434343"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, QColor.fromString("#454545"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Mid, QColor.fromString("#3b3b3b"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Mid, QColor.fromString("#525252"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, QColor.fromString("#dadada"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, QColor.fromString("#b6b6b6"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor.fromString("#353535"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.BrightText, QColor.fromString("#FFFFFF"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.BrightText, QColor.fromString("#FFFFFF"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.BrightText, QColor.fromString("#FFFFFF"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, QColor.fromString("#dadada"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, QColor.fromString("#b6b6b6"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor.fromString("#2b2b2b"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, QColor.fromString("#3d3d3d"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, QColor.fromString("#2c2c2c"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, QColor.fromString("#585858"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, QColor.fromString("#3d3d3d"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, QColor.fromString("#333333"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, QColor.fromString("#494949"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Shadow, QColor.fromString("#030303"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Shadow, QColor.fromString("#030303"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Shadow, QColor.fromString("#030303"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, QColor.fromString("#dc1438"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, QColor.fromString("#a20c27"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor.fromString("#e03352"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, QColor.fromString("#ffffff"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.HighlightedText, QColor.fromString("#ffffff"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor.fromString("#dadada"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Link, QColor.fromString("#308cc6"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Link, QColor.fromString("#308cc6"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Link, QColor.fromString("#308cc6"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.LinkVisited, QColor.fromString("#ff00ff"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.LinkVisited, QColor.fromString("#ff00ff"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.LinkVisited, QColor.fromString("#ff00ff"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.AlternateBase, QColor.fromString("#393939"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.AlternateBase, QColor.fromString("#282828"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.AlternateBase, QColor.fromString("#308cc6"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, QColor.fromString("#ffffdc"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, QColor.fromString("#ffffdc"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipBase, QColor.fromString("#ffffdc"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipText, QColor.fromString("#000000"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipText, QColor.fromString("#000000"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ToolTipText, QColor.fromString("#000000"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, QColor.fromString("#767676"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, QColor.fromString("#767676"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, QColor.fromString("#767676"))

        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, QColor.fromString("#308cc6"))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Accent, QColor.fromString("#308cc6"))
        self.palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Accent, QColor.fromString("#919191"))




