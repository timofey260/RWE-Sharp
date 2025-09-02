"""
All elements and actions are not made untill specific change in history happends
"""
from __future__ import annotations
from copy import deepcopy
from abc import ABC, abstractmethod


class HistoryElement(ABC):
    """
    Base for creating history elements
    """

    def __init__(self, history):
        self.history: History = history

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


class History:
    def __init__(self, level):
        from core.Level.RWELevel import RWELevel
        self.undoactions: list[HistoryElement] = []
        self.redoactions: list[HistoryElement] = []
        self.level: RWELevel = level

    def undo(self):
        if len(self.undoactions) == 0:
            return
        action = self.undoactions.pop()
        action.undo_changes()
        self.redoactions.append(action)

    def redo(self):
        if len(self.redoactions) == 0:
            return
        action = self.redoactions.pop()
        action.redo_changes()
        self.undoactions.append(action)

    @property
    def last_element(self) -> HistoryElement | None:
        try:
            return self.undoactions[-1]
        except IndexError:
            return None

    def add_element(self, element: HistoryElement):
        self.redoactions = []
        self.undoactions.append(element)


class MultiHistoryElement(HistoryElement):
    def __init__(self, history, elements: list[HistoryElement]):
        super().__init__(history)
        self.elements = elements

    def undo_changes(self):
        for i in reversed(self.elements):
            i.undo_changes()

    def redo_changes(self):
        for i in self.elements:
            i.redo_changes()


class LevelResized(MultiHistoryElement):
    def __init__(self, history, elements, oldrect, newrect):
        super().__init__(history, elements)
        self.oldrect = oldrect
        self.newrect = newrect
        self.level._level_size = [self.newrect.width(), self.newrect.height()]
        if self.level.viewport is None:
            return
        self.level.viewport.level_resized(self.newrect)

    def undo_changes(self):
        super().undo_changes()
        self.level._level_size = [self.oldrect.width(), self.oldrect.height()]
        if self.level.viewport is None:
            return
        self.level.viewport.level_resized(self.oldrect)

    def redo_changes(self):
        super().redo_changes()
        self.level._level_size = [self.newrect.width(), self.newrect.height()]
        if self.level.viewport is None:
            return
        self.level.viewport.level_resized(self.newrect)