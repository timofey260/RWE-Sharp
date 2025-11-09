from __future__ import annotations
from PySide6.QtCore import QPointF, QPoint, QRect
from RWESharp.Modify.Module import Module
from abc import abstractmethod, ABC
from typing import TYPE_CHECKING


class Renderable(ABC):
    def __init__(self, module: Module, depth: int, add_renderable: bool = True):
        self.depth: int = -depth
        # self.pos: QPointF = QPointF()
        self.offset: QPointF = QPointF()
        self.scale = 1
        self.opacity = 1
        self.module: Module = module
        self._graphics_initiated = False
        if add_renderable:
            self.module.add_renderable(self)

    def remove_myself(self):
        if self.module is None:
            return
        if self.viewport is not None:
            self.remove_graphics(self.viewport)
        self.module.renderables.remove(self)
        self.module = None

    @abstractmethod
    def init_graphics(self, viewport):
        self._graphics_initiated = True
        self.move_event()

    def post_init_graphics(self, viewport):
        pass

    @abstractmethod
    def remove_graphics(self, viewport):
        self._graphics_initiated = False

    @abstractmethod
    def zoom_event(self):
        pass

    def move_event(self):
        pass

    @property
    def is_initiated_grapgics(self):
        return self._graphics_initiated

    def setPos(self, pos: QPoint | QPointF):
        if pos is None:
            return
        if isinstance(pos, QPoint):
            self.offset = pos.toPointF()
            return
        self.offset = pos

    def setScale(self, scale):
        self.scale = scale
        self.zoom_event()

    def setOpacity(self, opacity):
        self.opacity = opacity

    @property
    def actual_offset(self):
        return self.pos + self.offset * self.zoom

    @property
    def zoom(self) -> float:
        if self.viewport is None:
            return 1
        return self.viewport.zoom

    @property
    def pos(self) -> QPointF:
        if self.viewport is None:
            return QPointF(0, 0)
        return self.viewport.topleft.pos()

    def level_resized(self, rect: QRect):
        pass

    @property
    def manager(self):
        return self.module.manager

    @property
    def viewport(self):
        return self.module.viewport

    @property
    def level(self):
        return self.module.viewport.level
