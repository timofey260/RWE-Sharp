from RWESharp.Modify import HistoryElement


class LevelResizedLight(HistoryElement):
    def __init__(self, history, newrect):
        super().__init__(history)
        self.newrect = newrect

    def undo_changes(self):
        pass

    def redo_changes(self):
        pass