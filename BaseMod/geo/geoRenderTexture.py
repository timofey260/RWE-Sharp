import os.path

from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap, QColor, QPainter

from RWESharp.Core import PATH_FILES_IMAGES, CONSTS, CELLSIZE
from RWESharp.Renderable import RenderTexture


class GeoRenderTexture(RenderTexture):
    def __init__(self, module, depth, geolayer):
        super().__init__(module, depth)
        self.geolayer = geolayer

        if os.path.exists(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image"))):
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image")))
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))
        self.geo_texture_colored = self.geo_texture.copy()
        cp = QPainter(self.geo_texture_colored)  # it's color painter i swear
        cp.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceAtop)
        op = 50
        cp.fillRect(self.geo_texture.rect(), [0, QColor(0, 255, 0, op), QColor(255, 0, 0, op)][self.geolayer])
        #self.painter.drawPixmap(QRect(0, 0, 20, 20), self.geo_texture, QRect(100, 100, 100, 100))
        self.binfo: dict = CONSTS.get("geo_image_config", {}).get("blocksinfo", {})
        self.sinfo: dict = CONSTS.get("geo_image_config", {}).get("stackablesinfo", {})
        self._sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        # self.draw_layer()

    def draw_layer(self):
        self.image.fill(QColor(0, 0, 0, 0))
        for xp, x in enumerate(self.manager.level["GE"]):
            for yp, y in enumerate(x):
                self.draw_geo(xp, yp)
        self.redraw()

    def redraw_beams(self):
        for xp, x in enumerate(self.manager.level["GE"]):
            for yp, y in enumerate(x):
                if 1 in y[self.geolayer][1] or 2 in y[self.geolayer][1]:
                    self.draw_geo(xp, yp, True)
        self.redraw()

    def redraw_misc(self):
        for xp, x in enumerate(self.manager.level["GE"]):
            for yp, y in enumerate(x):
                self.draw_geo(xp, yp, True)
        self.redraw()

    def redraw_pipes(self):
        for xp, x in enumerate(self.manager.level["GE"]):
            for yp, y in enumerate(x):
                if 5 in y[self.geolayer][1] or 6 in y[self.geolayer][1] or 7 in y[self.geolayer][1] or 19 in y[self.geolayer][1]:
                    self.draw_geo(xp, yp, True)
        self.redraw()

    def draw_geo(self, x: int, y: int, clear: bool = False, updatearound: bool = False):
        cell: int = self.manager.level["GE"][x][y][self.geolayer][0]
        stackables: list[int] = self.manager.level["GE"][x][y][self.geolayer][1]
        pos = self.binfo.get(str(cell), [0, 0])
        cellpos = QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz)
        placepos = QRect(x * CELLSIZE, y * CELLSIZE, 20, 20)
        drawmap = self.geo_texture if self.module.drawoption.value == 0 else self.geo_texture_colored
        if clear:
            self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_Clear)
            self.painter.fillRect(placepos, QColor(0, 0, 0, 0))
            self.painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceOver)
        self.painter.drawPixmap(placepos, drawmap, cellpos)
        for s in stackables:
            if (s == 1 or s == 2) and not self.module.drawlbeams.value:
                continue
            elif s in [5, 6, 7, 19] and not self.module.drawlpipes.value:
                continue
            elif s not in [1, 2, 5, 6, 7, 19] and not self.module.drawlmisc.value:
                continue
            if s == 4:
                # checking structures
                continue
            spos = self.sinfo.get(str(s), [0, 0])
            stackpos = QRect(spos[0] * self._sz, spos[1] * self._sz, self._sz, self._sz)
            self.painter.drawPixmap(placepos, drawmap, stackpos)
