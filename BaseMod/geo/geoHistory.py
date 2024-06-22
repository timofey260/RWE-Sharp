from RWESharp.Modify import HistoryElement
from RWESharp.Utils import draw_line
from PySide6.QtCore import QPoint, QRect


def grab_return(form: [int, bool], block: [int, list[int]]) -> ([int, list[int]], ...):
    if form[1] and form[0] < 0:
        if form[0] == -2:  # upper
            return [block[0], []], block[1].copy()
        elif form[0] == -3:  # block
            return [0, block[1].copy()], block[0]
        elif form[0] == -4:  # all, no layer check
            return [0, []], [block[0], block[1].copy()]
        elif form[0] == -5:  # layer
            return [0, []], [block[0], block[1].copy()]
    elif form[1]:  # stack
        bol = form[0] in block[1]
        ar = block[1].copy()
        if not bol:
            ar.append(form[0])
        return [block[0], ar], bol
    return [form[0], block[1].copy()], block[0]


def put_return(form: [int, bool], block: [int, list[int]], saved) -> [int, list[int]]:
    if form[1] and form[0] < 0:
        if form[0] == -2:  # upper
            return [block[0], saved.copy()]
        elif form[0] == -3:  # block
            return [saved, block[1].copy()]
        elif form[0] == -4:  # all
            return [saved[0], saved[1].copy()]
        elif form[0] == -5:  # layer
            return [saved[0], saved[1].copy()]
    elif form[1]:  # stack
        ar = block[1].copy()
        if not saved:
            ar.remove(form[0])
        return [block[0], ar]
    return [saved, block[1].copy()]


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
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool]):
        super().__init__(history)
        self.positions: list[QPoint] = []
        self.before: list[int] = []
        self.replace = replace
        self.start: QPoint = start
        self.layers = layers
        self.module = self.history.level.manager.basemod.geomodule
        for i, l in enumerate(self.layers):
            if l:
                block, save = grab_return(self.replace, self.history.level.GE_data(start.x(), start.y(), i))
                self.before.append(save)
                self.history.level.data["GE"][start.x()][start.y()][i] = block
                t = self.module.get_layer(i)
                t.draw_geo(start.x(), start.y(), True)
                t.redraw()

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
                    block, save = grab_return(self.replace, self.history.level.GE_data(point.x(), point.y(), i))
                    self.before.append(save)
                    self.history.level.data["GE"][point.x()][point.y()][i] = block
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
                        block = put_return(self.replace, self.history.level.GE_data(point.x(), point.y(), i2), self.before[beforeitem])
                        self.history.level.data["GE"][point.x()][point.y()][i2] = block
                        self.module.get_layer(i2).draw_geo(point.x(), point.y(), True)
                        beforeitem += 1
            start = v
        layer = 0
        for i, l in enumerate(self.layers):
            if l:
                block = put_return(self.replace, self.history.level.GE_data(self.start.x(), self.start.y(), i),
                                   self.before[layer])
                self.history.level.data["GE"][self.start.x()][self.start.y()][i] = block
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
                        block, save = grab_return(self.replace, self.history.level.GE_data(point.x(), point.y(), li))
                        self.before.append(save)
                        self.history.level.data["GE"][point.x()][point.y()][li] = block
                        self.module.get_layer(li).draw_geo(point.x(), point.y(), True)
            start = v
        for i, l in enumerate(self.layers):
            if l:
                self.module.get_layer(i).redraw()
