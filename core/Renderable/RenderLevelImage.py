from PySide6.QtCore import QSize
from core.Renderable.RenderImage import RenderImage
from core.info import CELLSIZE


class RenderLevelImage(RenderImage):
    def __init__(self, mod, depth):
        super().__init__(mod, depth, QSize(mod.manager.level_width * CELLSIZE, mod.manager.level_height * CELLSIZE))
