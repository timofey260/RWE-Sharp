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
        self.tileindex: list[QGraphicsPixmapItem | QGraphicsRectItem] = []

    def fill_scene(self):
        self.clear_scene()
        self.tilescene.setSceneRect(0, 0, self.viewport.level.level_width * CELLSIZE, self.viewport.level.level_height * CELLSIZE)
        # air = QPixmap(1, 1)
        # air.fill(QColor(0, 0, 0, 0))
        matpen = QPen(QColor(0, 0, 0, 255 if self.module.ui.matborder.value else 0), 0)
        for x in range(self.level.level_width):
            for y in range(self.level.level_height):
                tile = self.level.l_tiles.tile_data(QPoint(x, y), self.tilelayer)
                if isinstance(tile, PlacedTileHead):
                    item = self.tilescene.addPixmap(tile.tile.image)
                    item.setPos(QPoint(x * CELLSIZE, y * CELLSIZE) - tile.tile.top_left * CELLSIZE)
                    item.setScale(20 / 16)
                    tile.graphics = item
                    self.tileindex.append(item)
                elif isinstance(tile, PlacedMaterial):
                    sz = CONSTS.get("materialsize", [6, 8])
                    # self.painter.setBrush(QBrush(QColor(*CONSTS.get("materials", {}).get(tile.tile.name, [255, 0, 0, 255]))))
                    # self.painter.setPen(Qt.PenStyle.NoPen)
                    # self.painter.drawRoundedRect(x * CELLSIZE + sz[0], y * CELLSIZE + sz[0], sz[1], sz[1], 2, 2)
                    item = self.tilescene.addRect(x * CELLSIZE + sz[0], y * CELLSIZE + sz[0], sz[1], sz[1],
                                                  pen=matpen,
                                                  brush=tile.tile.color)
                    #item = self.tilescene.addPixmap(tile.tile.image)
                    #item.setPos(QPoint(x * CELLSIZE, y * CELLSIZE))
                    #item.setScale(16 / 20)
                    tile.graphics = item
                    self.tileindex.append(item)
        self.tilescene.render(self.painter)

    def render_layer(self):
        self.image.fill(QColor(0, 0, 0, 0))
        self.tilescene.render(self.painter)
        self.redraw()

    def change_material_border(self, enabled):
        matpen = QPen(QColor(0, 0, 0, 255 if enabled else 0), 0)
        for i in self.tileindex:
            if isinstance(i, QGraphicsRectItem):
                i.setPen(matpen)
        self.render_layer()

    def clear_scene(self):
        self.tilescene.clear()
        self.tileindex.clear()

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

    @Slot(bool)
    @Slot(Qt.CheckState)
    def redraw_mats(self, state: bool | Qt.CheckState):
        if isinstance(state, bool):
            pass #todo
        for xp, x in enumerate(self.viewport.level["TE"]["tlMatrix"]):
            for yp, y in enumerate(x):
                if y[self.tilelayer]["tp"] == "material":
                    self.draw_tile(QPoint(xp, yp))
        self.redraw()

    def clean_pixel(self, pos: QPoint):
        self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
        self.painter.eraseRect(QRect(pos * CELLSIZE, QSize(CELLSIZE, CELLSIZE)))
        self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)

    def clean_tile(self, pos: QPoint):
        ptile = self.viewport.level.l_tiles(pos, self.tilelayer)
        if ptile is None:
            return
        tile: Tile = ptile.tile
        # todo

    def level_resized(self):
        super().level_resized()
        self.tilescene.setSceneRect(0, 0, self.viewport.level.level_width * CELLSIZE, self.viewport.level.level_height * CELLSIZE)
        # todo other tile bullshit
        self.draw_layer(True)

    def draw_tile(self, pos: QPoint):
        # drawrect = QRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
        tile = self.viewport.level.l_tiles(pos, self.tilelayer)
        x = pos.x()
        y = pos.y()
        if isinstance(tile, PlacedMaterial):
            if self.ui.drawoption.value == 0:
                sz = CONSTS.get("materialsize", [6, 8])
                self.painter.setBrush(QBrush(QColor(*CONSTS.get("materials", {}).get(tile.tile.name, [255, 0, 0, 255]))))
                self.painter.setPen(Qt.PenStyle.NoPen)
                self.painter.drawRoundedRect(x * CELLSIZE + sz[0], y * CELLSIZE + sz[0], sz[1], sz[1], 2, 2)
            elif self.ui.drawoption.value == 3:
                self.painter.fillRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE, QColor(122, 0, 0, 255))
        elif isinstance(tile, PlacedTileHead):
            foundtile = tile.tile
            if foundtile is None:
                return
            cposxo = int((foundtile.size.width() * .5) + .5) - 1
            cposyo = int((foundtile.size.height() * .5) + .5) - 1
            if self.ui.drawoption.value == 0:
                sourcerect = QRect(0, 0, SPRITESIZE * foundtile.size.width(), SPRITESIZE * foundtile.size.height())
                drawrect = QRect((x - cposxo) * CELLSIZE, (y - cposyo) * CELLSIZE, CELLSIZE * foundtile.size.width(), CELLSIZE * foundtile.size.height())  # it works trust
                self.painter.drawPixmap(drawrect, foundtile.image, sourcerect)
            elif self.ui.drawoption.value == 1:
                drawrect = QRect((x - cposxo - foundtile.bfTiles) * CELLSIZE,
                                 (y - cposyo - foundtile.bfTiles) * CELLSIZE,
                                 CELLSIZE * (foundtile.size.width() + foundtile.bfTiles * 2),
                                 CELLSIZE * (foundtile.size.height() + foundtile.bfTiles * 2))  # it works trust

                self.painter.drawPixmap(drawrect, foundtile.image2)

            else:
                drawrect = QRect((x - cposxo - foundtile.bfTiles) * CELLSIZE,
                                 (y - cposyo - foundtile.bfTiles) * CELLSIZE,
                                 CELLSIZE * (foundtile.size.width() + foundtile.bfTiles * 2),
                                 CELLSIZE * (foundtile.size.height() + foundtile.bfTiles * 2))  # it works trust
                if self.ui.drawoption.value == 3:
                    foundtile.image3.setColorTable(colortable[self.tilelayer])
                elif self.ui.drawoption.value == 2:
                    foundtile.image3.setColorTable(color_colortable(foundtile.color))
                else:
                    col = self.ui.drawoption.value - 4
                    foundtile.image3.setColorTable(self.ui.colortable[col][self.tilelayer])
                self.painter.drawImage(drawrect, foundtile.image3)

    def draw_material(self):
        pass