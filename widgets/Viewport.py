from PySide6.QtGui import QPen, QColor, QPixmap
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtCore import QAbstractNativeEventFilter

class ViewPort(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.workscene = QGraphicsScene(self)
        self.pen = QPen(QColor(0, 255, 255, 255))
        self.pen.setWidth(20)
        self.setScene(self.workscene)
        self.pixmap = QPixmap()
        self.pixmap.load("resources\\icon.png")
        map = self.workscene.addPixmap(self.pixmap)
        map.setPos(500, 0)
        map.setOffset(200, 0)
        # self.workscene.addLine(0, 0, 20, 20, self.pen)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("thing")
