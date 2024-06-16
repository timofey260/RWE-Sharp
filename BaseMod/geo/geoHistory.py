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


class GEPointChange(HistoryElement):
    def __init__(self, history, start: QPoint, replace, layers: [bool, bool, bool]):
        super().__init__(history)
        self.positions: list[QPoint] = []
        self.before: list[int] = []
        self.replace = replace
        self.start: QPoint = start
        self.layers = layers
        self.module = self.history.level.manager.basemod.geomodule
        for i, l in enumerate(self.layers):
            if l:
                self.before.append(self.get_save(start.x(), start.y(), i))
                self.set_replace(start.x(), start.y(), i)
                t = self.module.get_layer(i)
                t.draw_geo(start.x(), start.y(), True)
                t.redraw()

    def get_save(self, x, y, l):
        return self.history.level.GE_data(x, y, l)

    def set_load(self, x, y, l, data):
        self.history.level.data["GE"][x][y][l] = data

    def set_replace(self, x, y, l):
        self.history.level.data["GE"][x][y][l] = self.replace

    def add_move(self, position):
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
                    self.before.append(self.get_save(point.x(), point.y(), i))
                    self.set_replace(point.x(), point.y(), i)
                    self.module.get_layer(i).draw_geo(point.x(), point.y(), True)
        for i, l in enumerate(self.layers):
            if l:
                self.module.get_layer(i).redraw()

    def undo_changes(self, level):  # removing placed cells with replaced ones
        allpoints = []
        activelayers = sum(1 if i else 0 for i in self.layers)
        beforeitem = activelayers
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
                        self.set_load(point.x(), point.y(), i2, self.before[beforeitem])
                        self.module.get_layer(i2).draw_geo(point.x(), point.y(), True)
                        beforeitem += 1
            start = v
        layer = 0
        for i, l in enumerate(self.layers):
            if l:
                self.set_load(self.start.x(), self.start.y(), i, self.before[layer])
                layer += 1
                self.module.get_layer(i).draw_geo(self.start.x(), self.start.y(), True)
                self.module.get_layer(i).redraw()

    def redo_changes(self, level):  # re-adding replace cell
        start = self.start
        for i, v in enumerate(self.positions):
            points = []
            draw_line(start, v, lambda p: points.append(p))
            for point in points:
                for li, l in enumerate(self.layers):
                    if l:
                        self.set_replace(point.x(), point.y(), li)
                        self.module.get_layer(li).draw_geo(point.x(), point.y(), True)
            start = v
        for i, l in enumerate(self.layers):
            if l:
                self.module.get_layer(i).redraw()


class GEBlockChange(GEPointChange):
    def __init__(self, history, start: QPoint, replace: int, layers: [bool, bool, bool]):
        super().__init__(history, start, replace, layers)

    def get_save(self, x, y, l):
        return self.history.level.GE_data(x, y, l)[0]

    def set_load(self, x, y, l, data):
        self.history.level.data["GE"][x][y][l][0] = data

    def set_replace(self, x, y, l):
        self.history.level.data["GE"][x][y][l][0] = self.replace


class GEStackChange(GEPointChange):
    def __init__(self, history, start: QPoint, replace: int, layers: [bool, bool, bool]):
        super().__init__(history, start, replace, layers)

    def get_save(self, x, y, l):
        return self.replace in self.history.level.GE_data(x, y, l)[1]

    def set_load(self, x, y, l, data):
        if not data:
            self.history.level.data["GE"][x][y][l][1].remove(self.replace)

    def set_replace(self, x, y, l):
        if self.replace not in self.history.level.GE_data(x, y, l)[1]:
            self.history.level.data["GE"][x][y][l][1].append(self.replace)


class GEClearLayer(GEPointChange):
    def __init__(self, history, start: QPoint, layers: [bool, bool, bool]):
        super().__init__(history, start, [], layers)

    def get_save(self, x, y, l):
        data = self.history.level.GE_data(x, y, l)
        return [data[0], data[1].copy()]

    def set_load(self, x, y, l, data):
        self.history.level.data["GE"][x][y][l] = [data[0], data[1].copy()]

    def set_replace(self, x, y, l):
        self.history.level.data["GE"][x][y][l] = [0, []]


class GEClearAll(GEClearLayer):
    def __init__(self, history, start: QPoint):
        super().__init__(history, start, [True, True, True])


class GEClearUpper(GEPointChange):
    def __init__(self, history, start: QPoint, layers: [bool, bool, bool]):
        super().__init__(history, start, [], layers)

    def get_save(self, x, y, l):
        return self.history.level.GE_data(x, y, l)[1].copy()

    def set_load(self, x, y, l, data):
        self.history.level.data["GE"][x][y][l][1] = data.copy()

    def set_replace(self, x, y, l):
        self.history.level.data["GE"][x][y][l][1] = []


class GEClearBlock(GEPointChange):
    def __init__(self, history, start: QPoint, layers: [bool, bool, bool]):
        super().__init__(history, start, [], layers)

    def get_save(self, x, y, l):
        return self.history.level.GE_data(x, y, l)[0]

    def set_load(self, x, y, l, data):
        self.history.level.data["GE"][x][y][l][0] = data

    def set_replace(self, x, y, l):
        self.history.level.data["GE"][x][y][l][0] = 0


class GEShortcutBlock(GEPointChange):
    def __init__(self, history, start: QPoint, layers: [bool, bool, bool]):
        super().__init__(history, start, [7, [4]], layers)

    def get_save(self, x, y, l):
        data = self.history.level.GE_data(x, y, l)
        return [data[0], data[1].copy()]

    def set_load(self, x, y, l, data):
        self.history.level.data["GE"][x][y][l] = [data[0], data[1].copy()]

    def set_replace(self, x, y, l):
        self.history.level.data["GE"][x][y][l] = [7, [4]]
