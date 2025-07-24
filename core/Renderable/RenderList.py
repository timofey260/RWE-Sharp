from PySide6.QtWidgets import QGraphicsItem
from core.Renderable.Renderable import Renderable
from PySide6.QtCore import QPointF


class RenderList(Renderable):
    """
    some easy way to have multiple Renderables or QGraphicsItems in one class
    without having to worry about them getting added
    """
    def __init__(self, module, depth, add_renderable: bool = True):
        super().__init__(module, depth, False)
        self.graphicsitems: list[QGraphicsItem] = []
        self.renderables: list[Renderable] = []
        if add_renderable:
            self.module.add_renderable(self)

    def assign_depth(self):
        for i in self.graphicsitems:
            i.setZValue(self.depth)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        for i in self.graphicsitems:
            viewport.workscene.addItem(i)
        # for i in self.renderables:
        #     i.init_graphics(viewport)

    def remove_graphics(self, viewport):
        for i in self.graphicsitems:
            viewport.workscene.removeItem(i)
        for i in self.renderables:
            i.remove_graphics(viewport)
        super().remove_graphics(viewport)

    def remove_myself(self):
        for i in self.graphicsitems:
            self.viewport.workscene.removeItem(i)
        for i in self.renderables:
            i.remove_myself()
        super().remove_myself()

    def move_event(self):
        super().move_event()
        for i in self.graphicsitems:
            i.setPos(self.actual_offset)

    def zoom_event(self):
        for i in self.graphicsitems:
            i.setScale(self.zoom * self.scale)

    def setPos(self, pos: QPointF):
        super().setPos(pos)
        for i in self.graphicsitems:
            i.setPos(self.actual_offset)
        for i in self.renderables:
            i.setPos(self.offset)

    def setOpacity(self, opacity):
        super().setOpacity(opacity)
        for i in self.renderables:
            i.setOpacity(self.opacity)
        for i in self.graphicsitems:
            i.setOpacity(self.opacity)
