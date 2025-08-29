from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
from PySide6.QtCore import QRect
if TYPE_CHECKING:
    from core.Level.RWELevel import RWELevel
    from core.HistorySystem import HistoryElement


class LevelPart(ABC):

    def __init__(self, name: str, level: RWELevel):
        self.level = level
        if name not in level.levelparts.keys():
            level.levelparts[name] = self

    @abstractmethod
    def save_level(self):
        pass

    @property
    def manager(self):
        return self.level.manager

    @abstractmethod
    def level_resized(self, changerect: QRect) -> HistoryElement:
        pass
