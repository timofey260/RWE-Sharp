from core.HistorySystem import HistoryElement
from PySide6.QtCore import QPoint

class GERectChange(HistoryElement):
    def __init__(self, level, rect, block: int, layers: list[bool, bool, bool]):
        super().__init__()

class GEpointChange(HistoryElement):
    def __init__(self, points: list[QPoint], layer, before, after):
        super().__init__()
