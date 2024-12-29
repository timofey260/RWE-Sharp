from core.Renderable.RenderImage import RenderImage
from core.Loaders.Tile import Tile
from core.info import CELLSIZE
from core.Loaders.TileLoader import palette_to_colortable, return_tile_pixmap, collisions_image, tile_offset
from PySide6.QtCore import QSize, QPoint
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem


class RenderTile(RenderImage):
    def __init__(self, module, depth, layer: int):
        super().__init__(module, depth, QSize(1, 1))
        self.colsimage = QPixmap(1, 1)
        self.colsimage_rendered = QGraphicsPixmapItem(self.colsimage)
        self.layer = layer
        self.tile = None
        self.drawoption = 0

    def set_tile(self, tile: Tile, colortable, option: int = 0):
        self.drawoption = option
        self.image = return_tile_pixmap(tile, self.drawoption, self.layer, colortable)
        self.colsimage = collisions_image(tile)
        self.redraw()
        self.tile = tile
        self.zoom_event(self.zoom)

    def redraw(self) -> None:
        super().redraw()
        self.colsimage_rendered.setPixmap(self.colsimage)

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.viewport.workscene.addItem(self.colsimage_rendered)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        viewport.workscene.removeItem(self.colsimage_rendered)

    def move_event(self, pos):
        if self.tile is None:
            return
        super().move_event(pos)
        self.colsimage_rendered.setPos(self.actual_offset)
        if self.drawoption == 0:
            self.renderedtexture.setPos(self.actual_offset)
            return
        self.renderedtexture.setPos(self.actual_offset - (QPoint(1, 1) * self.tile.bfTiles * CELLSIZE * self.zoom))

    def zoom_event(self, zoom):
        self.colsimage_rendered.setScale(zoom)
        self.scale = (20 / 16) if self.drawoption == 0 else 1
        super().zoom_event(zoom)
