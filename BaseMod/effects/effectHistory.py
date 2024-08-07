from RWESharp.Modify import HistoryElement
from PySide6.QtCore import QPoint
from RWESharp.Loaders import Effect


class EffectBrush(HistoryElement):
    def __init__(self, history, start: QPoint, size: int):
        super().__init__(history)
        self.start = start
        self.size = size

    def add_move(self, point):
        pass


class EffectAdd(HistoryElement):
    def __init__(self, history, effect: Effect):
        super().__init__(history)
        self.effect = effect
        self.add_effect()
        self.history.level.manager.basemod.effectui.effect_select(len(self.history.level["FE"]["effects"]) - 1)

    def add_effect(self):
        self.history.level["FE"]["effects"].append(self.effect.todict(self.history.level.level_size_qsize))
        self.history.level.manager.basemod.effectui.add_effects()

    def undo_changes(self, level):
        self.history.level["FE"]["effects"].pop()
        self.history.level.manager.basemod.effectui.add_effects()

    def redo_changes(self, level):
        self.add_effect()
