from RWESharp.Renderable import Renderable

from PySide6.QtGui import QTransform, QPolygonF, QPainter, QPixmap

from widgets import Viewport


class PropRenderable(Renderable):
    def __init__(self, mod, depth, prop):
        super().__init__(mod, depth)
        prop = self.mod.manager.props.find_prop(prop[1])
        if prop is None:
            pass
        transform = prop[3]

    def init_graphics(self, viewport: Viewport):
        pass

    def remove_graphics(self):
        pass

    def zoom_event(self, zoom):
        pass