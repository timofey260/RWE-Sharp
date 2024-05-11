from core.HistorySystem import HistoryElement

class GERectChange(HistoryElement):
    def __init__(self, level, rect, block: int, layers: list[bool, bool, bool]):
        super().__init__()
