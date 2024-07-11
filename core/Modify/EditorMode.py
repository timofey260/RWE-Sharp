from __future__ import annotations
from PySide6.QtGui import QMoveEvent, QMouseEvent, QWheelEvent
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QGraphicsScene
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from core.Renderable.Renderable import Renderable


class EditorMode:
    """
    Base for creating custom viewport editors
    """
    def __init__(self, mod):
        """
        :param mod: Mod
        """
        from core.Manager import Manager
        from core.Modify.Mod import Mod
        from widgets.Viewport import ViewPort
        self.mod: mod = mod
        self.manager: Manager = mod.manager
        self.renderables: list[Renderable] = []
        self.viewport: ViewPort = mod.manager.viewport

    def init_scene_items(self):
        """
        Called when editor is changed, should add drawables to scene
        :return:
        """

    def mouse_move_event(self, event: QMoveEvent):
        pass

    def mouse_press_event(self, event: QMouseEvent):
        pass

    def mouse_release_event(self, event: QMouseEvent):
        pass

    def mouse_wheel_event(self, event: QWheelEvent):
        pass

    def zoom_event(self, zoom):
        for i in self.renderables:
            i.zoom_event(zoom)

    def move_event(self, pos):
        for i in self.renderables:
            i.move_event(pos)

    def remove_items_from_scene(self):
        """
        Called when editor is changed, should remove anything it doesn't need
        :return: None
        """
        for i in self.renderables:
            i.remove_graphics()

    def add_renderable(self, renderable: Renderable):
        self.renderables.append(renderable)

    @property
    def workscene(self) -> QGraphicsScene:
        return self.viewport.workscene

    @property
    def mouse_left(self) -> bool:
        return self.viewport.mouse_left

    @property
    def mouse_right(self) -> bool:
        return self.viewport.mouse_right

    @property
    def mouse_pos(self) -> QPoint:
        return self.viewport.mouse_pos

    def add_myself(self, ui):
        self.mod.add_editor(self, ui)
        return self
