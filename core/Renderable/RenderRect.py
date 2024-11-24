from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderRect(Renderable):
    def __init__(self, mod, depth, rect: QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(mod, depth)
        self.rect = rect
        self.drawrect: None | QGraphicsRectItem = None
        self.pen = QPen(pen)
        self.brush = QBrush(brush)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.drawrect = viewport.workscene.addRect(self.rect)
        self.drawrect.setZValue(self.depth)
        self.drawrect.setPen(self.pen)
        self.drawrect.setBrush(self.brush)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        self.drawrect.removeFromIndex()
        self.drawrect = None

    def move_event(self, pos):
        super().move_event(pos)
        self.drawrect.setPos(self.actual_offset)

    def zoom_event(self, zoom):
        self.drawrect.setScale(zoom)

    def setRect(self, rect: QRect):
        self.rect = rect
        self.drawrect.setRect(rect)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawrect.setPos(self.actual_offset)
