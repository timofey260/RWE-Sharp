from __future__ import annotations
from PySide6.QtCore import QPoint, Qt, QPointF
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from RWESharp.Core import CELLSIZE, SPRITESIZE
from RWESharp.Loaders import Tile, collisions_image, return_tile_pixmap
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BaseMod.tiles.tileExplorer import TileExplorer


class TilePreview(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.workscene = QGraphicsScene(self)
        self.setScene(self.workscene)
        # self.origin = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.topleft = self.workscene.addEllipse(0, 0, 1, 1, QColor(0, 0, 0, 0))
        self.tileimage = self.workscene.addPixmap(QPixmap())
        self.tilecolsimage = self.workscene.addPixmap(QPixmap())
        self.lastpos = QPoint()
        self.mouse_pos = QPoint()
        self.manager = None
        self.setMouseTracking(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.zoom = 1
        self.tile: Tile | None = None
        self.ui: TileExplorer | None = None

    def add_manager(self, manager, ui: TileExplorer):
        self.manager = manager
        self.ui = ui
        self.workscene.setSceneRect(0, 0, 1000, 1000)

    def preview_tile(self, tile):
        self.tile = tile
        self.tileimage.setOpacity(1)
        self.tileimage.setPixmap(return_tile_pixmap(self.tile, self.ui.synced_draw_option, self.ui.layer.value, self.ui.colortable))
        self.tilecolsimage.setPixmap(collisions_image(tile))
        if self.ui.synced_draw_option == 0:
            self.tileimage.setScale(self.zoom * (CELLSIZE / SPRITESIZE))
        else:
            self.tileimage.setScale(self.zoom)
        self.set_pos(QPoint(0, 0))
        self.verticalScrollBar().setValue(0)
        self.horizontalScrollBar().setValue(0)

    def set_pos(self, pos: QPointF | QPoint):
        if self.tile is None:
            return
        self.topleft.setPos(pos)
        if self.ui.synced_draw_option != 0:
            self.tileimage.setPos(self.topleft.pos() - QPoint(self.tile.bfTiles, self.tile.bfTiles) * CELLSIZE * self.zoom)
        else:
            self.tileimage.setPos(self.topleft.pos())
        self.tilecolsimage.setPos(self.topleft.pos())

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.pos()
        offset = event.pos() - self.lastpos
        if event.buttons() & Qt.MouseButton.AllButtons:
            self.set_pos(self.topleft.pos() + offset)
        self.lastpos = event.pos()

    def mousePressEvent(self, event):
        self.setCursor(Qt.CursorShape.SizeAllCursor)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def wheelEvent(self, event):
        pointbefore = self.viewport_to_editor_float(self.mouse_pos.toPointF())
        self.zoom = max(0.01, self.zoom + (event.angleDelta().y() * (-1 if event.inverted() else 1) / 800))
        if self.ui.synced_draw_option == 0:
            self.tileimage.setScale(self.zoom * (CELLSIZE / SPRITESIZE))
        else:
            self.tileimage.setScale(self.zoom)
        self.tilecolsimage.setScale(self.zoom)
        offset = (self.viewport_to_editor_float(self.mouse_pos.toPointF()) - pointbefore) * CELLSIZE * self.zoom
        self.set_pos(self.topleft.pos() + offset)

    def viewport_to_editor_float(self, point: QPointF) -> QPointF:
        npoint = point + QPointF(self.horizontalScrollBar().value(), self.verticalScrollBar().value()) - self.tileimage.pos()
        npoint.setX(npoint.x() / (CELLSIZE * self.zoom))
        npoint.setY(npoint.y() / (CELLSIZE * self.zoom))
        return npoint

