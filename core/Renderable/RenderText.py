from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QRect, Qt, QPointF, QRectF
from PySide6.QtWidgets import QGraphicsTextItem
from PySide6.QtGui import QColor, QPen, QBrush


class RenderText(Renderable):
    def __init__(self, module, depth, text: str, color: QColor, add_renderable: bool = True):
        super().__init__(module, depth, False)
        self.text = text
        self.drawtext = QGraphicsTextItem(self.text)
        self.color = color
        self.drawtext.setZValue(self.depth)
        self.drawtext.setDefaultTextColor(color)
        if add_renderable:
            module.add_renderable(self)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        viewport.workscene.addItem(self.drawtext)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.drawtext)

    def move_event(self):
        super().move_event()
        self.drawtext.setPos(self.actual_offset)

    def zoom_event(self):
        self.drawtext.setScale(self.zoom * self.scale)

    def setOpacity(self, opacity):
        super().setOpacity(opacity)
        self.drawtext.setOpacity(self.opacity)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        self.drawtext.setPos(self.actual_offset)
