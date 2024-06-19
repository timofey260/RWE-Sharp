from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt
from PySide6.QtWidgets import QGraphicsRectItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderRect(Renderable):
    def __init__(self, module, depth, rect: QRect, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(module, depth)
        self.rect = rect
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

    def move_event(self, pos):
        self.drawrect.setPos(pos)

    def zoom_event(self, zoom):
        self.drawrect.setScale(zoom)
