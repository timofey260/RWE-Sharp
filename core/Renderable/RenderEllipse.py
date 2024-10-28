from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderEllipse(Renderable):
    def __init__(self, mod, depth, rect: QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(mod, depth)
        self.rect = rect
        self.drawellipse: None | QGraphicsEllipseItem = None
        self.pen = QPen(pen)
        self.brush = QBrush(brush)

    def init_graphics(self):
        self.drawellipse = self.viewport.workscene.addEllipse(self.rect)
        self.drawellipse.setZValue(self.depth)
        self.drawellipse.setPen(self.pen)
        self.drawellipse.setBrush(self.brush)

    def remove_graphics(self):
        super().remove_graphics()
        self.drawellipse.removeFromIndex()
        self.drawellipse = None

    def move_event(self, pos):
        super().move_event(pos)
        self.drawellipse.setPos(self.actual_offset)

    def zoom_event(self, zoom):
        self.drawellipse.setScale(zoom)

    def setRect(self, rect: QRect):
        self.rect = rect
        self.drawellipse.setRect(rect)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawellipse.setPos(self.actual_offset)
