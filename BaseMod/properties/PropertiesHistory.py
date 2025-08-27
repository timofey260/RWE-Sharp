from RWESharp.Modify import HistoryElement

class BorderChange(HistoryElement):
    def __init__(self, history, border_tiles: list[int]):
        super().__init__(history)
        self.before = self.level.extra_tiles.copy()
        self.after = border_tiles.copy()
        self.redo_changes()

    def undo_changes(self):
        self.level.l_info.extra_tiles = self.before.copy()
        self.level.viewport.modulenames["grid"].level_resized()

    def redo_changes(self):
        self.level.l_info.extra_tiles = self.after.copy()
        self.level.viewport.modulenames["grid"].level_resized()
