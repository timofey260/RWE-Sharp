from core.HistorySystem import HistoryElement
from PySide6.QtCore import QPoint, QRect
from core.utils import draw_line

class GERectChange(HistoryElement):
    def __init__(self, history, rect: QRect, replace, layers: list[bool, bool, bool]):
        super().__init__(history)
        self.rect = rect
        self.replace = replace
        self.before = []
        self.layers = layers
        for x in range(self.rect.x(), self.rect.width()):
            for y in range(self.rect.y(), self.rect.height()):
                for i, l in enumerate(self.layers):
                    if l:
                        data = self.history.level.GE_data(x, y, i)
                        self.before.append([data[0], data[1].copy()])
                        self.history.level.data["GE"][x][y][i] = [replace[0], replace[1].copy()]

    def undo_changes(self, level):
        c = 0
        for x in range(self.rect.x(), self.rect.width()):
            for y in range(self.rect.y(), self.rect.height()):
                for i, l in enumerate(self.layers):
                    if l:
                        self.history.level.data["GE"][x][y][i] = [self.before[0], self.before[1].copy()]
                        c += 1  # c++ almost

    def redo_changes(self, level):
        for x in range(self.rect.x(), self.rect.width()):
            for y in range(self.rect.y(), self.rect.height()):
                for i, l in enumerate(self.layers):
                    if l:
                        self.history.level.data["GE"][x][y][i] = [self.replace[0], self.replace[1].copy()]

class GEpointChange(HistoryElement):
    def __init__(self, history, start: QPoint, replace, layers: list[bool, bool, bool]):
        super().__init__(history)
        self.positions: list[QPoint] = []
        self.before = []
        self.replace = replace
        self.start: QPoint = start
        self.layers = layers
        for i, l in enumerate(self.layers):
            if l:
                self.before.append(self.history.level.data["GE"][start.x()][start.y()][i])
                self.history.level.data["GE"][start.x()][start.y()][i] = [self.replace[0], self.replace[1].copy()]
                t = [history.level.manager.basemod.geomodule.l1, history.level.manager.basemod.geomodule.l2,
                    history.level.manager.basemod.geomodule.l3][i]
                t.draw_geo(start.x(), start.y(), True)
                t.redraw()

    def add_move(self, position, module):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            for i, l in enumerate(self.layers):
                if l:
                    data = self.history.level.GE_data(point.x(), point.y(), i)
                    self.before.append([data[0], data[1].copy()])  # not using recursive deepcopy bullshit
                    self.history.level.data["GE"][point.x()][point.y()][i] = [self.replace[0], self.replace[1].copy()]
                    [module.l1, module.l2, module.l3][i].draw_geo(point.x(), point.y(), True)
        for i, l in enumerate(self.layers):
            if l:
                [module.l1, module.l2, module.l3][i].redraw()

    def undo_changes(self, level):  # removing placed cells with replaced ones
        allpoints = []
        activelayers = sum(1 if i else 0 for i in self.layers)
        beforeitem = activelayers
        layers = [level.manager.basemod.geomodule.l1, level.manager.basemod.geomodule.l2,
                  level.manager.basemod.geomodule.l3]
        start = self.start

        for i, v in enumerate(self.positions):
            points = []
            draw_line(start, v, lambda p: points.append(p))
            points.pop(0)
            for point in points:
                if point in allpoints:
                    beforeitem += activelayers
                    continue
                allpoints.append(point)
                for i2, l in enumerate(self.layers):
                    if l:
                        data = self.before[beforeitem]
                        level.data["GE"][point.x()][point.y()][i2] = [data[0], data[1].copy()]
                        layers[i2].draw_geo(point.x(), point.y(), True)
                        beforeitem += 1
            start = v
        layer = 0
        for i, l in enumerate(self.layers):
            if l:
                level.data["GE"][self.start.x()][self.start.y()][i] = [self.before[layer][0], self.before[layer][1].copy()]
                layer += 1
                layers[i].draw_geo(self.start.x(), self.start.y(), True)
                layers[i].redraw()

    def redo_changes(self, level):  # re-adding replace cell
        layers = [level.manager.basemod.geomodule.l1, level.manager.basemod.geomodule.l2,
                  level.manager.basemod.geomodule.l3]
        start = self.start
        for i, v in enumerate(self.positions):
            points = []
            draw_line(start, v, lambda p: points.append(p))
            for point in points:
                for i, l in enumerate(self.layers):
                    if l:
                        level.data["GE"][point.x()][point.y()][i] = [self.replace[0], self.replace[1].copy()]
                        layers[i].draw_geo(point.x(), point.y(), True)
            start = v
        for i, l in enumerate(self.layers):
            if l:
                layers[i].redraw()
