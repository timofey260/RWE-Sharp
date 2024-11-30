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
        self.pos: QPointF = QPointF()
        self.offset: QPointF = QPointF()
        self.module: Module = module
        self.viewport: None | ViewPort = None

    def add_myself(self, where: Module):
        if isinstance(where, Module):
            where.add_renderable(self)
        self.module = where
        return self

    def remove_myself(self):
        if self.module is None:
            return
        self.module.renderables.remove(self)

    @abstractmethod
    def init_graphics(self, viewport):
        self.viewport = viewport

    def post_init_graphics(self, viewport):
        pass

    @abstractmethod
    def remove_graphics(self, viewport):
        self.viewport = None

    @abstractmethod
    def zoom_event(self, zoom):
        pass

    def move_event(self, pos):
        if pos is None:
            return
        self.pos = pos

    def setPos(self, pos):
        if pos is None:
            return
        self.offset = pos

    @property
    def actual_offset(self):
        return self.pos + self.offset * self.zoom

    @property
    def zoom(self):
        return self.viewport.zoom

    def level_resized(self):
        pass

    @property
    def manager(self):
        return self.module.manager
