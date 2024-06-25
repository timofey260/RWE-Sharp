from PySide6.QtCore import QPoint, Qt, QPointF
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from RWESharp.Core import CELLSIZE


class TilePreview(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.workscene = QGraphicsScene(self)
        self.setScene(self.workscene)
        # self.origin = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.topleft = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.tileimage = self.workscene.addPixmap(QPixmap())
        self.lastpos = QPoint()
        self.mouse_pos = QPoint()
        self.manager = None
        self.setMouseTracking(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.zoom = 1

    def add_manager(self, manager):
        self.manager = manager
        self.workscene.setSceneRect(0, 0, 1000, 1000)

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.pos()
        offset = event.pos() - self.lastpos
        if event.buttons() & Qt.MouseButton.AllButtons:
            self.topleft.setPos(self.topleft.pos() + offset)
            self.tileimage.setPos(self.topleft.pos())
        self.lastpos = event.pos()

    def mousePressEvent(self, event):
        self.setCursor(Qt.CursorShape.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def wheelEvent(self, event):
        pointbefore = self.viewport_to_editor_float(self.mouse_pos.toPointF())
        self.zoom = max(0.01, self.zoom + (event.angleDelta().y() * (-1 if event.inverted() else 1) / 800))
        self.tileimage.setScale(self.zoom)
        offset = (self.viewport_to_editor_float(self.mouse_pos.toPointF()) - pointbefore) * CELLSIZE * self.zoom
        self.topleft.setPos(self.topleft.pos() + offset)
        self.tileimage.setPos(self.topleft.pos())

    def viewport_to_editor_float(self, point: QPointF) -> QPointF:
        npoint = point + QPointF(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.tileimage.pos()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        return npoint

