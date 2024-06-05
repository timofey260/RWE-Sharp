from core.Modify.baseModule import Module
from BaseMod.geo.geoRenderTexture import GeoRenderTexture
from PySide6.QtCore import Qt, Slot


class GeoModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        from ..baseMod import BaseMod
        self.mod: BaseMod
        self.draw = True
        self.l1 = GeoRenderTexture(self, 0)
        self.l2 = GeoRenderTexture(self, 1)
        self.l3 = GeoRenderTexture(self, 2)
        self.append_layer(100, self.l3)
        self.append_layer(200, self.l2)
        self.append_layer(300, self.l1)
        self.mod.geoviewconfig.drawl1.valueChanged.connect(self.check_l1_change)
        self.mod.geoviewconfig.drawl2.valueChanged.connect(self.check_l2_change)
        self.mod.geoviewconfig.drawl3.valueChanged.connect(self.check_l3_change)
        self.mod.geoviewconfig.drawlbeams.valueChanged.connect(self.check_beams_change)
        self.mod.geoviewconfig.drawlpipes.valueChanged.connect(self.check_pipes_change)
        self.mod.geoviewconfig.drawlmisc.valueChanged.connect(self.check_misc_change)
        self.mod.geoviewconfig.drawoption.valueChanged.connect(self.redraw_option)

    @Slot()
    def check_l1_change(self):
        if self.mod.geoviewconfig.drawoption.value == 0:
            self.l1.renderedtexture.setOpacity(
                self.mod.geoviewconfig.opacityl1.value if self.mod.geoviewconfig.drawl1.value else 0)
            return
        self.l1.renderedtexture.setOpacity(
            self.mod.geoviewconfig.opacityrgb.value if self.mod.geoviewconfig.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if self.mod.geoviewconfig.drawoption.value == 0:
            self.l2.renderedtexture.setOpacity(
                self.mod.geoviewconfig.opacityl2.value if self.mod.geoviewconfig.drawl2.value else 0)
            return
        self.l2.renderedtexture.setOpacity(
            self.mod.geoviewconfig.opacityrgb.value if self.mod.geoviewconfig.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        if self.mod.geoviewconfig.drawoption.value == 0:
            self.l3.renderedtexture.setOpacity(
                self.mod.geoviewconfig.opacityl3.value if self.mod.geoviewconfig.drawl3.value else 0)
            return
        self.l3.renderedtexture.setOpacity(
            self.mod.geoviewconfig.opacityrgb.value if self.mod.geoviewconfig.drawl3.value else 0)

    @Slot()
    def redraw_option(self):
        self.render_module()
        self.init_module_textures()

    # a lot of bullshit functions to speed up rendering
    @Slot()
    def check_beams_change(self):
        if not self.draw:
            return
        self.l1.redraw_beams()
        self.l2.redraw_beams()
        self.l3.redraw_beams()

    @Slot()
    def check_misc_change(self):
        if not self.draw:
            return
        self.l1.redraw_misc()
        self.l2.redraw_misc()
        self.l3.redraw_misc()

    @Slot()
    def check_pipes_change(self):
        if not self.draw:
            return
        self.l1.redraw_pipes()
        self.l2.redraw_pipes()
        self.l3.redraw_pipes()

    def init_module_textures(self):
        self.check_l1_change()
        self.check_l2_change()
        self.check_l3_change()

    def render_module(self):
        self.l1.draw_layer()
        self.l2.draw_layer()
        self.l3.draw_layer()

    def get_layer(self, layer: int) -> GeoRenderTexture:
        return [self.l1, self.l2, self.l3][layer]
