from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from RWESharp.Core.HistorySystem import LevelHistory


class HistoryElement(ABC):
    """
    Base for creating history elements
    """

    def __init__(self, history: LevelHistory):
        self.history: LevelHistory = history

    @abstractmethod
    def undo_changes(self):
        pass

    @abstractmethod
    def redo_changes(self):
        pass

    @property
    def manager(self):
        return self.history.level.manager

    @property
    def basemod(self):
        return self.manager.basemod

    @property
    def level(self):
        return self.history.level
