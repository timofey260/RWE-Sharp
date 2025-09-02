import numpy as np
from PySide6.QtCore import QPoint, QRect

from BaseMod.geo.geoUtils import geo_save, geo_undo
from RWESharp.Modify import HistoryElement
from RWESharp.Utils import draw_line, draw_ellipse


nearpoints = [QPoint(-1, 0), QPoint(0, -1), QPoint(1, 0), QPoint(0, 1)]
# ^ i  have no clue what this does. Stack overflow told me to do so


class GEChange(HistoryElement):
    def __init__(self, history, replace, layers: [bool, bool, bool]):
        super().__init__(history)
        self.history = history
        self.replace = replace
        self.layers = layers
        self.before = []
        self.module = history.level.viewport.modulenames["geo"]

    def redraw(self):
        for i, l in enumerate(self.layers):
            if not l:
                continue
            self.module.get_layer(i).redraw()


class GERectChange(GEChange):
    def __init__(self, history, rect: QRect, replace, layers: [bool, bool, bool], hollow=False):
        super().__init__(history, replace, layers)
        self.rect = rect
        self.hollow = hollow
        x_range = np.arange(self.rect.x(), self.rect.x() + self.rect.width())
        y_range = np.arange(self.rect.y(), self.rect.y() + self.rect.height()) # if this works im  buying all the lotery tickets
        #Vectorized loops: np.arange is used for x_range and y_range for faster looping over grid coordinates.
        for x in x_range:
            for y in y_range:
                for i, l in enumerate(self.layers):
                    if not l or not self.history.level.inside(QPoint(x, y)):
                        continue
                    if self.ishollow(x, y):
                        continue
                    block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(x, y, i))
                    self.before.append(save)
                    self.history.level.l_geo.setlevelgeo(x, y, i, block)
                    t = self.module.get_layer(i)
                    t.draw_geo(x, y, True, self.inborder(x, y))
        self.redraw()

    #change to make new branch

    def inborder(self, x, y):
        return (x == self.rect.x() or y == self.rect.y() or
                x == self.rect.x() + self.rect.width() - 1 or
                y == self.rect.y() + self.rect.height() - 1)

    def ishollow(self, x, y):
        if self.hollow and self.inborder(x, y):
            return False
        return self.hollow

    def undo_changes(self):
        c = 0
        x_range = np.arange(self.rect.x(), self.rect.x() + self.rect.width())
        y_range = np.arange(self.rect.y(), self.rect.y() + self.rect.height())
        for x in x_range:
            for y in y_range:
                for i, l in enumerate(self.layers):
                    if not l or not self.history.level.inside(QPoint(x, y)):
                        continue
                    if self.ishollow(x, y):
                        continue
                    block = geo_undo(self.replace, self.history.level.l_geo.getlevelgeo(x, y, i), self.before[c])
                    self.history.level.l_geo.setlevelgeo(x, y, i, block)
                    self.module.get_layer(i).draw_geo(x, y, True, self.inborder(x, y))
                    c += 1  # c++ almost
        self.redraw()

    def redo_changes(self):
        x_range = np.arange(self.rect.x(), self.rect.x() + self.rect.width())
        y_range = np.arange(self.rect.y(), self.rect.y() + self.rect.height())
        for x in x_range: # ? okay
            for y in y_range:
                for i, l in enumerate(self.layers):
                    if not l or not self.history.level.inside(QPoint(x, y)):
                        continue
                    if self.ishollow(x, y):
                        continue
                    block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(x, y, i))
                    self.history.level.l_geo.setlevelgeo(x, y, i, block)
                    t = self.module.get_layer(i)
                    t.draw_geo(x, y, True, self.inborder(x, y))
        self.redraw()


class GEEllipseChange(GEChange):
    def __init__(self, history, rect: QRect, replace, layers: [bool, bool, bool], hollow=False):
        super().__init__(history, replace, layers)
        self.rect = rect
        self.hollow = hollow
        self.area = np.ones((self.history.level.level_width, self.history.level.level_height), dtype=bool)
        #Replaced the 2D lists with NumPy arrays
        draw_ellipse(self.rect, self.hollow, self.drawpoint)
        self.redraw()

    def drawpoint(self, pos: QPoint, saveblock=True):
        if not self.area[pos.x(), pos.y()] and saveblock:
            return
        self.area[pos.x(), pos.y()] = False
        for i, l in enumerate(self.layers):
            if not l:
                continue
            block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(pos.x(), pos.y(), i))
            if saveblock:
                self.before.append([pos, i, save])
            self.history.level.l_geo.setlevelgeo(pos.x(), pos.y(), i, block)
            t = self.module.get_layer(i)
            t.draw_geo(pos.x(), pos.y(), True)

    def drawpointredo(self, pos):
        self.drawpoint(pos, False)

    def undo_changes(self):
        for i in self.before:
            point, layer, save = i
            block = geo_undo(self.replace, self.history.level.l_geo.getlevelgeo(point.x(), point.y(), layer), save)
            self.history.level.l_geo.setlevelgeo(point.x(), point.y(), layer, block)
            self.module.get_layer(layer).draw_geo(point.x(), point.y(), True)
        self.redraw()

    def redo_changes(self):
        draw_ellipse(self.rect, self.hollow, self.drawpointredo)
        self.redraw()


