from PySide6.QtCore import QRect, Qt, Slot
from PySide6.QtGui import QBrush, QColor
from RWESharp.Renderable import RenderTexture
from RWESharp.Core import CONSTS, CELLSIZE, SPRITESIZE
from RWESharp.Loaders import colortable


class TileRenderTexture(RenderTexture):
    def __init__(self, module, depth, tilelayer):
        super().__init__(module, depth)
        self.tilelayer = tilelayer

    def draw_layer(self, clear=False):
        if clear:
            self.image.fill(QColor(0, 0, 0, 0))
            # self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Source)
            # for xp, x in enumerate(self.manager.level["TE"]["tlMatrix"]):
            #     for yp, y in enumerate(x):
            #         self.painter.fillRect(QRect(xp * CELLSIZE, yp * CELLSIZE, CELLSIZE, CELLSIZE), QColor(0, 0, 0, 0))
            # self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        for xp, x in enumerate(self.manager.level["TE"]["tlMatrix"]):
            for yp, y in enumerate(x):
                self.draw_tile(xp, yp)
        self.redraw()

    @Slot(bool)
    @Slot(Qt.CheckState)
    def redraw_mats(self, state: bool | Qt.CheckState):
        if isinstance(state, bool):
            pass #todo
        for xp, x in enumerate(self.manager.level["TE"]["tlMatrix"]):
            for yp, y in enumerate(x):
                if y[self.tilelayer]["tp"] == "material":
                    self.draw_tile(xp, yp)
        self.redraw()

    def color_colortable(self, color: QColor) -> list[int]:
        table = []
        mult = 1
        table = []
        for i in range(3):
            for i2 in range(10):
                newcol = QColor.fromHsv(color.hue(), color.saturation(), color.value() - 90 + (30 * i + i2))
                table.append(newcol.rgba())
        table.append(QColor(0, 0, 0, 0).rgba())
        return table

    def draw_tile(self, x: int, y: int):
        # drawrect = QRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
        tile = self.manager.level.TE_data(x, y, self.tilelayer)
        match tile["tp"]:
            case "default":
                return
            case "material":
                if self.module.drawoption.value == 0:
                    sz = CONSTS.get("materialsize", [6, 8])
                    self.painter.setBrush(QBrush(QColor(*CONSTS.get("materials", {}).get(tile["data"], [255, 0, 0, 255]))))
                    self.painter.setPen(Qt.PenStyle.NoPen)
                    self.painter.drawRoundedRect(x * CELLSIZE + sz[0], y * CELLSIZE + sz[0], sz[1], sz[1], 2, 2)
                elif self.module.drawoption.value == 3:
                    self.painter.fillRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE, QColor(122, 0, 0, 255))
            # old version
            # case "tileBody":
            #     pointer = fromarr(tile["data"][0], "point")
            #     if self.layer != tile["data"][1] - 1:
            #         # drawing arrow
            #         # self.painter.setPen(Qt.PenStyle.DashLine)
            #         # self.painter.setPen(QColor(255, 0, 0, 255))
            #         self.painter.setPen(QPen(QColor(255, 0, 0, 255), 2))
            #         self.painter.drawLines([
            #             QLine(x * CELLSIZE + 10, y * CELLSIZE + 3, x * CELLSIZE + 10, y * CELLSIZE + 17),
            #             QLine(x * CELLSIZE + 10, y * CELLSIZE + 3, x * CELLSIZE + 5, y * CELLSIZE + 8),
            #             QLine(x * CELLSIZE + 10, y * CELLSIZE + 3, x * CELLSIZE + 15, y * CELLSIZE + 8)
            #         ])
            #     pointer = [pointer[0] - 1, pointer[1] - 1]
            #     newtile = self.manager.level.TE_data(pointer[0], pointer[1], tile["data"][1] - 1)
            #     if newtile["tp"] != "tileHead":
            #         print("uuh error")
            #         return
            #     foundtile = self.manager.tiles[newtile["data"][1]]
            #     if foundtile == None:
            #         print("uuh tile not found")
            #         return
            #     cposxo = pointer[0] - int((foundtile.size[0] * .5) + .5) + 1
            #     cposyo = pointer[1] - int((foundtile.size[1] * .5) + .5) + 1
            #     offset = [x - cposxo, y - cposyo]
            #     if offset[0] > foundtile.size[0] or offset[1] > foundtile.size[1]:
            #         print("broken tile size")
            #         return
            #     sourcerect = QRect(offset[0] * SPRITESIZE, offset[1] * SPRITESIZE, SPRITESIZE, SPRITESIZE)
            #     self.painter.drawImage(drawrect, foundtile.image, sourcerect)
            # case "tileHead":
            #     foundtile = self.manager.tiles[tile["data"][1]]
            #     cposxo = int((foundtile.size[0] * .5) + .5) - 1
            #     cposyo = int((foundtile.size[1] * .5) + .5) - 1
            #     sourcerect = QRect(cposxo * SPRITESIZE, cposyo * SPRITESIZE, SPRITESIZE, SPRITESIZE)
            #     self.painter.drawImage(drawrect, foundtile.image, sourcerect)

            # new one
            case "tileHead":
                foundtile = self.manager.tiles[tile["data"][1]]
                cposxo = int((foundtile.size.x() * .5) + .5) - 1
                cposyo = int((foundtile.size.y() * .5) + .5) - 1
                if self.module.drawoption.value == 1:
                    drawrect = QRect((x - cposxo - foundtile.bfTiles) * CELLSIZE,
                                     (y - cposyo - foundtile.bfTiles) * CELLSIZE,
                                     CELLSIZE * (foundtile.size.x() + foundtile.bfTiles * 2),
                                     CELLSIZE * (foundtile.size.y() + foundtile.bfTiles * 2))  # it works trust

                    self.painter.drawPixmap(drawrect, foundtile.image2)

                elif self.module.drawoption.value in [2, 3, 4, 5, 6]:
                    drawrect = QRect((x - cposxo - foundtile.bfTiles) * CELLSIZE,
                                     (y - cposyo - foundtile.bfTiles) * CELLSIZE,
                                     CELLSIZE * (foundtile.size.x() + foundtile.bfTiles * 2),
                                     CELLSIZE * (foundtile.size.y() + foundtile.bfTiles * 2))  # it works trust
                    if self.module.drawoption.value == 3:
                        foundtile.image3.setColorTable(colortable[self.tilelayer])
                    elif self.module.drawoption.value == 2:
                        foundtile.image3.setColorTable(self.color_colortable(foundtile.color))
                    else:
                        col = self.module.drawoption.value - 4
                        foundtile.image3.setColorTable(self.module.colortable[col][self.tilelayer])
                    self.painter.drawImage(drawrect, foundtile.image3)
                else:
                    sourcerect = QRect(0, 0, SPRITESIZE * foundtile.size.x(), SPRITESIZE * foundtile.size.y())
                    drawrect = QRect((x - cposxo) * CELLSIZE, (y - cposyo) * CELLSIZE, CELLSIZE * foundtile.size.x(), CELLSIZE * foundtile.size.y())  # it works trust
                    self.painter.drawPixmap(drawrect, foundtile.image, sourcerect)

    def draw_material(self):
        pass