from __future__ import annotations
from dataclasses import dataclass, field
from PySide6.QtGui import QColor, QPixmap
from random import randint


@dataclass
class EffectOption:
    name: str
    options: list[str]
    selectedOption: str


class SeedOption(EffectOption):
    def __init__(self):
        super().__init__("Seed", [], str(randint(0, 100)))


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
