from __future__ import annotations
from PySide6.QtCore import QPointF
from core.Modify.baseModule import Module
from core.Modify.Editor import Editor
from abc import abstractmethod, ABC
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from widgets.Viewport import ViewPort


class Renderable(ABC):
    def __init__(self, module: Module, depth: int):
        self.depth: int = -depth
        # self.pos: QPointF = QPointF()
        self.offset: QPointF = QPointF()
        self.scale = 1
        self.module: Module = module
        self.module.add_renderable(self)

    def remove_myself(self):
        if self.module is None:
            return
        self.module.renderables.remove(self)
        self.module = None

    @abstractmethod
    def init_graphics(self, viewport):
        self.move_event()

    def post_init_graphics(self, viewport):
        pass

    @abstractmethod
    def remove_graphics(self, viewport):
        pass

    @abstractmethod
    def zoom_event(self):
        pass

    def move_event(self):
        pass

    def setPos(self, pos):
        if pos is None:
            return
        self.offset = pos

    def setScale(self, scale):
        self.scale = scale
        self.zoom_event(self.zoom)

    @property
    def actual_offset(self):
        return self.pos + self.offset * self.zoom

    @property
    def zoom(self):
        return self.viewport.zoom

    @property
    def pos(self):
        return self.viewport.topleft.pos()

    def level_resized(self):
        pass

    @property
    def manager(self):
        return self.module.manager

    @property
    def viewport(self):
        return self.module.viewport
