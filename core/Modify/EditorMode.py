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
        self.mod = mod
        self.manager = mod.manager
        self.viewport = mod.manager.viewport
        self.mpos = QPoint()
        self._ml = False
        self._mr = False

    def init_scene_items(self):
        """
        Called when editor is changed, should add drawables to scene
        :return:
        """

    def mouse_move_event(self, event: QMoveEvent):
        self.mpos = event.pos()

    def mouse_click_event(self, event: QMouseEvent):
        print(event.buttons())

    def mouse_wheel_event(self, event: QWheelEvent):
        pass

    def remove_items_from_scene(self):
        """
        Called when editor is changed, should remove anything it doesn't need
        :return: None
        """

    @property
    def mouse_left(self):
        return

    @property
    def mousepos(self) -> QPoint:
        pos = QPoint(
            round((self.mpos.x() + self.viewport.horizontalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5) * CELLSIZE,
            round((self.mpos.y() + self.viewport.verticalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5) * CELLSIZE
        )
        return pos