from PySide6.QtWidgets import QGraphicsItem


class Renderable:
    from widgets import Viewport

    def __init__(self, module, depth: int):
        from core.Modify.baseModule import Module
        from core.Manager import Manager
        self.module: Module = module
        self.depth: int = -depth
        self.manager: Manager = module.manager

    def add_myself(self):
        self.module.append_layer(self)
        return self

    def init_graphics(self, viewport: Viewport):
        raise NotImplementedError("Abstract method should be overridden")

    def zoom_event(self, zoom):
        raise NotImplementedError("Abstract method should be overridden")

    def move_event(self, pos):
        raise NotImplementedError("Abstract method should be overridden")
