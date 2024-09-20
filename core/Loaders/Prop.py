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
    images: list[QImage]
    colorTreatment: str
    vars: int
    color: str
    color: QColor
    cat: QPoint
    tags: list[str]
    err: bool
    category: PropCategory
    notes: list[str]
    layerExceptions: list = field(default=list)
    beveltable: None | list[int] = None

    @property
    def colorable(self):
        return len(self.repeatl) > 1


@dataclass
class PropCategory:
    name: str
    color: QColor
    props: list[Prop]

    def find_prop(self, name) -> Prop | None:
        for i in self.props:
            if i.name == name:
                return i
        return None

    def __repr__(self):
        return f"<Prop category {self.name} with {len(self.props)} prop(s)>"


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
        t = [i.props for i in self.categories]
        newt = []
        for i in t:
            newt = [*newt, *i]
        return newt

    def __getitem__(self, item):
        if isinstance(item, str):
            return self.find_prop(item)
