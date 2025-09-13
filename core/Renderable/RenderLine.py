from core.Renderable.Renderable import Renderable
from PySide6.QtCore import Qt, QPointF, QLine, QLineF
from PySide6.QtWidgets import QGraphicsLineItem
from PySide6.QtGui import QPen


class RenderLine(Renderable):
    def __init__(self, module, depth, line: QLine | QLineF, pen=QPen(Qt.GlobalColor.red), add_renderable: bool = True):
        super().__init__(module, depth, False)
        self.line = line
        self.drawline = QGraphicsLineItem(line)
        self.pen = QPen(pen)
        self.drawline.setZValue(self.depth)
        self.drawline.setPen(self.pen)
        if add_renderable:
            self.module.add_renderable(self)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.viewport.workscene.addItem(self.drawline)
        self.setLine(self.line)
        # self.drawline.setBrush(self.brush)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawline)

    def move_event(self):
        super().move_event()
        self.drawline.setPos(self.actual_offset)

    def zoom_event(self):
        self.drawline.setScale(self.zoom * self.scale)

    def setLine(self, line: QLineF | QLine):
        self.drawline.setLine(line)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawline.setPos(self.actual_offset)

    def setOpacity(self, opacity):
        super().setOpacity(opacity)
        self.drawline.setOpacity(self.opacity)
