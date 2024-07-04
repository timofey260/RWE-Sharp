from __future__ import annotations

import os
from enum import Enum, auto
from typing import TYPE_CHECKING

from PySide6.QtCore import QPoint
from PySide6.QtGui import QPixmap, QWheelEvent, QMoveEvent, QImage, QMouseEvent
from PySide6.QtWidgets import QGraphicsPixmapItem

from RWESharp.Configurable import IntConfigurable, BoolConfigurable, StringConfigurable, EnumConfigurable
from RWESharp.Core import CELLSIZE, SPRITESIZE, PATH_FILES_IMAGES_PALETTES
from RWESharp.Modify import EditorMode
from RWESharp.Loaders import palette_to_colortable, return_tile_pixmap, collisions_image, tile_offset, Tile

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


class TileEditor(EditorMode):

    def __init__(self, mod):
        super().__init__(mod)
        mod: BaseMod
        self.module = mod.tilemodule
        self.previewoption = IntConfigurable(mod, "EDIT_tiles.previewMode", 7, "tile preview mode")
        self.show_collisions = BoolConfigurable(mod, "EDIT_tiles.show_collisions", True, "Show collisions")
        self.vis_layer = IntConfigurable(mod, "EDIT_tiles.layer", 1, "Layer to place tiles on")
        self.palette_image = StringConfigurable(mod, "EDIT_tiles.palette",
                                                os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"),
                                                "Layer to place tiles on")
        self.toolleft = EnumConfigurable(mod, "EDIT_tiles.lmb", TileTools.Pen, TileTools, "Current geo tool for LMB")
        self.toolright = EnumConfigurable(mod, "EDIT_tiles.rmb", TileTools.Rect, TileTools, "Current geo tool for RMB")
        self.deleteleft = BoolConfigurable(mod, "EDIT_tiles.deletelmb", False, "Delete tiles with LMB")
        self.deleteright = BoolConfigurable(mod, "EDIT_tiles.deletermb", False, "Delete tiles with RMB")

        self.colortable = palette_to_colortable(QImage(self.palette_image.value))
        self.explorer = mod.tile_explorer
        self.tile: Tile | None = mod.manager.tiles["Four Holes"]
        self.tile_image = QPixmap(1, 1)
        self.tile_cols_image = QPixmap(1, 1)
        # self.tile_cols_painter = QPainter(self.tile_cols_image)
        self.tile_item: QGraphicsPixmapItem | None = None
        self.tile_cols_item: QGraphicsPixmapItem | None = None

        self.show_collisions.valueChanged.connect(self.hide_collisions)
        self.previewoption.valueChanged.connect(self.redraw_tile)
        self.vis_layer.valueChanged.connect(self.redraw_tile)
        self.module.drawoption.valueChanged.connect(self.redraw_tile)
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
        self.redraw_cols()

    def redraw_tile(self):
        if self.tile is None:
            return
        self.tile_image = return_tile_pixmap(self.tile, self.tile_preview_option, self.layer, self.colortable)
        if self.tile_item is not None:
            self.tile_item.setPixmap(self.tile_image)
            self.mouse_wheel_event(None)

    def redraw_cols(self):
        if self.tile is None:
            return
        self.tile_cols_image = collisions_image(self.tile)
        if self.tile_item is not None:
            self.tile_cols_item.setPixmap(self.tile_cols_image)
            self.mouse_wheel_event(None)

    def hide_collisions(self, value):
        self.tile_cols_item.setOpacity(1 if value else 0)

    def mouse_wheel_event(self, event: QWheelEvent):
        if self.tile is None:
            return
        if self.tile_preview_option == 0:
            self.tile_item.setScale(self.viewport.zoom * (CELLSIZE / SPRITESIZE))
        else:
            self.tile_item.setScale(self.viewport.zoom)
        self.tile_cols_item.setScale(self.viewport.zoom)

    @property
    def tile_preview_option(self):
        value = self.previewoption.value
        if self.previewoption.value == 7:
            value = self.mod.tilemodule.drawoption.value
        return value

    def mouse_move_event(self, event: QMoveEvent):
        if self.tile is None:
            return
        offset = tile_offset(self.tile)
        curpos = self.viewport.viewport_to_editor(self.mouse_pos)
        cellpos = curpos - offset
        pos = self.viewport.editor_to_viewport(cellpos)
        if self.tile_preview_option != 0:
            self.tile_item.setPos(pos - QPoint(self.tile.bfTiles, self.tile.bfTiles) * CELLSIZE * self.viewport.zoom)
        else:
            self.tile_item.setPos(pos)
        if self.mouse_left:
            if self.deleteleft.value:
                self.manager.level.history.last_element.add_move(curpos)
            else:
                self.manager.level.history.last_element.add_move(cellpos)
        if self.manager.level.inside(cellpos):
            self.manager.set_status(f"x: {cellpos.x()}, y: {cellpos.y()}, {self.manager.level['TE']['tlMatrix'][cellpos.x()][cellpos.y()]}")
        self.tile_cols_item.setPos(pos)

    def init_scene_items(self):
        self.tile_item = self.workscene.addPixmap(self.tile_image)
        self.tile_cols_item = self.workscene.addPixmap(self.tile_cols_image)
        self.redraw_tile()

    def remove_items_from_scene(self):
        self.tile_item.removeFromIndex()
        self.tile_cols_item.removeFromIndex()

    def mouse_press_event(self, event: QMouseEvent):
        offset = tile_offset(self.tile)
        point = self.viewport.viewport_to_editor(self.mouse_pos) - offset
        if self.mouse_left:
            self.tool_specific_press(self.toolleft.value, self.deleteleft.value)
        if self.mouse_left:
            self.tool_specific_press(self.toolright.value, self.deleteright.value)

    def tool_specific_press(self, tool: TileTools, delete: bool):
        fpos = self.viewport.viewport_to_editor(self.mouse_pos)
        if tool == TileTools.Pen:
            self.manager.level.add_history(TilePen(self.manager.level.history, fpos, self.tile, self.layer, delete))
