from widgets.Viewport import ViewPort
from PySide6.QtGui import QMoveEvent, QMouseEvent, QWheelEvent
from PySide6.QtCore import QPoint, QPointF
from core.info import CELLSIZE

class EditorMode:
    """
    Base for creating custom viewport editors
    """
    def __init__(self, manager):
        """
        :param viewport: viewport where actions should be tracked
        """
        self.manager = manager
        self.viewport = manager.viewport
        self.mpos = QPoint()

    def init_scene_items(self):
        pass

    def mouse_move_event(self, event: QMoveEvent):
        self.mpos = event.pos()

    def mouse_click_event(self, event: QMouseEvent):
        pass

    def mouse_wheel_event(self, event: QWheelEvent):
        pass

    def remove_items_from_scene(self):
        pass

    @property
    def mousepos(self) -> QPoint:
        pos = QPoint(
            round((self.mpos.x() + self.viewport.horizontalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5) * CELLSIZE,
            round((self.mpos.y() + self.viewport.verticalScrollBar().value()) / (CELLSIZE * self.viewport.zoom) - .5) * CELLSIZE
        )
        return pos