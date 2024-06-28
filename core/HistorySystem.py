"""
All elements and actions are not made untill specific change in history happends
"""
from __future__ import annotations
from copy import deepcopy


class HistoryElement:
    """
    Base for creating history elements
    """

    def __init__(self, history):
        self.history: History = history

    def undo_changes(self, level):
        pass

    def redo_changes(self, level):
        pass


class History:
    def __init__(self, level):
        from core.RWELevel import RWELevel
        self.undoactions: list[HistoryElement] = []
        self.redoactions: list[HistoryElement] = []
        self.level: RWELevel = level

    def undo(self):
        if len(self.undoactions) == 0:
            return
        action = self.undoactions.pop()
        action.undo_changes(self.level)
        self.redoactions.append(action)

    def redo(self):
        if len(self.redoactions) == 0:
            return
        action = self.redoactions.pop()
        action.redo_changes(self.level)
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


class SimpleChange(HistoryElement):
    def __init__(self, history, path, value, prev_value):
        super().__init__(history)
        self.path = path
        self.value = value
        self.prev_value = prev_value

    def undo_changes(self, level):
        level[self.path] = deepcopy(self.prev_value)

    def redo_changes(self, level):
        level[self.path] = deepcopy(self.value)