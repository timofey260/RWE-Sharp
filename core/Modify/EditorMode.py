from widgets.Viewport import ViewPort
from PySide6.QtGui import QMoveEvent, QMouseEvent, QWheelEvent
from PySide6.QtCore import QPoint, QPointF, QEvent
from PySide6.QtWidgets import QGraphicsScene
from core.info import CELLSIZE

class EditorMode:
    """
    Base for creating custom viewport editors
    """
    def __init__(self, mod):
        """
        :param viewport: viewport where actions should be tracked
        """
        from ..Manager import Manager
        from .Mod import Mod
        from widgets.Viewport import ViewPort
        self.mod: mod = mod
        self.manager: Manager = mod.manager
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

    def remove_items_from_scene(self):
        """
        Called when editor is changed, should remove anything it doesn't need
        :return: None
        """

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
    def mpos(self) -> QPoint:
        return self.viewport.mpos

    def add_myself(self, ui):
        self.mod.add_editor(self, ui)
        return self
