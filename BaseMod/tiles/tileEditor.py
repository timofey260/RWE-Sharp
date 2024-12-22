from __future__ import annotations

import os
from enum import Enum, auto
from typing import TYPE_CHECKING

from PySide6.QtGui import QMoveEvent, QImage, QMouseEvent

from RWESharp.Configurable import IntConfigurable, BoolConfigurable, StringConfigurable, EnumConfigurable
from RWESharp.Core import CELLSIZE, PATH_FILES_IMAGES_PALETTES
from RWESharp.Modify import Editor
from RWESharp.Loaders import palette_to_colortable, tile_offset, Tile
from RWESharp.Renderable import RenderTile
from BaseMod.tiles.tileExplorer import TileExplorer
from BaseMod.tiles.tileHistory import TilePen

if TYPE_CHECKING:
    from BaseMod.baseMod import BaseMod


class TileTools(Enum):
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


class TileEditor(Editor):

    def __init__(self, mod):
        super().__init__(mod)
        mod: BaseMod
        self.module = None
        self.previewoption = IntConfigurable(mod, "EDIT_tiles.previewMode", 7, "tile preview mode")
        self.show_collisions = BoolConfigurable(mod, "EDIT_tiles.show_collisions", True, "Show collisions")
        self.vis_layer = IntConfigurable(mod, "EDIT_tiles.layer", 1, "Layer to place tiles on")
        self.palette_image = StringConfigurable(mod, "EDIT_tiles.palette",
                                                os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"),
                                                "Layer to place tiles on")
        if not os.path.exists(self.palette_image.value):
            self.palette_image.reset_value()
        self.toolleft = EnumConfigurable(mod, "EDIT_tiles.lmb", TileTools.Pen, TileTools, "Current geo tool for LMB")
        self.toolright = EnumConfigurable(mod, "EDIT_tiles.rmb", TileTools.Rect, TileTools, "Current geo tool for RMB")
        self.deleteleft = BoolConfigurable(mod, "EDIT_tiles.deletelmb", False, "Delete tiles with LMB")
        self.deleteright = BoolConfigurable(mod, "EDIT_tiles.deletermb", False, "Delete tiles with RMB")
        self.force_place = BoolConfigurable(mod, "EDIT_tiles.fp", False, "Force place")
        self.force_geo = BoolConfigurable(mod, "EDIT_tiles.fg", False, "Force geometry")

        self.colortable = palette_to_colortable(QImage(self.palette_image.value))
        self.explorer = TileExplorer(self, self.manager.window)
        self.tile: Tile | None = mod.manager.tiles.find_tile("Four Holes")
        self.tile_item = RenderTile(self, 0, self.layer).add_myself(self)
        # self.tile_cols_image = QPixmap(1, 1)
        # self.tile_cols_painter = QPainter(self.tile_cols_image)
        # self.tile_item: QGraphicsPixmapItem | None = None
        # self.tile_cols_item: QGraphicsPixmapItem | None = None

        self.show_collisions.valueChanged.connect(self.hide_collisions)
        self.previewoption.valueChanged.connect(self.redraw_tile)
        self.vis_layer.valueChanged.connect(self.redraw_tile)
        self.palette_image.valueChanged.connect(self.change_palette)

    @property
    def layer(self):
        return self.vis_layer.value - 1

    @layer.setter
    def layer(self, value):
        self.vis_layer.update_value(value)

    def change_palette(self):
        self.colortable = palette_to_colortable(QImage(self.palette_image.value))
        self.redraw_tile()

    def add_tile(self, tiles: list[Tile]):
        self.tile = tiles[0]
        self.redraw_tile()

    def redraw_tile(self):
        if self.tile is None or self.tile_item.renderedtexture is None:
            return
        self.tile_item.layer = self.layer
        self.tile_item.set_tile(self.tile, self.colortable, self.tile_preview_option)

    def hide_collisions(self, value):
        self.tile_item.colsimage_rendered.setOpacity(1 if value else 0)

    @property
    def tile_preview_option(self):
        value = self.previewoption.value
        if self.previewoption.value == 7:
            value = self.basemod.tileview.drawoption.value
        return value

    def mouse_move_event(self, event: QMoveEvent):
        if self.tile is None:
            return
        offset = tile_offset(self.tile)
        curpos = self.viewport.viewport_to_editor(self.mouse_pos)
        cellpos = curpos - offset
        self.tile_item.setPos(cellpos * CELLSIZE)
        if self.mouse_left:
            if self.deleteleft.value:
                self.manager.selected_viewport.level.history.last_element.add_move(curpos)
            else:
                self.manager.selected_viewport.level.history.last_element.add_move(cellpos)
        if self.manager.selected_viewport.level.inside(cellpos):
            self.manager.set_status(f"x: {cellpos.x()}, y: {cellpos.y()}, {self.manager.selected_viewport.level['TE']['tlMatrix'][cellpos.x()][cellpos.y()]}")
        # self.tile_item.setPos(pos)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.module = viewport.modulenames["tiles"]
        self.basemod.tileview.drawoption.valueChanged.connect(self.redraw_tile)
        self.redraw_tile()

    def remove_items_from_scene(self, viewport):
        super().remove_items_from_scene(viewport)
        self.module = None

    def mouse_press_event(self, event: QMouseEvent):
        if self.mouse_left:
            self.tool_specific_press(self.toolleft.value, self.deleteleft.value)
        if self.mouse_left:
            self.tool_specific_press(self.toolright.value, self.deleteright.value)

    def tool_specific_press(self, tool: Enum, delete: bool):
        offset = tile_offset(self.tile)
        fpos = self.viewport.viewport_to_editor(self.mouse_pos) - offset
        if tool == TileTools.Pen:
            self.manager.selected_viewport.level.add_history(TilePen(self.manager.selected_viewport.level.history, fpos, self.tile, self.layer, delete, self.force_place.value, self.force_geo.value))