class GEPointChange(GEChange):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool]):
        super().__init__(history, replace, layers)
        self.positions: list[QPoint] = []
        self.start: QPoint = start
        self.before = {}
        self.paintpoint(start)
        self.redraw()

    def paintpoint(self, pos):
        for i, l in enumerate(self.layers):
            if not l:
                continue
            if not self.history.level.inside(pos):
                continue
            if self.before.get((pos, i), None) is not None:
                continue
            block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(pos.x(), pos.y(), i))
            self.before[(pos, i)] = save
            self.history.level.l_geo.setlevelgeo(pos.x(), pos.y(), i, block)
            t = self.module.get_layer(i)
            t.draw_geo(pos.x(), pos.y(), True)

    def add_move(self, position):
        start = self.start
        if len(self.positions) > 0:
            start = self.positions[-1]
        self.positions.append(position)

        points = []
        draw_line(start, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            self.paintpoint(point)
        self.redraw()

    def undo_changes(self):  # removing placed cells with replaced ones
        for k, v in self.before.items():
            block = geo_undo(self.replace, self.history.level.l_geo.getlevelgeo(k[0].x(), k[0].y(), k[1]), v)
            self.history.level.l_geo.setlevelgeo(k[0].x(), k[0].y(), k[1], block)
            t = self.module.get_layer(k[1])
            t.draw_geo(k[0].x(), k[0].y(), True)
        self.redraw()

    def redo_changes(self):  # re-adding replace cell
        for k, v in self.before.items():
            block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(k[0].x(), k[0].y(), k[1]))
            self.history.level.l_geo.setlevelgeo(k[0].x(), k[0].y(), k[1], block)
            t = self.module.get_layer(k[1])
            t.draw_geo(k[0].x(), k[0].y(), True)
        self.redraw()


class GEBrushChange(GEChange):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool], brushsize: int):
        super().__init__(history, replace, layers)
        self.start = start
        self.brushsize = brushsize
        self.area = np.ones((self.history.level.level_width, self.history.level.level_height), dtype=bool)
        self.lastpos = start
        self.paint_sphere(start, self.paintpoint)
        self.redraw()

    def paintpoint(self, pos: QPoint):
        if not self.history.level.inside(pos) or not self.area[pos.x(), pos.y()]:
            return
        for i, l in enumerate(self.layers):
            if not l:
                continue
            self.area[pos.x(), pos.y()] = False
            block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(pos.x(), pos.y(), i))
            self.before.append([pos, i, save])
            self.history.level.l_geo.setlevelgeo(pos.x(), pos.y(), i, block)
            t = self.module.get_layer(i)
            t.draw_geo(pos.x(), pos.y(), True)

    def paint_sphere(self, pos, callback):
        point = QPoint(self.brushsize // 2, self.brushsize // 2)
        rect = QRect(pos - point, pos + point)
        draw_ellipse(rect, False, callback)

    def add_move(self, position):
        points = []
        draw_line(self.lastpos, position, lambda p: points.append(p))
        points.pop(0)
        for point in points:
            self.paint_sphere(point, self.paintpoint)
        self.lastpos = position
        self.redraw()

    def undo_changes(self):
        for i in self.before:
            point, layer, save = i
            block = geo_undo(self.replace, self.history.level.l_geo.getlevelgeo(point.x(), point.y(), layer), save)
            self.history.level.l_geo.setlevelgeo(point.x(), point.y(), layer, block)
            self.module.get_layer(layer).draw_geo(point.x(), point.y(), True)
        self.redraw()

    def redo_changes(self):
        for i in self.before:
            pos, layer, _ = i
            block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(pos.x(), pos.y(), layer))
            self.history.level.l_geo.setlevelgeo(pos.x(), pos.y(), layer, block)
            t = self.module.get_layer(layer)
            t.draw_geo(pos.x(), pos.y(), True)
        self.redraw()


