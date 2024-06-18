from core.Modify.baseModule import Module
from BaseMod.grid.gridRenderTexture import GridRenderTexture
from PySide6.QtCore import Slot, QRect
from core.configTypes.BaseTypes import BoolConfigurable, FloatConfigurable
from core.configTypes.QtTypes import KeyConfigurable


class GridModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.enablegrid = BoolConfigurable(mod, "enablegrid", False, "Enable grid")
        self.gridopacity = FloatConfigurable(mod, "gridopacity", .5, "Opacity grid")
        self.enablegrid_key = KeyConfigurable(mod, "enablegrid_key", "Alt+G", "Grid key")
        self.gridtexture = GridRenderTexture(self, 1000).add_myself()
        self.enablegrid.valueChanged.connect(self.check_change)
        self.gridopacity.valueChanged.connect(self.check_change)

        self.borders = self.viewport.workscene.addRect(QRect(0, 0, 1, 1))

    @Slot()
    def check_change(self):
        self.gridtexture.renderedtexture.setOpacity(self.gridopacity.value if self.enablegrid.value else 0)

    def render_module(self):
        self.check_change()
        self.gridtexture.draw_layer()
