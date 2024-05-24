from core.Modify.EditorMode import EditorMode
from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QPen, QMoveEvent, QWheelEvent
from PySide6.QtWidgets import QGraphicsRectItem
from core.info import CELLSIZE


class GeometryEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.config = self.mod.geoconfig
        self.module = self.mod.geomodule

        self.cursor: QGraphicsRectItem = None

    def init_scene_items(self):
        self.cursor = self.viewport.workscene.addRect(QRect(0, 0, 20, 20), pen=QPen(QColor(255, 0, 0), 3))
        self.manager.set_status("placing walls")

    def remove_items_from_scene(self):
        self.cursor.removeFromIndex()

    def mouse_move_event(self, event: QMoveEvent):
        super().mouse_move_event(event)
        pos = self.mousepos * self.viewport.zoom
        self.cursor.setPos(pos)
        fpos = self.viewportcell
        if self.mouse_left and self.manager.level.inside(fpos):
            self.manager.level["GE"][fpos.x()][fpos.y()][0][0] = 1
            self.module.l1.draw_geo(fpos.x(), fpos.y(), True)
            self.module.l1.redraw()

    def mouse_wheel_event(self, event: QWheelEvent):
        self.cursor.setRect(QRect(0, 0, CELLSIZE * self.viewport.zoom, CELLSIZE * self.viewport.zoom))