from widgets.Viewport import ViewPort
from PySide6.QtGui import QMoveEvent, QMouseEvent

class EditorMode:
    """
    Base for creating custom viewport editors
    :param viewport: viewport where actions should be tracked
    """
    def __init__(self, viewport: ViewPort):
        self.viewport = viewport

    def init_scene_items(self):
        pass

    def mouse_move_event(self, event: QMoveEvent):
        pass

    def mouse_click_event(self, event: QMouseEvent):
        pass

    def remove_items_from_scene(self):
        pass