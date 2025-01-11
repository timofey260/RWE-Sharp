from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF
from PySide6.QtWidgets import QGraphicsEllipseItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderEllipse(Renderable):
    def __init__(self, module, depth, rect: QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(module, depth)
        self.rect = rect
        self.drawellipse = QGraphicsEllipseItem(self.rect)
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.drawellipse.setZValue(self.depth)
        self.drawellipse.setPen(self.pen)
        self.drawellipse.setBrush(self.brush)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.drawellipse)
        self.setRect(self.rect)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawellipse)

    def move_event(self):
        super().move_event()
        self.drawellipse.setPos(self.actual_offset)

    def zoom_event(self):
        self.drawellipse.setScale(self.zoom * self.scale)

    def setRect(self, rect: QRect):
        self.rect = rect
        self.drawellipse.setRect(rect)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawellipse.setPos(self.actual_offset)
