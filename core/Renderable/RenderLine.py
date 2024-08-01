from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF, QLine
from PySide6.QtWidgets import QGraphicsLineItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderLine(Renderable):
    def __init__(self, mod, depth, line: QLine, pen=QPen(Qt.GlobalColor.red), brush=QBrush(Qt.GlobalColor.transparent)):
        super().__init__(mod, depth)
        self.line = line
        self.drawline: None | QGraphicsLineItem = None
        self.pen = QPen(pen)
        self.brush = QBrush(brush)
        self.setPen = None
        self.setBrush = None

    def init_graphics(self, viewport: Viewport):
        self.drawline = viewport.workscene.addLine(self.line)
        self.drawline.setZValue(self.depth)
        self.drawline.setPen(self.pen)
        # self.drawline.setBrush(self.brush)

    def remove_graphics(self):
        super().remove_graphics()
        self.drawline.removeFromIndex()
        self.drawline = None

    def move_event(self, pos):
        super().move_event(pos)
        self.drawline.setPos(self.actual_offset)

    def zoom_event(self, zoom):
        self.drawline.setScale(zoom)

    def setLine(self, line: QLine):
        self.drawline.setLine(line)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawline.setPos(self.actual_offset)
