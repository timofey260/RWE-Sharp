from RWESharp.Modify import Palette
from PySide6.QtGui import QPalette, QColor, QBrush
from PySide6.QtCore import Qt


class RaspberryDark(Palette):
    def __init__(self, mod):
        super().__init__("Raspberry Dark", mod)
        brush = QBrush(QColor(60, 60, 60, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush1)
        brush2 = QBrush(QColor(90, 90, 90, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Midlight, brush2)
        brush3 = QBrush(QColor(30, 30, 30, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Dark, brush3)
        brush4 = QBrush(QColor(40, 40, 40, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Mid, brush4)
        brush5 = QBrush(QColor(45, 45, 45, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush5)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush3)
        brush6 = QBrush(QColor(255, 0, 53, 255))
        brush6.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush6)
        brush7 = QBrush(QColor(255, 0, 35, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Link, brush7)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ToolTipBase, brush)
        self.palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Accent, brush6)
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, QBrush(QColor(30, 30, 30, 255)))
        self.palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ToolTipBase, brush)
