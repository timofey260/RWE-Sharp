from PySide6.QtWidgets import QGraphicsItem
from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QPointF


class RenderList(Renderable):
    def __init__(self, module, depth):
        super().__init__(module, depth)
        self.rendered: list[QGraphicsItem] = []

    def assign_depth(self):
        for i in self.rendered:
            i.setZValue(self.depth)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        for i in self.rendered:
            viewport.workscene.addItem(i)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        for i in self.rendered:
            viewport.workscene.removeItem(i)

    def move_event(self):
        super().move_event()
        for i in self.rendered:
            i.setPos(self.actual_offset)

    def zoom_event(self):
        for i in self.rendered:
            i.setScale(self.zoom * self.scale)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        for i in self.rendered:
            i.setPos(self.actual_offset)
