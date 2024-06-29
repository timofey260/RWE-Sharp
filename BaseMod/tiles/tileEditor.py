from __future__ import annotations

import os
from typing import TYPE_CHECKING

from PySide6.QtCore import QPoint
from PySide6.QtGui import QPixmap, QWheelEvent, QMoveEvent, QImage, QMouseEvent
from PySide6.QtWidgets import QGraphicsPixmapItem

from RWESharp.Configurable import IntConfigurable, BoolConfigurable, StringConfigurable
from RWESharp.Core import CELLSIZE, SPRITESIZE, PATH_FILES_IMAGES_PALETTES
from RWESharp.Loaders import Tile
from RWESharp.Loaders import palette_to_colortable, return_tile_pixmap, collisions_image, tile_offset
from RWESharp.Modify import EditorMode

from BaseMod.tiles.tileHistory import TilePen, PlacedTile
from core import lingoIO
from core.Loaders.Tile import Tile
from core.Loaders.TileLoader import tile_offset
from core.RWELevel import RWELevel

if TYPE_CHECKING:
    from BaseMod.baseMod import BaseMod


def point_collision(level: RWELevel, pos: QPoint, layer: int, tilepos: QPoint, tile: Tile) -> bool:
    tiledata = level.tile_data(pos, layer)
    tp = tiledata.get("tp", "default")
    # data = tiledata.get("data", 0)
    if tp != "default":
        return False
    geodata = level.geo_data(pos, layer)[0]
    try:
        collision = tile.cols[0][tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if geodata != collision and geodata != -1:
        return False
    # next layer
    if not isinstance(tile.cols[1], list) or layer + 1 > 2:
        return True
    geodata = level.geo_data(pos, layer + 1)[0]
    try:
        collision = tile.cols[1][tilepos.x() * tile.size.height() + tilepos.y()]
    except IndexError:
        collision = 1
    if geodata != collision and geodata != -1:
        return False
    return True


def check_collisions(level: RWELevel, pos: QPoint, layer: int, tile: Tile) -> bool:
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            levelpos = QPoint(x, y)
            tilepos = levelpos - pos
            if not level.inside(levelpos):
                continue
            result = point_collision(level, levelpos, layer, tilepos, tile)
            if not result:
                return False
    return True


def can_place(level: RWELevel,
              pos: QPoint,
              layer: int,
              tile: Tile,
              area: list[list[bool]],
              area2: list[list[bool]],
              force_place: bool,
              force_geometry: bool) -> bool:
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return False
    # if area is available
    for x in range(pos.x(), pos.x() + tile.size.width()):
        for y in range(pos.y(), pos.y() + tile.size.height()):
            if not level.inside(QPoint(x, y)):
                continue
            if not area[x][y]:
                return False
            if isinstance(tile.cols[1], list) and not area2[x][y]:
                return False
    # mf got through our defence
    if force_place or force_geometry:
        return False
    return check_collisions(level, pos, layer, tile)


def place_tile(level: RWELevel,
               pos: QPoint,
               layer: int,
               tile: Tile,
               area: list[list[bool]] = None,
               area2: list[list[bool]] = None,
               force_place: bool = False,
               force_geometry: bool = False) -> PlacedTile | None:
    if tile.type == "material":
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "material", "data": tile.name}
        level.manager.basemod.tilemodule.get_layer(layer).draw_tile(pos)
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return PlacedTile(pos, layer, tile)
    headpos = tile_offset(tile) + pos
    if not level.inside(headpos):
        return None
    for x in range(tile.size.width()):
        for y in range(tile.size.height()):
            tilepos = QPoint(x, y) + pos
            if not level.inside(tilepos):
                continue
            if area is not None:
                area[tilepos.x()][tilepos.y()] = False
            # area2[x][y] = False
            try:
                col = tile.cols[0][x * tile.size.height() + y]
            except IndexError:
                col = 1
            if isinstance(tile.cols[1], list) and layer + 1 < 3:
                if area2 is not None:
                    area2[tilepos.x()][tilepos.y()] = False
                try:
                    col = tile.cols[1][x * tile.size.height() + y]
                except IndexError:
                    col = 1
                if col != -1:
                    level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer + 1] = \
                        {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x(), headpos.y()], "point"), layer]}
            if col == -1:
                continue
            if tilepos == headpos:
                level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer] = {"tp": "tileHead", "data": [
                    lingoIO.makearr([tile.cat.x(), tile.cat.y()], "point"), tile.name]}
                continue
            level.data["TE"]["tlMatrix"][tilepos.x()][tilepos.y()][layer] = \
                {"tp": "tileBody", "data": [lingoIO.makearr([headpos.x(), headpos.y()], "point"), layer]}
    level.manager.basemod.tilemodule.get_layer(layer).draw_tile(headpos)
    return PlacedTile(pos, layer, tile)


def remove_tile(level: RWELevel, pos: QPoint, layer: int):
    if not level.inside(pos):
        return
    data = level.tile_data(pos, layer)
    tp = data.get("tp", "default")
    head = [lingoIO.makearr([pos.x(), pos.y()], "point"), layer]
    if tp == "default":
        return
    elif tp == "material":
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "default", "data": 0}
        level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(pos)
        level.manager.basemod.tilemodule.get_layer(layer).redraw()
        return
    elif tp == "tileBody":
        head = data.get("data")
        level.data["TE"]["tlMatrix"][pos.x()][pos.y()][layer] = {"tp": "default", "data": 0}
        if head is None:
            return
    headpos = QPoint(*lingoIO.fromarr(head[0], "point"))
    headdata = level.tile_data(headpos, head[1])
    if headdata.get("tp") != "tileHead":
        return
    foundtile = level.manager.tiles[headdata.get("data")[1]]
    if foundtile is None:
        return
    offset = tile_offset(foundtile)
    for x in range(foundtile.size.width()):
        for y in range(foundtile.size.height()):
            bodypos = QPoint(x, y) + headpos - offset
            if not level.inside(bodypos):
                continue
            try:
                col = foundtile.cols[0][x * foundtile.size.height() + y]
            except IndexError:
                col = 1
            if isinstance(foundtile.cols[1], list) and layer + 1 < 3:
                try:
                    col2 = foundtile.cols[1][x * foundtile.size.height() + y]
                except IndexError:
                    col2 = 1
                if col2 != -1:
                    level.manager.basemod.tilemodule.get_layer(layer + 1).clean_pixel(bodypos)
                    level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer + 1] = {"tp": "default", "data": 0}
            if col == -1:
                continue
            level.manager.basemod.tilemodule.get_layer(layer).clean_pixel(bodypos)
            level.data["TE"]["tlMatrix"][bodypos.x()][bodypos.y()][layer] = {"tp": "default", "data": 0}


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
        cellpos = self.viewport.viewport_to_editor(self.mouse_pos) - offset
        pos = self.viewport.editor_to_viewport(cellpos)
        if self.tile_preview_option != 0:
            self.tile_item.setPos(pos - QPoint(self.tile.bfTiles, self.tile.bfTiles) * CELLSIZE * self.viewport.zoom)
        else:
            self.tile_item.setPos(pos)
        if self.mouse_left:
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
            self.manager.level.add_history(TilePen(self.manager.level.history, point, self.tile, self.layer))
