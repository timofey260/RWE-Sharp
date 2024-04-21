from PySide6.QtGui import QPen, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

class ViewPort(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.workscene = QGraphicsScene(self)
        self.pen = QPen(QColor(0, 255, 255, 255))
        self.pen.setWidth(20)
        self.setScene(self.workscene)
        self.workscene.addLine(0, 0, 20, 20, self.pen)
