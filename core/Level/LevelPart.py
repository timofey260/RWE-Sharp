from __future__ import annotations
from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
if TYPE_CHECKING:
    from core.Level.RWELevel import RWELevel


class LevelPart(ABC):

    def __init__(self, name: str, level: RWELevel):
        self.level = level
        if name not in level.levelparts.keys():
            level.levelparts[name] = self

    @abstractmethod
    def save_level(self):
        pass
