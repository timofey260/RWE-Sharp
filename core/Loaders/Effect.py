from __future__ import annotations
from dataclasses import dataclass, field
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import QSize
from random import randint


@dataclass
class EffectOption:
    name: str
    options: list[str]
    selectedOption: str

    def tolist(self):
        return [self.name, self.options.copy(), self.selectedOption]


class SeedOption(EffectOption):
    def __init__(self):
        super().__init__("Seed", [], str(randint(0, 100)))

    def tolist(self):
        return [self.name, self.options.copy(), int(self.selectedOption)]


class MoveDeleteOption(EffectOption):
    def __init__(self):
        super().__init__("Move/Delete", ["Delete", "Move Back", "Move Forth"], "")


@dataclass(frozen=True)
class Effect:
    name: str
    description: str
    tp: str
    crossscreen: int
    color: QColor
    options: list[EffectOption]
    repeats: int
    affect_open_areas: float
    preview: QPixmap
    category: EffectCategory
    ultrablack: bool  # goo

    def todict(self, size: QSize):
        newoptions = [i.tolist() for i in self.options]
        matrix = [[0 for _ in range(size.height())] for _ in range(size.width())]
        return {"nm": self.name, "tp": self.tp, "options": newoptions, "repeats": self.repeats,
                "affectOpenAreas": self.affect_open_areas, "crossScreen": self.crossscreen, "mtrx": matrix}


@dataclass
class EffectCategory:
    name: str
    color: QColor
    effects: list[Effect]

    def find_effect(self, name) -> Effect | None:
        for i in self.effects:
            if i.name == name:
                return i
        return None

    def __getitem__(self, item):
        return self.effects[item]


@dataclass
class Effects:
    categories: list[EffectCategory]

    def find_effect(self, name) -> Effect | None:
        for i in self.categories:
            effect = i.find_effect(name)
            if effect is not None:
                return effect
        return None

    def find_category(self, name) -> EffectCategory | None:
        for i in self.categories:
            if i.name == name:
                return i
        return None

    def __getitem__(self, item):
        return self.categories[item]
