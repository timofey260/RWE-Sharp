from __future__ import annotations

from PySide6.QtCore import QPoint, Qt, QPointF
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem
from RWESharp.info import CELLSIZE


class SimpleViewport(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.workscene = QGraphicsScene(self)
        self.setScene(self.workscene)
        # self.origin = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.topleft = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.lastpos = QPoint()
        self.mouse_pos = QPoint()
        self.manager = None
        self.setMouseTracking(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.zoom = 1
        self.items: list[QGraphicsItem] = []

    def add_manager(self, manager):
        self.manager = manager
        self.workscene.setSceneRect(0, 0, 1000, 1000)

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.pos()
        offset = event.pos() - self.lastpos
        if event.buttons() & Qt.MouseButton.AllButtons:
            self.set_pos(self.topleft.pos() + offset)
        self.lastpos = event.pos()

    def set_pos(self, pos: QPointF | QPoint | None = None):
        if pos is None:
            pos = self.topleft.pos()
        self.topleft.setPos(pos)
        for i in self.items:
            i.setPos(pos + (i.data(1) if isinstance(i.data(1), (QPoint, QPointF)) else QPoint(0, 0)) * self.zoom * (i.data(3) if isinstance(i.data(3), (int, float)) else 1))

    def set_zoom(self):
        for i in self.items:
            i.setScale(self.zoom * (i.data(2) if isinstance(i.data(2), (int, float)) else 1) + (i.data(0) if isinstance(i.data(0), (int, float)) else 0))

    def ratio1(self):
        self.zoom = 1
        self.topleft.setPos(0, 0)
        self.set_zoom()
        self.set_pos()

    def mousePressEvent(self, event):
        self.setCursor(Qt.CursorShape.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def wheelEvent(self, event):
        pointbefore = self.viewport_to_editor_float(self.mouse_pos.toPointF())
        self.zoom = max(0.01, self.zoom + (event.angleDelta().y() * (-1 if event.inverted() else 1) / 800))
        offset = (self.viewport_to_editor_float(self.mouse_pos.toPointF()) - pointbefore) * CELLSIZE * self.zoom
        self.set_pos(self.topleft.pos() + offset)
        self.set_zoom()

    def viewport_to_editor_float(self, point: QPointF) -> QPointF:
        npoint = point + QPointF(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.topleft.pos()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        return npoint