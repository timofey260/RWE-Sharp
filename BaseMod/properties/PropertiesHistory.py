from RWESharp.Modify.HistoryElement import HistoryElement


class BorderChange(HistoryElement):
    def __init__(self, history, border_tiles: list[int]):
        super().__init__(history)
        self.before = self.level.extra_tiles.copy()
        self.after = border_tiles.copy()
        self.redo_changes()

    def undo_changes(self):
        self.level.l_info.extra_tiles = self.before.copy()
        self.level.viewport.modulenames["grid"].level_resized(self.level.level_rect)
        self.manager.basemod.propertieseditor.reposition_extra()  # i can't believe stuff is so simple

    def redo_changes(self):
        self.level.l_info.extra_tiles = self.after.copy()
        self.level.viewport.modulenames["grid"].level_resized(self.level.level_rect)
        self.manager.basemod.propertieseditor.reposition_extra()

class TileSeedChange(HistoryElement):
    def __init__(self, history, seed: int):
        super().__init__(history)
        self.before = self.level.l_info.tile_seed
        self.after = seed
        self.redo_changes()

    def undo_changes(self):
        self.level.l_info.tile_seed = self.before
        self.manager.basemod.propertieseditor.update_params()

    def redo_changes(self):
        self.level.l_info.tile_seed = self.after
        self.manager.basemod.propertieseditor.update_params()

class WaterChange(HistoryElement):
    def __init__(self, history, level: int, infront: int):
        super().__init__(history)
        self.before = [self.level.l_info.water_level, self.level.l_info.water_in_front]
        self.after = [level, infront]
        self.redo_changes()

    def undo_changes(self):
        self.level.l_info.water_level = self.before[0]
        self.level.l_info.water_in_front = self.before[1]
        self.manager.basemod.propertieseditor.update_params()
        self.level.viewport.modulenames["grid"].update_water()

    def redo_changes(self):
        self.level.l_info.water_level = self.after[0]
        self.level.l_info.water_in_front = self.after[1]
        self.manager.basemod.propertieseditor.update_params()
        self.level.viewport.modulenames["grid"].update_water()


class LevelResizedProperties(HistoryElement):
    def undo_changes(self):
        self.level.l_info.size = self.oldrect.copy()

    def redo_changes(self):
        self.level.l_info.size = [self.newrect.width(), self.newrect.height()]

    def __init__(self, history, newrect):
        super().__init__(history)
        self.newrect = newrect
        self.oldrect = self.level.l_info.size.copy()
        self.redo_changes()

