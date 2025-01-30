from RWESharp.Renderable import RenderRect
from PySide6.QtCore import QRect, QPoint


class RenderCamera(RenderRect):
    def __init__(self, module, depth, pos):

        super().__init__(module, depth)
