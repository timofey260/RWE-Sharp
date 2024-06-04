from core.Modify.baseModule import Module
from .gridRenderTexture import GridRenderTexture
from PySide6.QtCore import Slot


class GridModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.gridtexture = GridRenderTexture(self)
        self.append_layer(1000, self.gridtexture)
        self.mod.gridconfig.enablegrid.valueChanged.connect(self.check_change)
        self.mod.gridconfig.gridopacity.valueChanged.connect(self.check_change)

    @Slot()
    def check_change(self):
        self.gridtexture.renderedtexture.setOpacity(
            self.mod.gridconfig.gridopacity.value if self.mod.gridconfig.enablegrid.value else 0)

    def render_module(self):
        self.check_change()
        self.gridtexture.draw_layer()
