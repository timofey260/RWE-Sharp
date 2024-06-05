from core.Modify.EditorMode import EditorMode
from PySide6.QtCore import QRect, QPoint, Qt
from PySide6.QtGui import QColor, QPen, QMoveEvent, QWheelEvent, QMouseEvent
from PySide6.QtWidgets import QGraphicsRectItem
from core.info import CELLSIZE
from .geoHistory import GEpointChange


class GeometryEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.config = self.mod.geoconfig
        self.module = self.mod.geomodule

        self.cursor: QGraphicsRectItem | None = None
        self.lastpos = QPoint()

    @property
    def layers(self) -> list[bool]:
        return [self.config.drawl1.value, self.config.drawl2.value, self.config.drawl3.value]

    def init_scene_items(self):
        self.cursor = self.viewport.workscene.addRect(QRect(0, 0, 20, 20), pen=QPen(QColor(255, 0, 0), 3))
        self.manager.set_status("placing walls")

    def remove_items_from_scene(self):
        self.cursor.removeFromIndex()

    def mouse_press_event(self, event: QMouseEvent):
        # todo tools
        if self.mouse_left:
            fpos = self.viewport.viewport_to_editor(self.mpos)
            self.manager.level.add_history(GEpointChange(self.manager.level.history, fpos, [1, []], self.layers))

    def mouse_move_event(self, event: QMoveEvent):
        super().mouse_move_event(event)
        fpos = self.viewport.viewport_to_editor(self.mpos)
        cpos = self.viewport.editor_to_viewport(fpos)
        if cpos != self.cursor.pos():
            self.cursor.setPos(self.viewport.editor_to_viewport(fpos))
        if self.manager.level.inside(fpos):
            self.manager.set_status(f"x: {fpos.x()}, y: {fpos.y()}, {self.manager.level['GE'][fpos.x()][fpos.y()]}")
        if self.mouse_left and self.manager.level.inside(fpos) and not (self.lastpos - fpos).isNull():
            self.manager.level.last_history_element.add_move(fpos)

            # self.manager.set_status(str(self.manager.level.TE_data(fpos.x(), fpos.y(), 0)))
            # self.manager.level["GE"][fpos.x()][fpos.y()][0][0] = 1
            # self.module.l1.draw_geo(fpos.x(), fpos.y(), True)
            # self.module.l1.redraw()
        self.lastpos = fpos

    def mouse_wheel_event(self, event: QWheelEvent):
        self.cursor.setRect(QRect(0, 0, CELLSIZE * self.viewport.zoom, CELLSIZE * self.viewport.zoom))