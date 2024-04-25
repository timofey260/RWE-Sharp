from PySide6.QtGui import QPen, QColor, QPixmap, QPainter, QWheelEvent
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

class ViewPort(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.workscene = QGraphicsScene(self)
        self.pen = QPen(QColor(0, 255, 255, 255))
        self.pen.setWidth(20)
        self.setScene(self.workscene)
        self.pixmap = QPixmap()
        self.pixmap.load("resources\\icon.png")
        self.painter = QPainter(self.pixmap)
        self.painter.drawLine(0, 0, 200, 200)
        map = self.workscene.addPixmap(self.pixmap)
        self.workscene.addPixmap(self.pixmap)
        map.setPos(200, 0)
        map.setScale(.2)
        # self.workscene.addLine(0, 0, 20, 20, self.pen)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("thing")

    def event(self, event):
        if type(event) is QWheelEvent:
            print(event.angleDelta())
        return super().event(event)

    def fullrender(self):
        pass
