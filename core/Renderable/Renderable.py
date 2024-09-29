from PySide6.QtCore import QPointF
from core.Modify.baseModule import Module
from core.Modify.Editor import Editor
from abc import abstractmethod, ABC


class Renderable(ABC):
    from widgets import Viewport

    def __init__(self, mod, depth: int):
        from core.Modify.Mod import Mod
        from core.Manager import Manager
        self.mod: Mod = mod
        self.depth: int = -depth
        self.manager: Manager = mod.manager
        self.pos: QPointF = QPointF()
        self.offset: QPointF = QPointF()

    def add_myself(self, where: Module | Editor):
        if isinstance(where, Module):
            where.add_renderable(self)
        elif isinstance(where, Editor):
            where.add_renderable(self)
        return self

    @abstractmethod
    def init_graphics(self, viewport: Viewport):
        pass

    @abstractmethod
    def remove_graphics(self):
        pass

    @abstractmethod
    def zoom_event(self, zoom):
        pass

    def move_event(self, pos):
        self.pos = pos

    def setPos(self, pos):
        self.offset = pos

    @property
    def actual_offset(self):
        return self.pos + self.offset * self.zoom

    @property
    def zoom(self):
        return self.manager.viewport.zoom

    def level_resized(self):
        pass