class GEFillChange(GEChange):
    def __init__(self, history, start: QPoint, replace: [int, bool], layers: [bool, bool, bool]):
        super().__init__(history, replace, layers)
        self.area = np.ones((3, self.history.level.level_width, self.history.level.level_height), dtype=bool)
        self.start: QPoint = start
        self.before = [[], [], []]
        self.replacefrom = [self.history.level.l_geo.getlevelgeo(start.x(), start.y(), 0)[0],
                            self.history.level.l_geo.getlevelgeo(start.x(), start.y(), 1)[0],
                            self.history.level.l_geo.getlevelgeo(start.x(), start.y(), 2)[0]]
        for i, l in enumerate(self.layers):
            if not l:
                continue
            self.drawpoint(start, i)
        self.dobrush()
        self.redraw()

    def dobrush(self, save=True):
        lastlen = 9999
        while True:
            for i, l in enumerate(self.layers):
                if not l:
                    continue
                for item in range(len(self.before[i])):
                    pos, _, val = self.before[i][item]
                    if not val:
                        continue
                    for p in nearpoints:
                        newpos = pos + p
                        if not self.history.level.inside(newpos) or not self.area[i][newpos.x(), newpos.y()]:
                            continue
                        self.area[i][newpos.x(), newpos.y()] = False
                        if self.history.level.l_geo.getlevelgeo(newpos.x(), newpos.y(), i)[0] != self.replacefrom[i]:
                            continue
                        self.drawpoint(newpos, i, save)
                    self.before[i][item][2] = False
            newlen = sum([len(i) for i in self.before])
            if newlen == lastlen:
                break
            lastlen = newlen
        self.redraw()

    def drawpoint(self, pos: QPoint, layer: int, saveblock=True):
        block, save = geo_save(self.replace, self.history.level.l_geo.getlevelgeo(pos.x(), pos.y(), layer))
        if saveblock:
            self.before[layer].append([pos, save, True])
        self.history.level.l_geo.setlevelgeo(pos.x(), pos.y(), layer, block)
        self.module.get_layer(layer).draw_geo(pos.x(), pos.y(), True)

    def undo_changes(self):
        for i, l in enumerate(self.before):
            for item in l:
                point, save, _ = item
                block = geo_undo(self.replace, self.history.level.l_geo.getlevelgeo(point.x(), point.y(), i), save)
                self.history.level.l_geo.setlevelgeo(point.x(), point.y(), i, block)
                self.module.get_layer(i).draw_geo(point.x(), point.y(), True)
        self.redraw()

    def redo_changes(self):
        for i, l in enumerate(self.before):
            for item in l:
                point, save, _ = item
                self.drawpoint(point, i, False)
        self.redraw()

class LevelResizedGeo(HistoryElement):
    def __init__(self, history, newrect: QRect):
        super().__init__(history)
        self.newrect = newrect
        self.oldblocks = None
        self.oldstack = None
        self.redo_changes()

    def undo_changes(self):
        self.level.l_geo.blocks = np.copy(self.oldblocks)
        self.level.l_geo.stack = np.copy(self.oldstack)

    def redo_changes(self):
        newshape = np.zeros((self.newrect.width(), self.newrect.height(), 3), np.uint8)
        newshapestack = np.zeros((self.newrect.width(), self.newrect.height(), 3), np.uint16)

        self.oldblocks = np.copy(self.level.l_geo.blocks)
        self.oldstack = np.copy(self.level.l_geo.stack)

        with np.nditer(newshape, flags=['multi_index'], op_flags=['writeonly']) as it:
            for x in it:
                if it.multi_index[0] < -self.newrect.x() or it.multi_index[1] < -self.newrect.y():
                    x[...] = 1
                    newshapestack[*it.multi_index] = 0
                    continue
                newpoints = [it.multi_index[0] + self.newrect.x(), it.multi_index[1] + self.newrect.y()]
                if newpoints[0] >= self.level.l_geo.blocks.shape[0] or newpoints[1] >= self.level.l_geo.blocks.shape[1]:
                    x[...] = 1
                    newshapestack[*it.multi_index] = 0
                    continue
                x[...] = self.level.l_geo.blocks[newpoints[0], newpoints[1], it.multi_index[2]]
                newshapestack[*it.multi_index] = self.level.l_geo.stack[newpoints[0], newpoints[1], it.multi_index[2]]

        self.level.l_geo.blocks = newshape
        self.level.l_geo.stack = newshapestack
