import os
from enum import Enum, auto
import numpy as np

from PySide6.QtCore import QRectF, QPoint, QSize, QLine, QRect
from PySide6.QtGui import QColor, QMoveEvent, QMouseEvent, QPixmap, QPainter, QCursor

from BaseMod.geo.geoControls import GeoControls
from BaseMod.geo.GeoConsts import IMG_PEN, IMG_BRUSH, IMG_BUCKET, IMG_LINE, IMG_RECT, IMG_RECT_HOLLOW, IMG_CIRCLE, IMG_CIRCLE_HOLLOW
from BaseMod.geo.geoHistory import GEPointChange, GERectChange, GEBrushChange, GEEllipseChange, GEFillChange
from BaseMod.LevelParts import stack_pos, GeoLevelPart
from RWESharp.Configurable import BoolConfigurable, IntConfigurable, EnumConfigurable, ColorConfigurable
from RWESharp.Core import CELLSIZE, PATH_FILES_IMAGES, CONSTS
from RWESharp.Modify import Editor
from RWESharp.Renderable import RenderImage, RenderRect, RenderEllipse, RenderLine
from RWESharp.Utils import closest_line, paint_svg


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
    Inverse = auto()


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
    GeoBlocks.ShortcutEntrance
]

stackables_all_layers = [
    GeoBlocks.Beam,
    GeoBlocks.Crack,
    GeoBlocks.Hive,
    GeoBlocks.ShortcutEntrance,
    GeoBlocks.Shortcut
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


class GeometryEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod

        self.cursor = RenderRect(self, 0, QRectF(0, 0, CELLSIZE, CELLSIZE))
        self.rect = RenderRect(self, 0, QRectF(0, 0, CELLSIZE, CELLSIZE))
        self.ellipse = RenderEllipse(self, 0, QRect(0, 0, CELLSIZE, CELLSIZE))
        self.brushellipse = RenderEllipse(self, 0, QRect(0, 0, CELLSIZE, CELLSIZE))
        self.lineline = RenderLine(self, 0, QLine(0, 0, 0, 0))
        self.pixmap = RenderImage(self, 1, QSize(CELLSIZE, CELLSIZE))
        self.lastpos = QPoint()
        self.block = EnumConfigurable(mod, "EDIT_geo.block", GeoBlocks.Wall, GeoBlocks, "Current geo block")
        self.toolleft = EnumConfigurable(mod, "EDIT_geo.lmb", GeoTools.Pen, GeoTools, "Current geo tool for LMB")
        self.toolright = EnumConfigurable(mod, "EDIT_geo.rmb", GeoTools.Rect, GeoTools, "Current geo tool for RMB")
        self.rotation = IntConfigurable(mod, "EDIT_geo.rotation", 0, "Rotation of block")
        self.drawl1 = BoolConfigurable(mod, "EDIT_geo.drawl1", True, "Draw on l1")
        self.drawl2 = BoolConfigurable(mod, "EDIT_geo.drawl2", False, "Draw on l2")
        self.drawl3 = BoolConfigurable(mod, "EDIT_geo.drawl3", False, "Draw on l3")
        self.drawfollow = BoolConfigurable(mod, "EDIT_geo.drawlfollow", True, "Follow current layer")
        self.brushsize = IntConfigurable(mod, "EDIT_geo.brushsize", 4, "Brush size")

        self.controls = GeoControls(mod)
        self.block.valueChanged.connect(self.block_changed)
        self.rotation.valueChanged.connect(self.block_changed)

        self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))

        self.binfo: dict = CONSTS.get("geo_image_config", {}).get("blocksinfo", {})
        self.sinfo: dict = CONSTS.get("geo_image_config", {}).get("stackablesinfo", {})
        self._sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        self.lastclick = QPoint()
        self.toolleft.valueChanged.connect(self.tool_changed)
        self.toolright.valueChanged.connect(self.tool_changed)
        self.brushsize.valueChanged.connect(self.repos_brush)
        self.toolcolor = ColorConfigurable(mod, "EDIT_geo.toolcolor", QColor(255, 0, 0, 255), "Tool color")
        self.toolcolor.valueChanged.connect(self.change_color)

        self.geo_preload = QPixmap(256 * self._sz, self._sz * 2)  # this would be something
        #self.preload_geo_textures()

    def preload_geo_textures(self):  # optimizations my man
        self.geo_preload.fill(QColor(0, 0, 0, 0))
        p = QPainter(self.geo_preload)
        for i in range(256):
            for j in GeoLevelPart.byte2stack(i):
                pos = self.sinfo.get(str(j), [0, 0])
                if j == 4:
                    continue
                    # pos = pos[1]
                if j == 11:
                    continue
                    # pos = pos[0]
                p.drawPixmap(QPoint(i * self._sz, 0), self.geo_texture, QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz))
            for j in GeoLevelPart.byte2stack(i << 8):
                pos = self.sinfo.get(str(j), [0, 0])
                p.drawPixmap(QPoint(i * self._sz, self._sz), self.geo_texture, QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz))
        p.end()

    def update_geo_texture(self):
        if os.path.exists(self.mod.geoview.imagepath.value):
            self.geo_texture = QPixmap(self.mod.geoview.imagepath.value)
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))
        self.preload_geo_textures()

    @property
    def module(self):
        return self.viewport.modulenames["geo"]

    def change_color(self):
        self.rect.drawrect.setPen(self.toolcolor.value)
        self.cursor.drawrect.setPen(self.toolcolor.value)
        self.brushellipse.drawellipse.setPen(self.toolcolor.value)
        self.ellipse.drawellipse.setPen(self.toolcolor.value)
        self.lineline.drawline.setPen(self.toolcolor.value)

    def rotate(self):
        if self.block.value in [GeoBlocks.Slope, GeoBlocks.Beam]:
            self.rotation.update_value((self.rotation.value + 1) % (4 if self.block.value == GeoBlocks.Slope else 2))

    def rotate_back(self):
        if self.block.value in [GeoBlocks.Slope, GeoBlocks.Beam]:
            self.rotation.update_value((self.rotation.value - 1) % (4 if self.block.value == GeoBlocks.Slope else 2))

    def tool_changed(self, tool):
        self.brushellipse.drawellipse.setOpacity(0)
        if tool == GeoTools.Brush or tool == GeoTools.Line:
            self.brushellipse.drawellipse.setOpacity(1)

    def block_changed(self):
        if self.block.value == GeoBlocks.CleanAll:
            self.drawl1.update_value(True)
            self.drawl2.update_value(True)
            self.drawl3.update_value(True)
        elif self.block.value in stackables and self.block.value not in stackables_all_layers:
            self.drawl1.update_value(True)
            self.drawl2.update_value(False)
            self.drawl3.update_value(False)
        self.pixmap.image.fill(QColor(0, 0, 0, 0))
        blk, stak = self.block2info()
        if not stak and blk != 0:
            pos = self.binfo.get(str(blk), [0, 0])
            cellpos = QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz)
            self.pixmap.painter.drawPixmap(QRect(0, 0, CELLSIZE, CELLSIZE), self.geo_texture, cellpos)
        elif self.block.value in stackables:
            blk = self.level.l_geo.byte2stack(blk)[0]
            pos = self.sinfo.get(str(blk), [0, 0])
            if blk == 4:
                pos = self.sinfo.get(str(blk), [[0, 0]])
                pos = pos[1]
            if blk == 11:
                pos = self.sinfo.get(str(blk), [[0, 0]])
                pos = pos[0]
            cellpos = QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz)
            self.pixmap.painter.drawPixmap(QRect(0, 0, CELLSIZE, CELLSIZE), self.geo_texture, cellpos)
        else:
            self.pixmap.painter.setBrush(QColor(0, 0, 0, 0))
            self.pixmap.painter.setPen(QColor(255, 0, 0, 255))
            self.pixmap.painter.drawLine(QPoint(0, 0), QPoint(CELLSIZE, CELLSIZE))
            self.pixmap.painter.drawLine(QPoint(CELLSIZE, 0), QPoint(0, CELLSIZE))
        self.pixmap.redraw()

    @property
    def layers(self) -> list[bool]:
        if self.drawfollow.value:
            return [self.layer == 0, self.layer == 1, self.layer == 3]
        return [self.drawl1.value, self.drawl2.value, self.drawl3.value]

    def block2info(self) -> [np.uint16 | np.uint8 | int, bool]:  # tile, stackable
        match self.block.value:
            case GeoBlocks.Wall:
                return np.uint8(1), False
            case GeoBlocks.Air:
                return np.uint8(0), False
            case GeoBlocks.Floor:
                return np.uint8(6), False
            case GeoBlocks.Slope:
                return np.uint8(2 + self.rotation.value), False
            # case GeoBlocks.ShortcutEntrance:  # obsolete
            #     return 7, False
            case GeoBlocks.Glass:
                return np.uint8(9), False

            case GeoBlocks.Beam:
                return np.uint16(1 << stack_pos.index(1 + self.rotation.value % 2)), True
            case GeoBlocks.Hive:
                return np.uint16(0b1000), True
            case GeoBlocks.ShortcutEntrance:
                return np.uint16(0b10000), True
            case GeoBlocks.Shortcut:
                return np.uint16(0b100000), True
            case GeoBlocks.Entrance:
                return np.uint16(0b1000000), True
            case GeoBlocks.DragonDen:
                return np.uint16(0b10000000), True
            case GeoBlocks.Rock:
                return np.uint16(0b100000000), True
            case GeoBlocks.Spear:
                return np.uint16(0b1000000000), True
            case GeoBlocks.Crack:
                return np.uint16(0b100), True
            case GeoBlocks.ForbidFlyChains:
                return np.uint16(0b10000000000), True
            case GeoBlocks.GarbageWormHole:
                return np.uint16(0b100000000000), True
            case GeoBlocks.Waterfall:
                return np.uint16(0b1000000000000), True
            case GeoBlocks.WhackAMoleHole:
                return np.uint16(0b1000000000000000), True
            case GeoBlocks.WormGrass:
                return np.uint16(0b100000000000000), True
            case GeoBlocks.ScavengerDen:
                return np.uint16(0b10000000000000), True

            case GeoBlocks.CleanUpper:
                return -2, True
            case GeoBlocks.CleanBlocks:
                return -3, True
            case GeoBlocks.CleanAll:
                return -5, True
            case GeoBlocks.CleanLayer:
                return -5, True
            case GeoBlocks.Inverse:
                return -6, True
        return 0, False

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.pixmap.renderedtexture.setOpacity(.3)
        self.rect.drawrect.setOpacity(0)
        self.ellipse.drawellipse.setOpacity(0)
        self.brushellipse.drawellipse.setOpacity(0)
        self.lineline.drawline.setOpacity(0)
        # self.cursor_item = self.workscene.addPixmap(self.pixmap)
        # self.cursor_item.setOpacity(.3)
        self.pixmap.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
        self.block_changed()
        self.change_color()

    def mouse_press_event(self, event: QMouseEvent):
        self.lastclick = self.mouse_pos
        if self.mouse_left:
            self.tool_specific_press(self.toolleft.value)
        elif self.mouse_right:  # it's elif for a reason
            self.tool_specific_press(self.toolright.value)

    def mouse_left_release(self):
        self.tool_specific_release(self.toolleft.value)

    def mouse_right_release(self):
        if self.mouse_left:
            return
        self.tool_specific_release(self.toolright.value)

    def tool_specific_release(self, tool: Enum):
        alt = self.alt
        shift = self.shift
        fpos = self.viewport.viewport_to_editor(self.mouse_pos)
        lpos = self.viewport.viewport_to_editor(self.lastclick)
        if tool == GeoTools.Rect or tool == GeoTools.RectHollow:
            blk, stak = self.block2info()
            rect = self.fit_rect(lpos, fpos, shift, alt)
            self.level.add_history(GERectChange, rect, [blk, stak], self.layers, tool == GeoTools.RectHollow)
            self.rect.drawrect.setOpacity(0)
        elif tool == GeoTools.Circle or tool == GeoTools.CircleHollow:
            blk, stak = self.block2info()
            rect = self.fit_rect(lpos, fpos, shift, alt)
            self.level.add_history(GEEllipseChange, rect, [blk, stak], self.layers, tool == GeoTools.CircleHollow)
            self.ellipse.drawellipse.setOpacity(0)
        elif tool == GeoTools.Line:
            self.lineline.drawline.setOpacity(0)
            blk, stak = self.block2info()
            self.level.add_history(GEBrushChange, lpos, [blk, stak], self.layers, self.brushsize.value)
            line = self.fit_line(lpos, fpos, shift)
            self.level.last_history_element.add_move(line.p2())

    def tool_specific_press(self, tool: Enum):
        fpos = self.viewport.viewport_to_editor(self.mouse_pos)
        #self.defaultcursor = QCursor(QPixmap(IMG_PEN), 0, 20)
        if tool == GeoTools.Pen:
            blk, stak = self.block2info()
            self.level.add_history(GEPointChange, fpos, [blk, stak], self.layers)
        elif tool == GeoTools.Brush:
            blk, stak = self.block2info()
            self.level.add_history(GEBrushChange, fpos, [blk, stak], self.layers, self.brushsize.value)
        elif tool == GeoTools.Rect or tool == GeoTools.RectHollow:
            lpos = self.viewport.viewport_to_editor(self.lastclick)
            self.rect.setRect(QRect.span(lpos * CELLSIZE, fpos * CELLSIZE))
            self.rect.drawrect.setOpacity(1)
        elif tool == GeoTools.Circle or tool == GeoTools.CircleHollow:
            lpos = self.viewport.viewport_to_editor(self.lastclick)
            self.ellipse.setRect(QRect.span(lpos * CELLSIZE, fpos * CELLSIZE))
            self.ellipse.drawellipse.setOpacity(1)
        elif tool == GeoTools.Bucket:
            blk, stak = self.block2info()
            self.level.add_history(GEFillChange, fpos, [blk, stak], self.layers)
        elif tool == GeoTools.Line:
            self.lineline.drawline.setOpacity(1)

    def tool_specific_update(self, tool: Enum, pos: QPoint):
        alt = self.alt
        shift = self.shift
        if tool == GeoTools.Pen or tool == GeoTools.Brush:
            self.level.last_history_element.add_move(pos)
        elif tool in [GeoTools.Rect, GeoTools.RectHollow, GeoTools.Circle, GeoTools.CircleHollow]:
            lpos = self.viewport.viewport_to_editor(self.lastclick)
            rect = self.fit_rect(lpos, pos, shift, alt)
            rect.setRect(rect.x() * CELLSIZE, rect.y() * CELLSIZE, rect.width() * CELLSIZE, rect.height() * CELLSIZE)
            # rect.setRect(rect.x(), rect.y(), rect.width(), rect.height())
            #rect.setSize(rect.size() + QSize(CELLSIZE, CELLSIZE))
            self.ellipse.setRect(rect)
            self.rect.setRect(rect)
        elif tool == GeoTools.Line:
            lpos = self.viewport.viewport_to_editor(self.lastclick)
            point = QPoint(CELLSIZE // 2, CELLSIZE // 2)
            line = self.fit_line(lpos, pos, shift)
            self.lineline.setLine(QLine(line.p1() * CELLSIZE + point, line.p2() * CELLSIZE + point))

    def fit_rect(self, lastpos, pos, shift, alt):
        if shift:
            pos2 = pos - lastpos
            absx = abs(pos2.x())
            xmul = 0 if absx == 0 else (pos2.x() // absx)
            absy = abs(pos2.y())
            ymul = 0 if absy == 0 else (pos2.y() // absy)
            if absy > absx:
                pos = QPoint(lastpos.x() + absy * xmul, lastpos.y() + absy * ymul)
            elif absx > absy:
                pos = QPoint(lastpos.x() + absx * xmul, lastpos.y() + absx * ymul)
        rect = QRect.span(lastpos, pos)
        if alt:
            rect = QRect.span(lastpos - (pos - lastpos), pos)
        return rect

    def fit_line(self, lastpos: QPoint, pos: QPoint, shift):
        if shift:
            return closest_line(pos, lastpos).toLine()
        return QLine(lastpos, pos)

    def repos_brush(self):
        pos = self.viewport.viewport_to_editor(self.mouse_pos)
        brushpos = (pos - QPoint(self.brushsize.value // 2, self.brushsize.value // 2)) * CELLSIZE
        rect = QRect(brushpos, QSize(self.brushsize.value, self.brushsize.value) * CELLSIZE)
        if self.brushsize.value % 2 == 0:
            rect.moveTo(brushpos + QPoint(CELLSIZE // 2, CELLSIZE // 2))
        self.brushellipse.setRect(rect)

    def next_layer(self):
        currentlayer = 0 if self.mod.geoview.drawl1.value else 1 if self.mod.geoview.drawl2.value else 2
        currentlayer = (currentlayer + 1) % 3
        self.showlayer(currentlayer)

    def prev_layer(self):
        currentlayer = 0 if self.mod.geoview.drawl1.value else 1 if self.mod.geoview.drawl2.value else 2
        currentlayer = (currentlayer - 1) % 3
        self.showlayer(currentlayer)

    def showlayer(self, currentlayer):
        self.drawl1.update_value(False)
        self.drawl2.update_value(False)
        self.drawl3.update_value(False)
        if self.block.value in stackables and self.block.value not in stackables_all_layers:
            self.drawl1.update_value(True)
        else:
            [self.drawl1, self.drawl2, self.drawl3][currentlayer].update_value(True)
        self.mod.geoview.showlayer(currentlayer)
        self.mod.tileview.showlayer(currentlayer)

    def mouse_move_event(self, event: QMoveEvent):
        super().mouse_move_event(event)
        fpos = self.viewport.viewport_to_editor(self.mouse_pos)
        # print(fpos * CELLSIZE, self.viewport.viewport_to_editor_float(self.mouse_pos.toPointF()))
        if fpos * CELLSIZE != self.cursor.pos.toPoint():
            self.cursor.setPos(fpos.toPointF() * CELLSIZE)
            self.pixmap.setPos(fpos.toPointF() * CELLSIZE)
            self.repos_brush()
            # self.cursor_item.setPos(self.viewport.editor_to_viewport(fpos))
        if self.level.inside(fpos):
            geo = [[int(i[0]), GeoLevelPart.byte2stack(i[1])] for i in self.level.l_geo.getlevelgeo_all(fpos.x(), fpos.y())]
            self.manager.set_status(f"x: {fpos.x()}, y: {fpos.y()}, {geo}"
                                    f" Placing {self.block.value.name}")
        if not (self.lastpos - fpos).isNull():
            if self.mouse_left:
                self.tool_specific_update(self.toolleft.value, fpos)
            elif self.mouse_right:
                self.tool_specific_update(self.toolright.value, fpos)

            # self.manager.set_status(str(self.level.TE_data(fpos.x(), fpos.y(), 0)))
            # self.level["GE"][fpos.x()][fpos.y()][0][0] = 1
            # self.module.l1.draw_geo(fpos.x(), fpos.y(), True)
            # self.module.l1.redraw()
        self.lastpos = fpos
