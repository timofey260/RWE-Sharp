from core.Renderable.RenderImage import RenderImage
from core.Loaders.Tile import Tile
from core.info import CELLSIZE
from core.Loaders.TileLoader import palette_to_colortable, return_tile_pixmap, collisions_image, tile_offset
from PySide6.QtCore import QSize, QPoint
from PySide6.QtGui import QPixmap


class RenderTile(RenderImage):
    def __init__(self, mod, depth, layer: int):
        super().__init__(mod, depth, QSize(1, 1))
        self.colsimage = QPixmap(1, 1)
        self.colsimage_rendered = None
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
        self.colsimage_rendered = self.viewport.workscene.addPixmap(self.colsimage)

    def remove_graphics(self, viewport):
        super().remove_graphics(viewport)
        self.colsimage_rendered.removeFromIndex()
        self.colsimage_rendered = None

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
        if self.drawoption == 0:
            zoom = zoom / 16 * 20
        super().zoom_event(zoom)
