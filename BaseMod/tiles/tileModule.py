import os.path

from core.Modify.baseModule import Module
from BaseMod.tiles.tileRenderTexture import TileRenderTexture
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QImage, QColor
from core.Loaders.TileLoader import palette_to_colortable


class TileModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        print(self.mod.tileviewconfig.palettepath.value)
        if not os.path.exists(self.mod.tileviewconfig.palettepath.value):
            self.mod.tileviewconfig.palettepath.reset_value()
        self.mod.tileviewconfig.palettepath.valueChanged.connect(self.change_colortable)
        self.change_colortable()
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
    def change_colortable(self):
        self.colortable = palette_to_colortable(QImage(self.mod.tileviewconfig.palettepath.value))

    @Slot()
    def redraw_option(self):
        self.render_module(True)
        self.init_module_textures()

    def init_module_textures(self):
        self.check_l1_change()
        self.check_l2_change()
        self.check_l3_change()

    @Slot()
    def check_l1_change(self):
        if self.mod.tileviewconfig.drawoption.value > 2:
            self.l1.renderedtexture.setOpacity(
                self.mod.tileviewconfig.drawl1rendered.value if self.mod.tileviewconfig.drawl1.value else 0)
            return
        self.l1.renderedtexture.setOpacity(
            self.mod.tileviewconfig.drawl1notrendered.value if self.mod.tileviewconfig.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if self.mod.tileviewconfig.drawoption.value > 2:
            self.l2.renderedtexture.setOpacity(
                self.mod.tileviewconfig.drawl2rendered.value if self.mod.tileviewconfig.drawl2.value else 0)
            return
        self.l2.renderedtexture.setOpacity(
            self.mod.tileviewconfig.drawl2notrendered.value if self.mod.tileviewconfig.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        if self.mod.tileviewconfig.drawoption.value > 2:
            self.l3.renderedtexture.setOpacity(
                self.mod.tileviewconfig.drawl3rendered.value if self.mod.tileviewconfig.drawl3.value else 0)
            return
        self.l3.renderedtexture.setOpacity(
            self.mod.tileviewconfig.drawl3notrendered.value if self.mod.tileviewconfig.drawl3.value else 0)

    def render_module(self, clear=False):
        self.l1.draw_layer(clear)
        self.l2.draw_layer(clear)
        self.l3.draw_layer(clear)
        if self.mod.tileviewconfig.drawoption.value == 6:
            self.manager.viewport.rect.setBrush(self.colortable[4])
        elif self.mod.tileviewconfig.drawoption.value in [4, 5]:
            self.manager.viewport.rect.setBrush(self.colortable[3])
        elif self.mod.tileviewconfig.drawoption.value == 3:
            self.manager.viewport.rect.setBrush(QColor(255, 255, 255))
        else:
            self.manager.viewport.rect.setBrush(self.manager.basemod.config.backgroundcolor.value)

    def get_layer(self, layer: int) -> TileRenderTexture:
        return [self.l1, self.l2, self.l3][layer]

