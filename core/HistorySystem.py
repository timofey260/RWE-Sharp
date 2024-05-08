"""
Alle elements and actions are not made untill specific change in history happends
"""
class History:
    def __init__(self):
        self.undoactions: list[HistoryElement] = []
        self.redoactions: list[HistoryElement] = []


    def add_change(self):
        pass


class HistoryElement:
    """
    Base for creating history elements
    """

    def __init__(self):
        pass

    def undo_changes(self):
        pass

    def redo_changes(self):
        pass

class SimpleChange(HistoryElement):
    def __init__(self, path, value):
        super().__init__()