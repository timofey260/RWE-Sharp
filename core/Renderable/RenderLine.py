from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF, QLine
from PySide6.QtWidgets import QGraphicsLineItem
from PySide6.QtGui import QColor, QPen, QBrush
from widgets import Viewport


class RenderLine(Renderable):
    def __init__(self, module, depth, line: QLine, pen=QPen(Qt.GlobalColor.red)):
        super().__init__(module, depth)
        self.line = line
        self.drawline = QGraphicsLineItem(line)
        self.pen = QPen(pen)
        self.drawline.setZValue(self.depth)
        self.drawline.setPen(self.pen)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.viewport.workscene.addItem(self.drawline)
        # self.drawline.setBrush(self.brush)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawline)

    def move_event(self, pos):
        super().move_event(pos)
        self.drawline.setPos(self.actual_offset)

    def zoom_event(self, zoom):
        self.drawline.setScale(zoom * self.scale)

    def setLine(self, line: QLine):
        self.drawline.setLine(line)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawline.setPos(self.actual_offset)
