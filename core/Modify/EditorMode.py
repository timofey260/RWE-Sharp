from widgets.Viewport import ViewPort
from PySide6.QtGui import QMoveEvent, QMouseEvent, QWheelEvent
from PySide6.QtCore import QPoint, QPointF, QEvent
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
        self.mpos: QPoint = QPoint()

    def init_scene_items(self):
        """
        Called when editor is changed, should add drawables to scene
        :return:
        """

    def mouse_move_event(self, event: QMoveEvent):
        self.mpos = event.pos()

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
    def mouse_left(self):
        return self.viewport.mouse_left

    @property
    def mouse_right(self):
        return self.viewport.mouse_right

    @property
    def mousepos(self) -> QPoint:
        pos = QPoint(
            round((self.mpos.x() + self.viewport.horizontalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5) * CELLSIZE,
            round((self.mpos.y() + self.viewport.verticalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5) * CELLSIZE
        )
        return pos

    @property
    def viewportcell(self) -> QPoint:
        pos = QPoint(
            round((self.mpos.x() + self.viewport.horizontalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5),
            round((self.mpos.y() + self.viewport.verticalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5)
        )
        return pos
