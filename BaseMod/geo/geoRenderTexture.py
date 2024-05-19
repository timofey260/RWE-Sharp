import os.path
from core.Modify.RenderTexture import RenderTexture
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import QRect
from core.info import PATH_FILES_IMAGES, CONSTS, CELLSIZE

class GeoRenderTexture(RenderTexture):
    def __init__(self, module, layer):
        super().__init__(module)
        self.layer = layer

        if os.path.exists(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image"))):
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, CONSTS.get("geo_image_config", {}).get("image")))
        else:
            self.geo_texture = QPixmap(os.path.join(PATH_FILES_IMAGES, "notfound.png"))
        #self.painter.drawPixmap(QRect(0, 0, 20, 20), self.geo_texture, QRect(100, 100, 100, 100))
        self.binfo: dict = CONSTS.get("geo_image_config", {}).get("blocksinfo", {})
        self.sinfo: dict = CONSTS.get("geo_image_config", {}).get("stackablesinfo", {})
        self._sz = CONSTS.get("geo_image_config", {}).get("itemsize", 100)
        self.draw_layer()


    def draw_layer(self):
        self.image.fill(QColor(0, 0, 0, 0))
        for xp, x in enumerate(self.manager.level["GE"]):
            for yp, y in enumerate(x):
                self.draw_geo(xp, yp)


    def draw_geo(self, x: int, y: int):
        cell = self.manager.level["GE"][x][y][self.layer][0]
        stackables = self.manager.level["GE"][x][y][self.layer][1]
        pos = self.binfo.get(str(cell), [0, 0])
        cellpos = QRect(pos[0] * self._sz, pos[1] * self._sz, self._sz, self._sz)
        placepos = QRect(x * CELLSIZE, y * CELLSIZE, 20, 20)
        self.painter.drawPixmap(placepos, self.geo_texture, cellpos)

        for s in stackables:
            spos = self.sinfo.get(str(s), [0, 0])
            stackpos = QRect(spos[0] * self._sz, spos[1] * self._sz, self._sz, self._sz)
            self.painter.drawPixmap(placepos, self.geo_texture, stackpos)

