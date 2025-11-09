"""
All elements and actions are not made untill specific change in history happends
"""
from __future__ import annotations
from RWESharp.Modify.HistoryElement import HistoryElement

class LevelHistory:
    def __init__(self, level):
        from RWESharp.Level.RWELevel import RWELevel
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