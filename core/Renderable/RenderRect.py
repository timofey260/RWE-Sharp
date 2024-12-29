from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderRect(Renderable):
    def __init__(self, module, depth, rect: QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(module, depth)
        self.rect = rect
        self.drawrect = QGraphicsRectItem(self.rect)
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.drawrect.setPen(self.pen)
        self.drawrect.setBrush(self.brush)
        self.drawrect.setZValue(self.depth)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.drawrect)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawrect)

    def move_event(self, pos):
        super().move_event(pos)
        self.drawrect.setPos(self.actual_offset)

    def zoom_event(self, zoom):
        self.drawrect.setScale(zoom * self.scale)

    def setRect(self, rect: QRect):
        self.rect = rect
        self.drawrect.setRect(rect)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawrect.setPos(self.actual_offset)
