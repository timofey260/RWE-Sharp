from core.Modify.RenderTexture import RenderTexture
from PySide6.QtCore import QRect, QLine, Qt
from PySide6.QtGui import QBrush, QColor, QPen
from core.info import CONSTS, CELLSIZE, SPRITESIZE
from core.lingoIO import fromarr


class TileRenderTexture(RenderTexture):
    def __init__(self, module, layer):
        super().__init__(module)
        self.layer = layer
        self.draw()

    def draw(self):
        for xp, x in enumerate(self.manager.level["TE"]["tlMatrix"]):
            for yp, y in enumerate(x):
                self.draw_tile(xp, yp)

    def draw_tile(self, x: int, y: int, clear: bool = False):
        tile = self.manager.level.TE_data(x, y, self.layer)
        match tile["tp"]:
            case "default":
                return
            case "material":
                sz = CONSTS.get("materialsize", [6, 8])
                self.painter.setBrush(QBrush(QColor(*CONSTS.get("materials", {}).get(tile["data"], [255, 0, 0, 255]))))
                self.painter.setPen(Qt.PenStyle.NoPen)
                self.painter.drawRoundedRect(x * CELLSIZE + sz[0], y * CELLSIZE + sz[0], sz[1], sz[1], 2, 2)
            case "tileBody":
                pointer = fromarr(tile["data"][0], "point")
                if self.layer != tile["data"][1] - 1:
                    # drawing arrow
                    # self.painter.setPen(Qt.PenStyle.DashLine)
                    # self.painter.setPen(QColor(255, 0, 0, 255))
                    self.painter.setPen(QPen(QColor(255, 0, 0, 255), 2))
                    self.painter.drawLines([
                        QLine(x * CELLSIZE + 10, y * CELLSIZE + 3, x * CELLSIZE + 10, y * CELLSIZE + 17),
                        QLine(x * CELLSIZE + 10, y * CELLSIZE + 3, x * CELLSIZE + 5, y * CELLSIZE + 8),
                        QLine(x * CELLSIZE + 10, y * CELLSIZE + 3, x * CELLSIZE + 15, y * CELLSIZE + 8)
                    ])
                pointer = [pointer[0] - 1, pointer[1] - 1]
                newtile = self.manager.level.TE_data(pointer[0], pointer[1], tile["data"][1] - 1)
                if newtile["tp"] != "tileHead":
                    print("uuh error")
                    return
                foundtile = self.manager.tiles[newtile["data"][1]]
                if foundtile == None:
                    print("uuh tile not found")
                    return
                cposxo = pointer[0] - int((foundtile.size[0] * .5) + .5) + 1
                cposyo = pointer[1] - int((foundtile.size[1] * .5) + .5) + 1
                offset = [x - cposxo, y - cposyo]
                if offset[0] > foundtile.size[0] or offset[1] > foundtile.size[1]:
                    print("broken tile size")
                    return
                drawrect = QRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
                sourcerect = QRect(offset[0] * SPRITESIZE, offset[1] * SPRITESIZE, SPRITESIZE, SPRITESIZE)
                self.painter.drawImage(drawrect, foundtile.image, sourcerect)
            case "tileHead":
                foundtile = self.manager.tiles[tile["data"][1]]
                cposxo = int((foundtile.size[0] * .5) + .5) - 1
                cposyo = int((foundtile.size[1] * .5) + .5) - 1
                drawrect = QRect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
                sourcerect = QRect(cposxo * SPRITESIZE, cposyo * SPRITESIZE, SPRITESIZE, SPRITESIZE)
                self.painter.drawImage(drawrect, foundtile.image, sourcerect)
