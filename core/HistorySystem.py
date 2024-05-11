"""
Alle elements and actions are not made untill specific change in history happends
"""
class History:
    def __init__(self, level):
        self.undoactions: list[HistoryElement] = []
        self.redoactions: list[HistoryElement] = []
        self.level = level

    def undo(self):
        pass

    def redo(self):
        pass


class HistoryElement:
    """
    Base for creating history elements
    """

    def __init__(self):
        pass

    def undo_changes(self, level):
        pass

    def redo_changes(self, level):
        pass

class SimpleChange(HistoryElement):
    def __init__(self, path, value, prev_value):
        super().__init__()
        self.path = path
        self.value = value
        self.prev_value = prev_value