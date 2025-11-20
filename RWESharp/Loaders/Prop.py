from __future__ import annotations
from PySide6.QtGui import QImage, QColor, QPixmap
from PySide6.QtCore import QPoint, QSize, QObject, Signal
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Prop:
    item: dict
    name: str
    type: str
    repeatl: list[int]
    description: str
    images: list[QImage]
    colorTreatment: str
    vars: int
    # color: str
    color: QColor
    cat: QPoint
    tags: list[str]
    err: bool
    category: PropCategory
    notes: list[str]
    size: QSize
    layerExceptions: list = field(default=list)
    beveltable: None | list[int] = None
    rope: bool = False
    long: bool = False

    @property
    def colorable(self):
        return len(self.repeatl) > 1

    def get(self, key, default=None):
        return self.item.get(key, default)

    def __getitem__(self, item):
        return self.item.get(item)

    def copy(self):
        return Prop(self.item, self.name, self.type, self.repeatl, self.description, self.images, self.colorTreatment,
                    self.vars, self.color, self.cat, self.tags, self.err, self.category, self.notes, self.size, self.layerExceptions,
                    self.beveltable, self.rope, self.long)


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


class Props(QObject):
    default = Prop({}, "None", "standard", [1], "No Description", [QImage(10, 10, QImage.Format.Format_RGBA64)], "none", 1, QColor(255, 0, 0), QPoint(0, 0), [], True, None, [], QSize(1, 1))
    propschanged = Signal()

    @property
    def categories(self):
        return [*self._categories, *self.custom_categories]

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

    def add_custom_props(self):
        # todo
        self.propschanged.emit()

    def __init__(self, categories):
        super().__init__()
        self._categories: list[PropCategory] = categories
        self.custom_categories = []
        self.add_custom_props()
