from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderRect(Renderable):
    def __init__(self, mod, depth, rect: QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(mod, depth)
        self.rect = rect
        self.pos = QPointF()
        self.drawrect: None | QGraphicsRectItem = None
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.setPen = None
        self.setBrush = None

    def init_graphics(self, viewport: Viewport):
        self.drawrect = viewport.workscene.addRect(self.rect)
        self.drawrect.setZValue(self.depth)
        self.drawrect.setPen(self.pen)
        self.drawrect.setBrush(self.brush)

    def remove_graphics(self):
        self.drawrect.removeFromIndex()

    def move_event(self, pos):
        self.drawrect.setPos(pos + self.pos)

    def zoom_event(self, zoom):
        self.drawrect.setScale(zoom)

    def setRect(self, rect: QRect):
        self.rect = rect
        self.drawrect.setRect(rect)

    def setPos(self, pos: QPointF):
        self.drawrect.setPos(self.drawrect.pos() - self.pos + pos)
        self.pos = pos
