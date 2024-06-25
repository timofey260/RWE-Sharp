from __future__ import annotations
from RWESharp.Modify import EditorMode
from RWESharp.Loaders import Tile
from RWESharp.Core import CELLSIZE, SPRITESIZE
from RWESharp.Configurable import IntConfigurable
from PySide6.QtGui import QPixmap, QColor, QPainter, QWheelEvent, QMoveEvent, QPen, QBrush
from PySide6.QtWidgets import QGraphicsPixmapItem
from PySide6.QtCore import QPoint, QRect, QSize, Qt, QLine
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BaseMod.baseMod import BaseMod


class TileEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        mod: BaseMod
        self.previewmode = IntConfigurable(mod, "EDIT_tiles.previewMode", 0, "tile preview mode")
        self.explorer = mod.tile_explorer
        self.tile: Tile | None = mod.manager.tiles["Four Holes"]
        self.explorer.tileSelected.connect(self.add_tile)
        self.tile_image = QPixmap(1, 1)
        self.tile_cols_image = QPixmap(1, 1)
        # self.tile_cols_painter = QPainter(self.tile_cols_image)
        self.tile_item: QGraphicsPixmapItem | None = None
        self.tile_cols_item: QGraphicsPixmapItem | None = None

    def add_tile(self, tiles: list[Tile]):
        self.tile = tiles[0]
        self.redraw_tile()

    def redraw_tile(self):
        if self.tile is None:
            return
        self.tile_image = self.tile.image
        self.redraw_cols()
        if self.tile_item is not None:
            self.tile_item.setPixmap(self.tile_image)
            self.tile_cols_item.setPixmap(self.tile_cols_image)
            self.tile_item.setScale(self.viewport.zoom * (CELLSIZE / SPRITESIZE))
            self.tile_cols_item.setScale(self.viewport.zoom)

    def redraw_cols(self):
        self.tile_cols_image = QPixmap((self.tile.size + QSize(self.tile.bfTiles * 2, self.tile.bfTiles * 2)) * CELLSIZE)
        self.tile_cols_image.fill(QColor(0, 0, 0, 0))
        painter = QPainter(self.tile_cols_image)
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.setPen(QPen(QColor(255, 0, 0, 255), 2, Qt.PenStyle.DotLine))
        for i, v in enumerate(self.tile.cols[0]):
            pos = QPoint(i // self.tile.size.height(), i % self.tile.size.height()) * CELLSIZE
            endpos = pos + QPoint(CELLSIZE, CELLSIZE)
            match v:
                case 1:
                    painter.drawRect(QRect(pos, QSize(CELLSIZE - 2, CELLSIZE - 2)))
                case 0:
                    c = CELLSIZE / 2
                    painter.drawEllipse(pos + QPoint(c, c), c, c)
                case 2:
                    pos2 = QPoint(pos.x(), endpos.y())
                    painter.drawLines([QLine(pos, pos2), QLine(pos2, endpos), QLine(endpos, pos)])
                case 3:
                    pos2 = QPoint(pos.x(), endpos.y())
                    pos3 = QPoint(endpos.x(), pos.y())
                    painter.drawLines([QLine(pos2, endpos), QLine(endpos, pos3), QLine(pos3, pos2)])
                case 4:
                    pos2 = QPoint(pos.x(), endpos.y())
                    pos3 = QPoint(endpos.x(), pos.y())
                    painter.drawLines([QLine(pos, pos2), QLine(pos2, pos3), QLine(pos3, pos)])
                case 5:
                    pos3 = QPoint(endpos.x(), pos.y())
                    painter.drawLines([QLine(pos, endpos), QLine(endpos, pos3), QLine(pos3, pos)])

    def mouse_wheel_event(self, event: QWheelEvent):
        if self.tile is None:
            return
        if self.previewmode.value == 0:
            self.tile_item.setScale(self.viewport.zoom * (CELLSIZE / SPRITESIZE))
        self.tile_cols_item.setScale(self.viewport.zoom)

    def mouse_move_event(self, event: QMoveEvent):
        if self.tile is None:
            return
        offset = QPoint(int((self.tile.size.width() * 0.5) + .5) - 1, int((self.tile.size.height() * .5) + .5) - 1)

        pos = self.viewport.editor_to_viewport(self.viewport.viewport_to_editor(self.mouse_pos) - offset)
        self.tile_item.setPos(pos)
        self.tile_cols_item.setPos(pos)

    def init_scene_items(self):
        self.tile_item = self.workscene.addPixmap(self.tile_image)
        self.tile_cols_item = self.workscene.addPixmap(self.tile_image)
        self.redraw_tile()

    def remove_items_from_scene(self):
        self.tile_item.removeFromIndex()
        self.tile_cols_item.removeFromIndex()
