from __future__ import annotations
from PySide6.QtGui import QImage, QColor, QPixmap
from PySide6.QtCore import QPoint, QSize
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Prop:
    name: str
    type: str
    repeatl: list[int]
    description: str
    bfTiles: int
    images: list[QPixmap]
    image2: list[QImage] | None
    colorTreatment: str
    color: str
    size: QSize
    color: QColor
    cat: QPoint
    tags: list[str]
    printcols: bool
    preview: QImage | None
    err: bool
    category: PropCategory
    notes: list[str]
    layerExceptions: list = field(default=list)



@dataclass
class PropCategory:
    name: str
    color: QColor
    tiles: list[Prop]

    def find_prop(self, name) -> Prop | None:
        for i in self.tiles:
            if i.name == name:
                return i
        return None


@dataclass
class Props:
    categories: list[PropCategory]

    def find_prop(self, name) -> Prop | None:
        for i in self.categories:
            tile = i.find_prop(name)
            if tile is not None:
                return tile
        return None

    def find_category(self, name) -> PropCategory | None:
        for i in self.categories:
            if i.name == name:
                return i
        return None

    def all_props(self) -> list[Prop]:
        t = [i.tiles for i in self.categories]
        newt = []
        for i in t:
            newt = [*newt, *i]
        return newt

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.find_prop(item)