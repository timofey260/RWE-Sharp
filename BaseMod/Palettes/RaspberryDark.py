from RWESharp.Modify import Palette
from PySide6.QtGui import QPalette, QColor, QBrush
from PySide6.QtCore import Qt


class RaspberryDark(Palette):
    def __init__(self, mod):
        super().__init__("Raspberry Dark", mod)
        brush = QBrush(QColor(60, 60, 60, 255))
        brush.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush2 = QBrush(QColor(90, 90, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(30, 30, 30, 255))
        brush3.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(40, 40, 40, 255))
        brush4.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        brush5 = QBrush(QColor(45, 45, 45, 255))
        brush5.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        self.palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush6 = QBrush(QColor(255, 0, 53, 255))
        brush6.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        brush7 = QBrush(QColor(255, 0, 35, 255))
        brush7.setStyle(Qt.SolidPattern)
        self.palette.setBrush(QPalette.Active, QPalette.Link, brush7)
        self.palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush)
        self.palette.setBrush(QPalette.Active, QPalette.Accent, brush6)
        self.palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        self.palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        self.palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush)
