from core.Modify.EditorMode import EditorMode
from PySide6.QtCore import QRect, QPoint, Qt
from PySide6.QtGui import QColor, QPen, QMoveEvent, QWheelEvent, QMouseEvent, QKeySequence
from PySide6.QtWidgets import QGraphicsRectItem
from core.info import CELLSIZE
from BaseMod.geo.geoHistory import GEpointChange
from core.configTypes.BaseTypes import StringConfigurable, BoolConfigurable
from core.configTypes.QtTypes import KeyConfigurable, EnumConfigurable
from enum import Enum, auto


class GeoBlocks(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    Wall = auto()
    Air = auto()
    Slope = auto()
    Beam = auto()
    Floor = auto()
    Crack = auto()
    Spear = auto()
    Rock = auto()
    Glass = auto()
    Hive = auto()
    ForbidFlyChains = auto()
    WormGrass = auto()
    ShortcutEntrance = auto()
    Shortcut = auto()
    DragonDen = auto()
    Entrance = auto()
    WhackAMoleHole = auto()
    GarbageWormDen = auto()
    ScavengerDen = auto()
    CleanUpper = auto()
    CleanLayer = auto()
    CleanBlocks = auto()
    CleanAll = auto()


class GeoTools(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    Pen = auto()
    Brush = auto()
    Bucket = auto()
    Line = auto()
    Rect = auto()
    RectHollow = auto()
    Circle = auto()
    CircleHollow = auto()


class GeometryEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.module = self.mod.geomodule

        self.cursor: QGraphicsRectItem | None = None
        self.lastpos = QPoint()
        self.block = EnumConfigurable(mod, "EDIT_geo.block", GeoBlocks.Wall, GeoBlocks, "Current geo block")
        self.toolleft = EnumConfigurable(mod, "EDIT_geo.lmb", GeoTools.Pen, GeoTools, "Current geo tool for LMB")
        self.toolright = EnumConfigurable(mod, "EDIT_geo.rmb", GeoTools.Rect, GeoTools, "Current geo tool for RMB")
        self.drawl1 = BoolConfigurable(mod, "EDIT_geo.drawl1", True, "Draw on l1")
        self.drawl2 = BoolConfigurable(mod, "EDIT_geo.drawl2", True, "Draw on l2")
        self.drawl3 = BoolConfigurable(mod, "EDIT_geo.drawl3", True, "Draw on l3")

        self.drawl1_key = KeyConfigurable(mod, "EDIT_geo.drawl1_key", "Ctrl+1", "key to draw on 1st layer")
        self.drawl2_key = KeyConfigurable(mod, "EDIT_geo.drawl2_key", "Ctrl+2", "key to draw on 2nd layer")
        self.drawl3_key = KeyConfigurable(mod, "EDIT_geo.drawl3_key", "Ctrl+3", "key to draw on 3rd layer")

    @property
    def layers(self) -> list[bool]:
        return [self.drawl1.value, self.drawl2.value, self.drawl3.value]

    def init_scene_items(self):
        self.cursor = self.viewport.workscene.addRect(QRect(0, 0, 20, 20), pen=QPen(QColor(255, 0, 0), 3))
        self.manager.set_status("placing walls")

    def remove_items_from_scene(self):
        self.cursor.removeFromIndex()

    def mouse_press_event(self, event: QMouseEvent):
        if self.mouse_left:
            self.tool_specific_press(self.toolleft.value)
        if self.mouse_right:
            self.tool_specific_press(self.toolright.value)

    def tool_specific_press(self, tool: GeoTools):
        fpos = self.viewport.viewport_to_editor(self.mpos)
        if tool == GeoTools.Pen:
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