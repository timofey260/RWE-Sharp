from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPen, QColor
from PySide6.QtCore import Signal, Qt
from ui.uiscripts.PenPicker import Ui_Penpicker

list2penstyle = [
    Qt.PenStyle.SolidLine,
    Qt.PenStyle.NoPen,
    Qt.PenStyle.DashLine,
    Qt.PenStyle.DotLine,
    Qt.PenStyle.DashDotLine,
    Qt.PenStyle.DashDotDotLine,
]


class PenPicker(QWidget):
    penChanged = Signal(QPen)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Penpicker()
        self.ui.setupUi(self)
        self.pen = QPen()
        self.set_pen(QPen(QColor(0, 0, 0), 2))
        self.ui.Color.colorPicked.connect(self.update_pen)
        self.ui.Width.valueChanged.connect(self.update_pen)
        self.ui.Style.currentIndexChanged.connect(self.update_pen)

    def update_pen(self):
        self.pen.setColor(self.ui.Color.color)
        self.pen.setStyle(list2penstyle[self.ui.Style.currentIndex()])
        self.pen.setWidthF(self.ui.Width.value())
        self.penChanged.emit(self.pen)

    def set_pen(self, pen: QPen):
        if pen == self.pen:
            return
        self.pen = pen.__copy__()  # NOQA it does return something but for some reason it says that it returns none
        self.ui.Color.set_color(pen.color())
        self.ui.Width.setValue(pen.widthF())
        self.ui.Style.setCurrentIndex(list2penstyle.index(pen.style()))
        self.penChanged.emit(self.pen)
