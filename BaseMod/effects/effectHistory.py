from RWESharp.Modify import HistoryElement
from PySide6.QtCore import QPoint


class EffectBrush(HistoryElement):
    def __init__(self, history, start: QPoint, size: int):
        super().__init__(history)
        self.start = start
        self.size = size

    def add_move(self, point):
        pass
