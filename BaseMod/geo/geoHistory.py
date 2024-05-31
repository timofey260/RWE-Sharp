from core.HistorySystem import HistoryElement
from PySide6.QtCore import QPoint
from core.utils import draw_line

class GERectChange(HistoryElement):
    def __init__(self, history, level, rect, block: int, layers: list[bool, bool, bool]):
        super().__init__(history)

class GEpointChange(HistoryElement):
    def __init__(self, history, start: QPoint, replace, layers:list[bool, bool, bool]):
        super().__init__(history)
        self.positions: list[QPoint] = []
        self.before = []
        self.replace = replace
        self.start: QPoint = start
        self.layers = layers

    def add_move(self, position, module):
        self.positions.append(position)
        start = self.start
        if len(self.positions) > 1:
            start = self.positions[-2]

        points = []
        draw_line(start, self.positions[-1], lambda p: points.append(p))
        for point in points:
            for i, l in enumerate(self.layers):
                if l:
                    data = self.history.level.GE_data(point.x(), point.y(), i)
                    self.before.append([data[0], data[1].copy()])  # not using recursive deepcopy bullshit
                    self.history.level.data["GE"][point.x()][point.y()][i] = [self.replace[0], self.replace[1].copy()]
                    [module.l1, module.l2, module.l3][i].draw_geo(point.x(), point.y(), True)

    def undo_changes(self, level):  # removing placed cells with replaced ones
        beforeitem = 0
        layers = [level.manager.basemod.geomodule.l1, level.manager.basemod.geomodule.l2,
                  level.manager.basemod.geomodule.l3]
        for i, v in enumerate(self.positions):
            start = self.start
            if i > 0:
                start = self.positions[i - 1]
            points = []
            draw_line(start, v, lambda p: points.append(p))
            for point in points:
                for i, l in enumerate(self.layers):
                    if l:
                        data = self.before[beforeitem]
                        level.data["GE"][point.x()][point.y()][i] = [data[0], data[1].copy()]
                        beforeitem += 1
                        layers[i].draw_geo(point.x(), point.y(), True)

    def redo_changes(self, level):  # re-adding replace cell
        layers = [level.manager.basemod.geomodule.l1, level.manager.basemod.geomodule.l2,
                  level.manager.basemod.geomodule.l3]
        for i, v in enumerate(self.positions):
            start = self.start
            if i > 0:
                start = self.positions[i - 1]
            points = []
            draw_line(start, v, lambda p: points.append(p))
            for point in points:
                for i, l in enumerate(self.layers):
                    if l:
                        level.data["GE"][point.x()][point.y()][i] = [self.replace[0], self.replace[1].copy()]
                        layers[i].draw_geo(point.x(), point.y(), True)
