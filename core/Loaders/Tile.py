from __future__ import annotations
from PySide6.QtGui import QImage, QColor, QPixmap
from PySide6.QtCore import QPoint, QSize
from dataclasses import dataclass


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
