from __future__ import annotations
from PySide6.QtGui import QImage, QColor, QPixmap, QPainter, QPen
from PySide6.QtCore import QPoint, QSize, QLine, Qt, QRect
from core.info import CELLSIZE
from dataclasses import dataclass

colortable = [[], [], []]
for l in range(3):
    for i in range(90):
        colortable[l].append(QColor(max(0, 90 + i - l * 30), 0, 0, 255).rgba())
            # colortable[l].append(QColor(91 + 30 * i + i2 - 10 * l, 0, 0, 255).rgba())
colortable[0].append(QColor(0, 0, 0, 0).rgba())
colortable[1].append(QColor(0, 0, 0, 0).rgba())
colortable[2].append(QColor(0, 0, 0, 0).rgba())


def color_colortable(color: QColor) -> list[int]:
    table = []
    # for i in range(3):
    #     for i2 in range(10):
    #         newcol = QColor.fromHsv(color.hue(), color.saturation(), color.value() - 90 + (30 * i + i2))
    #         table.append(newcol.rgba())
    for l in range(3):
        for i in range(30):
            table.append(QColor.fromHsv(color.hue(), color.saturation(), min(255, (145 + 45 * l) - (29 - i) * 15)).rgba())
    table.append(QColor(0, 0, 0, 0).rgba())
    return table


@dataclass(frozen=True)
class Tile:
    name: str
    type: str
    repeatl: list[int]
    description: str
    bfTiles: int
    image: QPixmap
    image2: QPixmap | None
    image3: QImage | None
    size: QSize
    color: QColor
    cols: [list[int], [list[int] | int]]
    cat: QPoint
    tags: list[str]
    printcols: bool
    preview: QImage | None
    err: bool
    category: TileCategory

    @property
    def top_left(self) -> QPoint:
        return QPoint(int((self.size.width() * 0.5) + .5) - 1, int((self.size.height() * .5) + .5) - 1)

    def collisions_image(self, l1color: QColor = QColor(255, 0, 0, 255),
                         l2color: QColor = QColor(0, 0, 255, 255)) -> QPixmap:
        tile_image = QPixmap((self.size + QSize(self.bfTiles * 2, self.bfTiles * 2)) * CELLSIZE)
        tile_image.fill(QColor(0, 0, 0, 0))
        painter = QPainter(tile_image)

        def drawlayer(specs):
            nonlocal painter
            for i, v in enumerate(specs):
                pos = QPoint(i // self.size.height(), i % self.size.height()) * CELLSIZE
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

        painter.setBrush(QColor(0, 0, 0, 0))
        if isinstance(self.cols[1], list):
            painter.setPen(QPen(l2color, 2, Qt.PenStyle.DotLine))
            drawlayer(self.cols[1])
        painter.setPen(QPen(l1color, 1, Qt.PenStyle.DashLine))
        drawlayer(self.cols[0])
        return tile_image

    def return_tile_pixmap(self, option: int, layer: int, layercolortable) -> QPixmap:
        if option == 0:
            return self.image
        elif option == 1:
            return self.image2
        elif option == 3:
            self.image3.setColorTable(colortable[layer])
            return QPixmap.fromImage(self.image3)
        elif option == 2:
            self.image3.setColorTable(color_colortable(self.color))
            return QPixmap.fromImage(self.image3)
        else:
            col = option - 4
            self.image3.setColorTable(layercolortable[col][layer])
            return QPixmap.fromImage(self.image3)


@dataclass
class TileCategory:
    name: str
    color: QColor
    tiles: list[Tile]

    def find_tile(self, name) -> Tile | None:
        for i in self.tiles:
            if i.name == name:
                return i
        return None


@dataclass
class Tiles:
    categories: list[TileCategory]

    def find_tile(self, name) -> Tile | None:
        for i in self.categories:
            tile = i.find_tile(name)
            if tile is not None:
                return tile
        return None

    def find_category(self, name) -> TileCategory | None:
        for i in self.categories:
            if i.name == name:
                return i
        return None

    def all_tiles(self) -> list[Tile]:
        t = [i.tiles for i in self.categories]
        newt = []
        for i in t:
            newt = [*newt, *i]
        return newt

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.find_tile(item)
