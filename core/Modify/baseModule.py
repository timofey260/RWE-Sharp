from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from core.Renderable.Renderable import Renderable
    from widgets.Viewport import ViewPort


class Module(ABC):
    """
    Module for passive editor and viewport work
    """
    def __init__(self, mod):
        self.mod = mod
        self.manager = mod.manager
        self.renderables: list[Renderable] = []
        self.viewport: ViewPort = mod.manager.viewport

    @abstractmethod
    def render_module(self):
        """
        Called when user asks for viewport cleanup
        Also called when booting up rwe#
        :return: None
        """
        pass

    def level_resized(self):
        """
        Called once level is resized
        """
        for i in self.renderables:
            i.level_resized()

    def add_renderable(self, renderable: Renderable):
        self.renderables.append(renderable)

    def add_myself(self, viewport: ViewPort, name=None):
        viewport.add_module(self)
        if name is not None:
            viewport.modulenames[name] = self
        return self

    def zoom_event(self, zoom):
        for i in self.renderables:
            i.zoom_event(zoom)

    def move_event(self, pos):
        for i in self.renderables:
            i.move_event(pos)

    @property
    def basemod(self):
        return self.manager.basemod

    @property
    def level(self):
        return self.viewport.level
