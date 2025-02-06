from RWESharp.Modify import HistoryElement


class AddCamera(HistoryElement):
    def __init__(self, history):
        super().__init__(history)

    def undo_changes(self):
        pass

    def redo_changes(self):
        pass
