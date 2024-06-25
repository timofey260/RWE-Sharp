from PySide6.QtCore import QPoint, Qt
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsEllipseItem


class TilePreview(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.workscene = QGraphicsScene(0, 0, 0, 0)
        self.setScene(self.workscene)
        self.origin = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.tileimage = self.workscene.addPixmap(QPixmap())
        self.lastpos = QPoint()
        self.manager = None
        self.setMouseTracking(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.zoom = 1

    def add_manager(self, manager):
        self.manager = manager

    def mouseMoveEvent(self, event):
        offset = event.pos() - self.lastpos
        if event.buttons() & Qt.MouseButton.AllButtons:
            self.tileimage.setPos(self.tileimage.pos() + offset)
        self.lastpos = event.pos()

    def mousePressEvent(self, event):
        self.setCursor(Qt.CursorShape.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def wheelEvent(self, event):
        self.zoom = max(0.01, self.zoom + (event.angleDelta().y() * (-1 if event.inverted() else 1) / 800))
        self.tileimage.setScale(self.zoom)
