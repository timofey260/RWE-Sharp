from __future__ import annotations

from enum import Enum, auto
from typing import TYPE_CHECKING

from PySide6.QtCore import QRect, QPoint, QLine
from PySide6.QtGui import QMoveEvent, QMouseEvent, QColor

from BaseMod.tiles.tileExplorer import TileExplorer
from BaseMod.tiles.tileHistory import TilePen, TileRectangle, TileEllipse, TileLine, TileBrush
from BaseMod.tiles.tileUtils import can_place
from RWESharp2.Configurable import IntConfigurable, BoolConfigurable, EnumConfigurable
from RWESharp2.Core import CELLSIZE
from RWESharp2.Loaders import Tile
from RWESharp2.Modify import Editor
from RWESharp2.Renderable import RenderTile, RenderRect, RenderEllipse, RenderLine
from RWESharp2.Utils import fit_rect

if TYPE_CHECKING:
    from BaseMod.baseMod import BaseMod


class TileTools(Enum):
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        return count
    Pen = auto()
    Brush = auto()
    Line = auto()
    Rect = auto()
    RectHollow = auto()
    Circle = auto()
    CircleHollow = auto()


class TileEditor(Editor):

    def __init__(self, mod):
        super().__init__(mod)
        mod: BaseMod
        self.module = None
        self.show_collisions = BoolConfigurable(mod, "EDIT_tiles.show_collisions", True, "Show collisions")
        self.vis_layer = IntConfigurable(mod, "EDIT_tiles.layer", 1, "Layer to place tiles on")

        self.strictmode = IntConfigurable(mod, "EDIT_tiles.strict", 0,
                                          "If mode is Strict, all tilebodies that refer to tilehead will be removed\n"
                                          "if mode is Full, all tilebodies in tilehead area will be removed\n"
                                          "Might be helpful when dealing with broken levels")
        self.toolleft = EnumConfigurable(mod, "EDIT_tiles.lmb", TileTools.Pen, TileTools, "Current geo tool for LMB")
        self.toolright = EnumConfigurable(mod, "EDIT_tiles.rmb", TileTools.Rect, TileTools, "Current geo tool for RMB")
        self.deleteleft = BoolConfigurable(mod, "EDIT_tiles.deletelmb", False, "Delete tiles with LMB")
        self.deleteright = BoolConfigurable(mod, "EDIT_tiles.deletermb", False, "Delete tiles with RMB")
        self.force_place = BoolConfigurable(mod, "EDIT_tiles.fp", False, "Force place")
        self.force_geo = BoolConfigurable(mod, "EDIT_tiles.fg", False, "Force geometry")
        self.brushsize = IntConfigurable(mod, "EDIT_tiles.brushsize", 4, "Brush size")

        self.explorer = TileExplorer(self, self.manager.window)
        self.tile: Tile | None = mod.manager.tiles.find_tile("Four Holes")
        self.tile_item = RenderTile(self, 0, self.layer)
        self.tile_rect = RenderRect(self, -10, QRect())
        self.rect_rect = RenderRect(self, -5, QRect())  # uh whatever at this point
        self.rect_ellipse = RenderEllipse(self, -5, QRect())  # gosh i'm so original
        self.rect_line = RenderLine(self, -5, QLine())  # this doesn't even make sense i got sick
        self.rect_brush = RenderEllipse(self, -5, QRect())  # i guess
        self.rect_rect.setOpacity(0)
        self.rect_ellipse.setOpacity(0)
        self.rect_line.setOpacity(0)
        self.rect_brush.setOpacity(0)
        # self.tile_cols_image = QPixmap(1, 1)
        # self.tile_cols_painter = QPainter(self.tile_cols_image)
        # self.tile_item: QGraphicsPixmapItem | None = None
        # self.tile_cols_item: QGraphicsPixmapItem | None = None

        self.show_collisions.valueChanged.connect(self.hide_collisions)
        self.mod.tileview.drawoption.valueChanged.connect(self.redraw_tile)
        self.mod.tileview.palettepath.valueChanged.connect(self.redraw_tile)
        self.vis_layer.valueChanged.connect(self.redraw_tile)

        self.lastpos = QPoint()
        self.lastclick = QPoint()
        self.toolright.valueChanged.connect(self.tool_changed)
        self.toolleft.valueChanged.connect(self.tool_changed)

    def tool_changed(self):
        self.rect_brush.setOpacity(0)
        if self.toolleft.value == TileTools.Brush or self.toolright.value == TileTools.Brush \
                or self.toolleft.value == TileTools.Line or self.toolright.value == TileTools.Line:
            self.rect_brush.setOpacity(1)

    @property
    def strict(self):
        return self.strictmode.value == 0

    @property
    def layer(self):
        if not hasattr(self.mod, "tileui"):
            return self.vis_layer.value - 1
        return self.module.layer if self.mod.tileui.ui.Follow.isChecked() else self.vis_layer.value - 1

    @layer.setter
    def layer(self, value):
        self.vis_layer.update_value(value)

    def add_tile(self, tiles: list[Tile]):
        self.tile = tiles[0]
        self.redraw_tile()

    def redraw_tile(self):
        if self.tile is None or self.tile_item.renderedtexture is None:
            return
        self.tile_item.layer = self.layer
        self.tile_item.set_tile(self.tile, self.mod.tileview.colortable, self.tile_preview_option)

    def hide_collisions(self, value):
        self.tile_item.colsimage_rendered.setOpacity(1 if value else 0)

    @property
    def tile_preview_option(self):
        return self.basemod.tileview.drawoption.value

    def mouse_move_event(self, event: QMoveEvent):
        if self.tile is None:
            return
        curpos = self.viewport.viewport_to_editor(self.mouse_pos)
        cellpos = curpos - self.tile.top_left
        self.tile_item.setPos(cellpos * CELLSIZE)
        if self.mouse_left:
            self.tool_specific_update(self.toolleft.value, self.deleteleft.value)
        if self.mouse_right:
            self.tool_specific_update(self.toolright.value, self.deleteright.value)
        if self.manager.selected_viewport.level.inside(cellpos):
            # self.manager.set_status(f"x: {cellpos.x()}, y: {cellpos.y()}, {self.manager.selected_viewport.level['TE']['tlMatrix'][cellpos.x()][cellpos.y()]}")
            layers = []
            for i in self.manager.selected_viewport.level.l_tiles[cellpos]:
                if i is None:
                    layers.append("Empty")
                    continue
                layers.append(i.tostring(self.level))
            self.manager.set_status(f"x: {cellpos.x()}, y: {cellpos.y()}, [{', '.join(layers)}]")
        # self.tile_item.setPos(pos)
        # self.tile_rect.setPos(self.tile_item.offset)
        # rect.setTopLeft(rect.topLeft() - QPoint(3, 3))
        # rect.setBottomRight(rect.bottomRight() + QPoint(3, 3))
        fpos = self.viewport.viewport_to_editor(self.mouse_pos) - self.tile.top_left
        rect = QRect(fpos * CELLSIZE, self.tile.size * CELLSIZE)
        rect.adjust(-3, -3, 3, 3)
        self.tile_rect.setRect(rect)
        b2 = round(self.brushsize.value / 2 * CELLSIZE)
        brushrect = QRect(curpos.x() * CELLSIZE - b2, curpos.y() * CELLSIZE - b2, self.brushsize.value * CELLSIZE, self.brushsize.value * CELLSIZE)
        self.rect_brush.setRect(brushrect)
        # self.tile_rect.setScale(self.tile_item.scale)

        self.tile_rect.drawrect.setPen(QColor(0, 255, 0) if can_place(self.level, fpos, self.layer, self.tile, self.force_place.value, self.force_geo.value) else QColor(255, 0, 0))
        self.lastpos = fpos

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.module = viewport.modulenames["tiles"]
        self.basemod.tileview.drawoption.valueChanged.connect(self.redraw_tile)
        self.basemod.tileui.set_default_material()
        self.redraw_tile()

    def remove_items_from_scene(self, viewport):
        super().remove_items_from_scene(viewport)
        self.module = None

    def mouse_press_event(self, event: QMouseEvent):
        self.lastclick = self.mouse_pos
        if self.mouse_left:
            #self.level.l_tiles.tile_data(self.viewport.viewport_to_editor(self.mouse_pos), self.layer).remove(self.level)
            self.tool_specific_press(self.toolleft.value, self.deleteleft.value) 
        elif self.mouse_right:
            self.tool_specific_press(self.toolright.value, self.deleteright.value)

    def mouse_left_release(self):
        self.tool_specific_release(self.toolleft.value, self.deleteleft.value)

    def mouse_right_release(self):
        if self.mouse_left:
            return
        self.tool_specific_release(self.toolright.value, self.deleteright.value)
            
    def tool_specific_release(self, tool: Enum, delete: bool):
        curpos = self.viewport.viewport_to_editor(self.mouse_pos)
        lastpos = self.viewport.viewport_to_editor(self.lastclick)
        if tool == TileTools.Rect or tool == TileTools.RectHollow:
            rect = fit_rect(lastpos, curpos, self.shift, self.alt)
            self.manager.selected_viewport.level.add_history(TileRectangle, rect, self.tile, self.layer, tool == TileTools.RectHollow, delete, self.force_place.value, self.force_geo.value, self.strict)
            self.rect_rect.setOpacity(0)
        elif tool == TileTools.Circle or tool == TileTools.CircleHollow:
            rect = fit_rect(lastpos, curpos, self.shift, self.alt)
            self.manager.selected_viewport.level.add_history(TileEllipse, rect, self.tile, self.layer, tool == TileTools.CircleHollow, delete, self.force_place.value, self.force_geo.value, self.strict)
            self.rect_ellipse.setOpacity(0)
        elif tool == TileTools.Line:
            self.manager.selected_viewport.level.add_history(TileLine, lastpos, curpos, self.tile, self.layer, self.brushsize.value, delete, self.force_place.value, self.force_geo.value, self.strict)
            self.rect_line.setOpacity(0)

    def tool_specific_press(self, tool: Enum, delete: bool):
        fpos = self.viewport.viewport_to_editor(self.mouse_pos) - self.tile.top_left
        if tool == TileTools.Pen:
            self.manager.selected_viewport.level.add_history(TilePen, fpos, self.tile, self.layer, delete, self.force_place.value, self.force_geo.value, self.strict)
        elif tool == TileTools.Brush:
            self.manager.selected_viewport.level.add_history(TileBrush, fpos, self.tile, self.layer, self.brushsize.value, delete, self.force_place.value, self.force_geo.value, self.strict)
        elif tool == TileTools.Rect or tool == TileTools.RectHollow:
            self.rect_rect.setOpacity(1)
            self.rect_rect.setRect(QRect(0, 0, 1, 1))
        elif tool == TileTools.Circle or tool == TileTools.CircleHollow:
            self.rect_ellipse.setOpacity(1)
            self.rect_ellipse.setRect(QRect(0, 0, 1, 1))
        elif tool == TileTools.Line:
            self.rect_line.setOpacity(1)
            self.rect_line.setLine(QLine())

    def tool_specific_update(self, tool: Enum, delete: bool):
        curpos = self.viewport.viewport_to_editor(self.mouse_pos)
        cellpos = curpos - self.tile.top_left
        lastpos = self.viewport.viewport_to_editor(self.lastclick)
        if tool == TileTools.Pen or tool == TileTools.Brush:
            if delete:
                self.manager.selected_viewport.level.history.last_element.add_move(curpos)
                return
            self.manager.selected_viewport.level.history.last_element.add_move(cellpos)
        elif tool == TileTools.Rect or tool == TileTools.RectHollow:
            rect = fit_rect(lastpos, curpos, self.shift, self.alt)
            self.rect_rect.setRect(QRect(rect.x() * CELLSIZE, rect.y() * CELLSIZE, rect.width() * CELLSIZE, rect.height() * CELLSIZE))
        elif tool == TileTools.Circle or tool == TileTools.CircleHollow:
            rect = fit_rect(lastpos, curpos, self.shift, self.alt)
            self.rect_ellipse.setRect(QRect(rect.x() * CELLSIZE, rect.y() * CELLSIZE, rect.width() * CELLSIZE, rect.height() * CELLSIZE))
        elif tool == TileTools.Line:
            self.rect_line.setLine(QLine(lastpos * CELLSIZE, curpos * CELLSIZE))
