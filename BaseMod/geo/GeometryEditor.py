from core.EditorMode import EditorMode
from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QPen, QMoveEvent, QWheelEvent
from PySide6.QtWidgets import QGraphicsRectItem
from core.info import CELLSIZE


class GeometryEditor(EditorMode):
    def __init__(self, manager):
        super().__init__(manager)

        self.drawl1 = False
        self.drawl2 = False
        self.drawl3 = False

        self.cursor: QGraphicsRectItem = None

    def init_scene_items(self):
        self.cursor = self.viewport.workscene.addRect(QRect(0, 0, 20, 20), pen=QPen(QColor(255, 0, 0), 3))

    def remove_items_from_scene(self):
        self.cursor.removeFromIndex()

    def mouse_move_event(self, event: QMoveEvent):
        super().mouse_move_event(event)
        pos = self.mousepos * self.viewport.zoom
        self.cursor.setPos(pos)

    def mouse_wheel_event(self, event: QWheelEvent):
        self.cursor.setRect(QRect(0, 0, CELLSIZE * self.viewport.zoom, CELLSIZE * self.viewport.zoom))