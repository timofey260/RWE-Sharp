from core.EditorModes.EditorMode import EditorMode
from PySide6.QtCore import Slot, Qt, QRect, QPoint
from PySide6.QtGui import QColor, QPen, QMoveEvent, QWheelEvent
from PySide6.QtWidgets import QGraphicsRectItem, QGraphicsPixmapItem
from core.info import CELLSIZE


class GeometryEditor(EditorMode):
    def __init__(self, viewport, l1: QGraphicsPixmapItem, l2: QGraphicsPixmapItem, l3: QGraphicsPixmapItem):
        super().__init__(viewport)

        self.drawl1 = False
        self.drawl2 = False
        self.drawl3 = False
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.cursor: QGraphicsRectItem = None

    @Slot(Qt.CheckState)
    def check_l1_change(self, state: Qt.CheckState):
        self.drawl1 = state == Qt.CheckState.Checked
        self.l1.setOpacity(1 if self.drawl1 else 0)

    @Slot(Qt.CheckState)
    def check_l2_change(self, state: Qt.CheckState):
        self.drawl2 = state == Qt.CheckState.Checked
        self.l2.setOpacity(1 if self.drawl2 else 0)

    @Slot(Qt.CheckState)
    def check_l3_change(self, state: Qt.CheckState):
        self.drawl3 = state == Qt.CheckState.Checked
        self.l2.setOpacity(1 if self.drawl3 else 0)

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