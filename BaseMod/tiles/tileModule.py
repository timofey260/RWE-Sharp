from core.Modify.baseModule import Module
from BaseMod.tiles.tileRenderTexture import TileRenderTexture
from PySide6.QtCore import Qt, Slot


class TileModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.l1 = TileRenderTexture(self, 0)
        self.l2 = TileRenderTexture(self, 1)
        self.l3 = TileRenderTexture(self, 2)
        self.append_layer(150, self.l3)
        self.append_layer(250, self.l2)
        self.append_layer(350, self.l1)
        self.mod.tileviewconfig.drawl1.valueChanged.connect(self.check_l1_change)
        self.mod.tileviewconfig.drawl2.valueChanged.connect(self.check_l2_change)
        self.mod.tileviewconfig.drawl3.valueChanged.connect(self.check_l3_change)
        self.mod.tileviewconfig.drawoption.valueChanged.connect(self.redraw_option)

    @Slot()
    def redraw_option(self):
        print("rerendered! ")
        self.render_module(True)

    def init_module_textures(self):
        self.l1.renderedtexture.setOpacity(self.mod.config.opacityl1.value)
        self.l2.renderedtexture.setOpacity(self.mod.config.opacityl2.value)
        self.l3.renderedtexture.setOpacity(self.mod.config.opacityl3.value)

    @Slot()
    def check_l1_change(self):
        self.l1.renderedtexture.setOpacity(
            self.mod.config.opacityl1.value if self.mod.tileviewconfig.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        self.l2.renderedtexture.setOpacity(
            self.mod.config.opacityl2.value if self.mod.tileviewconfig.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        self.l3.renderedtexture.setOpacity(
            self.mod.config.opacityl3.value if self.mod.tileviewconfig.drawl3.value else 0)

    def render_module(self, clear=False):
        self.l1.draw_layer(clear)
        self.l2.draw_layer(clear)
        self.l3.draw_layer(clear)
