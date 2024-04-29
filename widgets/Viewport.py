from PySide6.QtGui import QPen, QColor, QPixmap, QPainter
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
        self.painter.setBrush(self.foregroundBrush())
        #self.painter.drawLine(0, 0, 200, 200)
        self.map = self.workscene.addPixmap(self.pixmap)
        self.map.setPos(200, 0)
        self.map.setScale(.2)
        # self.workscene.addLine(0, 0, 20, 20, self.pen)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("thing")

    def wheelEvent(self, event):
        print(self.map.scale() + (event.angleDelta().y() / 80))
        self.map.setScale(max(.2, self.map.scale() + (event.angleDelta().y() / 80)))

    def fullrender(self):
        pass
