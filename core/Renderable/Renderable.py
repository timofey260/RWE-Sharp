from PySide6.QtWidgets import QGraphicsItem
from core.Modify.baseModule import Module
from core.Modify.EditorMode import EditorMode


class Renderable:
    from widgets import Viewport

    def __init__(self, mod, depth: int):
        from core.Modify.Mod import Mod
        from core.Manager import Manager
        self.mod: Mod = mod
        self.depth: int = -depth
        self.manager: Manager = mod.manager

    def add_myself(self, where: Module | EditorMode):
        if isinstance(where, Module):
            where.add_renderable(self)
        elif isinstance(where, EditorMode):
            where.add_renderable(self)
        return self

    def init_graphics(self, viewport: Viewport):
        raise NotImplementedError("Abstract method should be overridden")

    def remove_graphics(self):
        raise NotImplementedError("Abstract method should be overridden")

    def zoom_event(self, zoom):
        raise NotImplementedError("Abstract method should be overridden")

    def move_event(self, pos):
        raise NotImplementedError("Abstract method should be overridden")
