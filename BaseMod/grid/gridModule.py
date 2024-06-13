from core.Modify.baseModule import Module
from BaseMod.grid.gridRenderTexture import GridRenderTexture
from PySide6.QtCore import Slot
from core.configTypes.BaseTypes import BoolConfigurable, FloatConfigurable
from core.configTypes.QtTypes import KeyConfigurable


class GridModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.enablegrid = BoolConfigurable(mod, "enablegrid", False, "Enable grid")
        self.gridopacity = FloatConfigurable(mod, "gridopacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(mod, "enablegrid_key", "Alt+G", "Grid key")
        self.gridtexture = GridRenderTexture(self)
        self.append_layer(1000, self.gridtexture)
        self.enablegrid.valueChanged.connect(self.check_change)
        self.gridopacity.valueChanged.connect(self.check_change)

    @Slot()
    def check_change(self):
        self.gridtexture.renderedtexture.setOpacity(self.gridopacity.value if self.enablegrid.value else 0)

    def render_module(self):
        self.check_change()
        self.gridtexture.draw_layer()
