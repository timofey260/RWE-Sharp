from core.Modify.EditorMode import EditorMode
from PySide6.QtCore import QRect, QPoint, Slot
from PySide6.QtGui import QColor, QPen, QMoveEvent, QWheelEvent, QMouseEvent
from PySide6.QtWidgets import QGraphicsRectItem
from core.info import CELLSIZE
from BaseMod.geo.geoHistory import GEBlockChange, GEStackChange, GEClearAll, GEShortcutBlock, GEClearUpper, GEClearBlock, GEClearLayer
from core.configTypes.BaseTypes import BoolConfigurable, IntConfigurable
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
    GarbageWormHole = auto()
    ScavengerDen = auto()
    Waterfall = auto()
    CleanUpper = auto()
    CleanLayer = auto()
    CleanBlocks = auto()
    CleanAll = auto()


blocks = [
    GeoBlocks.Air,
    GeoBlocks.Wall,
    GeoBlocks.Slope,
    GeoBlocks.Floor,
    GeoBlocks.Glass
]

stackables = [
    GeoBlocks.Beam,
    GeoBlocks.Crack,
    GeoBlocks.Spear,
    GeoBlocks.Rock,
    GeoBlocks.Hive,
    GeoBlocks.ForbidFlyChains,
    GeoBlocks.WormGrass,
    GeoBlocks.Shortcut,
    GeoBlocks.DragonDen,
    GeoBlocks.Entrance,
    GeoBlocks.WhackAMoleHole,
    GeoBlocks.GarbageWormHole,
    GeoBlocks.ScavengerDen,
    GeoBlocks.Waterfall,
]


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
        self.rotation = IntConfigurable(mod, "EDIT_geo.rotation", 0, "Rotation of block")
        self.drawl1 = BoolConfigurable(mod, "EDIT_geo.drawl1", True, "Draw on l1")
        self.drawl2 = BoolConfigurable(mod, "EDIT_geo.drawl2", True, "Draw on l2")
        self.drawl3 = BoolConfigurable(mod, "EDIT_geo.drawl3", True, "Draw on l3")

        self.drawl1_key = KeyConfigurable(mod, "EDIT_geo.drawl1_key", "Ctrl+1", "key to draw on 1st layer")
        self.drawl2_key = KeyConfigurable(mod, "EDIT_geo.drawl2_key", "Ctrl+2", "key to draw on 2nd layer")
        self.drawl3_key = KeyConfigurable(mod, "EDIT_geo.drawl3_key", "Ctrl+3", "key to draw on 3rd layer")

    @property
    def layers(self) -> list[bool]:
        return [self.drawl1.value, self.drawl2.value, self.drawl3.value]

    def block2info(self) -> [int, bool]:  # tile, stackable
        match self.block.value:
            case GeoBlocks.Wall:
                return 1, False
            case GeoBlocks.Air:
                return 0, False
            case GeoBlocks.Floor:
                return 6, False
            case GeoBlocks.Slope:
                return 2 + self.rotation.value, False
            # case GeoBlocks.ShortcutEntrance:  # obsolete
            #     return 7, False
            case GeoBlocks.Glass:
                return 9, False

            case GeoBlocks.Beam:
                return 1 + self.rotation.value % 2, True
            case GeoBlocks.Hive:
                return 3, True
            case GeoBlocks.ShortcutEntrance:
                return -1, True
            case GeoBlocks.Shortcut:
                return 5, True
            case GeoBlocks.Entrance:
                return 6, True
            case GeoBlocks.DragonDen:
                return 7, True
            case GeoBlocks.Rock:
                return 9, True
            case GeoBlocks.Spear:
                return 10, True
            case GeoBlocks.Crack:
                return 11, True
            case GeoBlocks.ForbidFlyChains:
                return 12, True
            case GeoBlocks.GarbageWormHole:
                return 13, True
            case GeoBlocks.Waterfall:
                return 18, True
            case GeoBlocks.WhackAMoleHole:
                return 19, True
            case GeoBlocks.WormGrass:
                return 20, True
            case GeoBlocks.ScavengerDen:
                return 21, True

            case GeoBlocks.CleanUpper:
                return -2, True
            case GeoBlocks.CleanBlocks:
                return -3, True
            case GeoBlocks.CleanAll:
                return -4, True
            case GeoBlocks.CleanLayer:
                return -5, True
        return 0, False

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
            blk, stak = self.block2info()
            if not stak:
                self.manager.level.add_history(GEBlockChange(self.manager.level.history, fpos, blk, self.layers))
            elif self.block.value in stackables:
                self.manager.level.add_history(GEStackChange(self.manager.level.history, fpos, blk, self.layers))
            elif blk == -1:
                self.manager.level.add_history(GEShortcutBlock(self.manager.level.history, fpos, self.layers))
            elif blk == -2:
                self.manager.level.add_history(GEClearUpper(self.manager.level.history, fpos, self.layers))
            elif blk == -3:
                self.manager.level.add_history(GEClearBlock(self.manager.level.history, fpos, self.layers))
            elif blk == -4:
                self.manager.level.add_history(GEClearAll(self.manager.level.history, fpos))
            elif blk == -5:
                self.manager.level.add_history(GEClearLayer(self.manager.level.history, fpos, self.layers))

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