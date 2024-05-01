from core.EditorModes.EditorMode import EditorMode
from PySide6.QtCore import Slot, Qt, QRect, QPoint
from PySide6.QtGui import QColor, QPen, QMoveEvent
from PySide6.QtWidgets import QGraphicsRectItem
from core.info import CELLSIZE


class GeometryEditor(EditorMode):
    def __init__(self, viewport):
        super().__init__(viewport)

        self.drawl1 = False
        self.drawl2 = False
        self.drawl3 = False
        self.cursor: QGraphicsRectItem = None

    @Slot(Qt.CheckState)
    def check_l1_change(self, state: Qt.CheckState):
        self.drawl1 = state == Qt.CheckState.Checked

    @Slot(Qt.CheckState)
    def check_l2_change(self, state: Qt.CheckState):
        self.drawl2 = state == Qt.CheckState.Checked

    @Slot(Qt.CheckState)
    def check_l3_change(self, state: Qt.CheckState):
        self.drawl3 = state == Qt.CheckState.Checked

    def init_scene_items(self):
        self.cursor = self.viewport.workscene.addRect(QRect(0, 0, 20, 20), pen=QPen(QColor(255, 0, 0), 3))

    def remove_items_from_scene(self):
        self.cursor.removeFromIndex()

    def mouse_move_event(self, event: QMoveEvent):
        pos = event.pos() / (CELLSIZE * self.viewport.zoom) * CELLSIZE
        self.cursor.setPos(pos)