from PySide6.QtCore import QRect, Qt, Slot, QPoint, QSize
from PySide6.QtGui import QBrush, QColor, QPainter, QPixmap, QPen
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem

from RWESharp.Core import CONSTS, CELLSIZE, SPRITESIZE
from RWESharp.Loaders import colortable, color_colortable, Tile
from RWESharp.Renderable import RenderLevelImage
from BaseMod.tiles.tileUtils import PlacedMaterial, PlacedTileHead, PlacedTileBody


class TileRenderLevelImage(RenderLevelImage):
    def __init__(self, module, depth, tilelayer):
        super().__init__(module, depth)
        self.module = module
        self.ui = self.module.ui
        self.tilelayer = tilelayer
        self.tilescene = QGraphicsScene(0, 0, 100, 100)
        # self.tileindex: list[QGraphicsPixmapItem | QGraphicsRectItem] = []

    def fill_scene(self):
        self.clear_scene()
        self.tilescene.setSceneRect(0, 0, self.viewport.level.level_width * CELLSIZE, self.viewport.level.level_height * CELLSIZE)
        # air = QPixmap(1, 1)
        # air.fill(QColor(0, 0, 0, 0))
        for x in range(self.level.level_width):
            for y in range(self.level.level_height):
                tile = self.level.l_tiles.tile_data(QPoint(x, y), self.tilelayer)
                if isinstance(tile, PlacedTileHead):
                    self.add_tile_graphics(QPoint(x, y))
                elif isinstance(tile, PlacedMaterial):
                    self.add_material_graphics(QPoint(x, y))
        self.tilescene.render(self.painter)

    def add_tile_graphics(self, pos):
        tile = self.level.l_tiles.tile_data(pos, self.tilelayer)
        item = self.tilescene.addPixmap(tile.tile.return_tile_pixmap(self.ui.drawoption.value, self.tilelayer, self.ui.colortable))
        item.setPos(pos * CELLSIZE - tile.tile.option_based_top_left(self.ui.drawoption.value) * CELLSIZE)
        if self.ui.drawoption.value == 0:
            item.setScale(20 / 16)
        item.setZValue(tile.tile.size.height() * tile.tile.size.width())
        tile.graphics = item

    def add_material_graphics(self, pos):
        tile = self.level.l_tiles.tile_data(pos, self.tilelayer)
        sz = CONSTS.get("materialsize", [6, 8])
        if self.ui.drawoption.value == 3:
            item = self.tilescene.addRect(pos.x() * CELLSIZE, pos.y() * CELLSIZE, CELLSIZE, CELLSIZE,
                                          pen=QColor(122, 0, 0, 255),
                                          brush=QColor(122, 0, 0, 255))
            item.setZValue(-100)
            tile.graphics = item
            return
        matpen = QPen(QColor(0, 0, 0, 255 if self.ui.matborder.value else 0), 0)
        item = self.tilescene.addRect(pos.x() * CELLSIZE + sz[0], pos.y() * CELLSIZE + sz[0], sz[1], sz[1],
                                      pen=matpen,
                                      brush=tile.tile.color)
        item.setZValue(-100)
        tile.graphics = item

    def init_graphics(self, viewport):
        super().init_graphics(viewport)
        self.fill_scene()
        self.redraw()

    def render_layer(self):
        self.image.fill(QColor(0, 0, 0, 0))
        self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        self.tilescene.render(self.painter)
        self.redraw()

    def change_material_border(self, enabled):
        matpen = QPen(QColor(0, 0, 0, 255 if enabled else 0), 0)
        for x in range(self.level.level_width):
            for y in range(self.level.level_height):
                tile = self.level.l_tiles.tile_data_xy(x, y, self.tilelayer)
                if isinstance(tile, PlacedMaterial) and tile.graphics is not None:
                    tile.graphics.setPen(matpen)
        self.render_layer()

    def clear_scene(self):
        self.tilescene.clear()

    def draw_layer(self, clear=False):
        if clear:
            self.image.fill(QColor(0, 0, 0, 0))
            # self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
            # for xp, x in enumerate(self.manager.level["TE"]["tlMatrix"]):
            #     for yp, y in enumerate(x):
            #         self.painter.fillRect(QRect(xp * CELLSIZE, yp * CELLSIZE, CELLSIZE, CELLSIZE), QColor(0, 0, 0, 0))
            # self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        """
        for xp, x in enumerate(self.viewport.level["TE"]["tlMatrix"]):
            for yp, y in enumerate(x):
                self.draw_tile(QPoint(xp, yp))"""

        self.fill_scene()
        self.render_layer()

    def level_resized(self):
        super().level_resized()
        self.tilescene.setSceneRect(0, 0, self.viewport.level.level_width * CELLSIZE, self.viewport.level.level_height * CELLSIZE)
        # todo other tile bullshit
        self.draw_layer(True)

    def render_rect(self, rect: QRect):
        self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
        self.painter.fillRect(rect, QColor(0, 0, 0, 0))
        self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        self.tilescene.render(self.painter, target=rect, source=rect)

    def draw_tile(self, pos: QPoint, render: bool):
        tile = self.viewport.level.l_tiles(pos, self.tilelayer)
        if tile is not None and isinstance(tile, PlacedTileBody) and tile.graphics is not None:
            tile.graphics.removeFromIndex()
            tile.graphics = None
        if isinstance(tile, PlacedTileHead):
            self.add_tile_graphics(pos)
            # tile.graphics: QGraphicsPixmapItem
            if render:
                self.render_rect(tile.tile_bounds)
        elif isinstance(tile, PlacedMaterial):
            self.add_material_graphics(pos)
            # tile.graphics: QGraphicsPixmapItem
            if render:
                self.render_rect(tile.tile_bounds)


    # def draw_tile(self, pos: QPoint):
    #     # drawrect = QRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
    #     tile = self.viewport.level.l_tiles(pos, self.tilelayer)
    #     x = pos.x()
    #     y = pos.y()
    #     if isinstance(tile, PlacedMaterial):
    #         if self.ui.drawoption.value == 0:
    #             sz = CONSTS.get("materialsize", [6, 8])
    #             self.painter.setBrush(QBrush(QColor(*CONSTS.get("materials", {}).get(tile.tile.name, [255, 0, 0, 255]))))
    #             self.painter.setPen(Qt.PenStyle.NoPen)
    #             self.painter.drawRoundedRect(x * CELLSIZE + sz[0], y * CELLSIZE + sz[0], sz[1], sz[1], 2, 2)
    #         elif self.ui.drawoption.value == 3:
    #             self.painter.fillRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE, QColor(122, 0, 0, 255))
    #     elif isinstance(tile, PlacedTileHead):
    #         foundtile = tile.tile
    #         if foundtile is None:
    #             return
    #         cposxo = int((foundtile.size.width() * .5) + .5) - 1
    #         cposyo = int((foundtile.size.height() * .5) + .5) - 1
    #         if self.ui.drawoption.value == 0:
    #             sourcerect = QRect(0, 0, SPRITESIZE * foundtile.size.width(), SPRITESIZE * foundtile.size.height())
    #             drawrect = QRect((x - cposxo) * CELLSIZE, (y - cposyo) * CELLSIZE, CELLSIZE * foundtile.size.width(), CELLSIZE * foundtile.size.height())  # it works trust
    #             self.painter.drawPixmap(drawrect, foundtile.image, sourcerect)
    #         elif self.ui.drawoption.value == 1:
    #             drawrect = QRect((x - cposxo - foundtile.bfTiles) * CELLSIZE,
    #                              (y - cposyo - foundtile.bfTiles) * CELLSIZE,
    #                              CELLSIZE * (foundtile.size.width() + foundtile.bfTiles * 2),
    #                              CELLSIZE * (foundtile.size.height() + foundtile.bfTiles * 2))  # it works trust
    #
    #             self.painter.drawPixmap(drawrect, foundtile.image2)
    #
    #         else:
    #             drawrect = QRect((x - cposxo - foundtile.bfTiles) * CELLSIZE,
    #                              (y - cposyo - foundtile.bfTiles) * CELLSIZE,
    #                              CELLSIZE * (foundtile.size.width() + foundtile.bfTiles * 2),
    #                              CELLSIZE * (foundtile.size.height() + foundtile.bfTiles * 2))  # it works trust
    #             if self.ui.drawoption.value == 3:
    #                 foundtile.image3.setColorTable(colortable[self.tilelayer])
    #             elif self.ui.drawoption.value == 2:
    #                 foundtile.image3.setColorTable(color_colortable(foundtile.color))
    #             else:
    #                 col = self.ui.drawoption.value - 4
    #                 foundtile.image3.setColorTable(self.ui.colortable[col][self.tilelayer])
    #             self.painter.drawImage(drawrect, foundtile.image3)
