from PySide6.QtCore import Slot, Signal

from BaseMod.geo.geoRenderTexture import GeoRenderLevelImage
from RWESharp.Modify import Module


class GeoModule(Module):
    layerChanged = Signal(int)

    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.ui = self.mod.geoview

        self.draw = True
        self.l1 = GeoRenderLevelImage(self, 150, 0)
        self.l2 = GeoRenderLevelImage(self, 250, 1)
        self.l3 = GeoRenderLevelImage(self, 350, 2)

        self.ui.drawl1.valueChanged.connect(self.check_l1_change)
        self.ui.drawl2.valueChanged.connect(self.check_l2_change)
        self.ui.drawl3.valueChanged.connect(self.check_l3_change)
        self.ui.opacityl1.valueChanged.connect(self.check_l1_change)
        self.ui.opacityl2.valueChanged.connect(self.check_l2_change)
        self.ui.opacityl3.valueChanged.connect(self.check_l3_change)
        self.ui.opacityrgb.valueChanged.connect(self.init_module_textures)
        self.ui.opacityshift.valueChanged.connect(self.init_module_textures)

        self.ui.drawlbeams.valueChanged.connect(self.check_beams_change)
        self.ui.drawlpipes.valueChanged.connect(self.check_pipes_change)
        self.ui.drawlmisc.valueChanged.connect(self.check_misc_change)
        self.ui.drawoption.valueChanged.connect(self.render_module)
        self.ui.render.connect(self.render_module)
        self.ui.imagepath.valueChanged.connect(self.update_image)

    def update_image(self):
        self.l1.update_image()
        self.l1.draw_layer(True)
        self.l2.update_image()
        self.l2.draw_layer(True)
        self.l3.update_image()
        self.l3.draw_layer(True)

    @Slot()
    def check_l1_change(self):
        if not self.ui.drawgeo.value:
            self.l1.renderedtexture.setOpacity(0)
            return
        if self.ui.opacityshift.value:
            self.check_l2_change()
        if self.ui.drawoption.value == 0:
            self.l1.renderedtexture.setOpacity(self.ui.opacityl1.value if self.ui.drawl1.value else 0)
            return
        self.l1.renderedtexture.setOpacity(self.ui.opacityrgb.value if self.ui.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if not self.ui.drawgeo.value:
            self.l2.renderedtexture.setOpacity(0)
            return
        if self.ui.opacityshift.value:
            self.check_l3_change()
        if self.ui.drawoption.value == 0:
            if self.ui.opacityshift.value and self.ui.drawl2.value:
                opval = self.ui.opacityl1.value if not self.ui.drawl1.value else \
                        self.ui.opacityl2.value
            else:
                opval = self.ui.opacityl2.value if self.ui.drawl2.value else 0
            self.l2.renderedtexture.setOpacity(opval)
            return
        self.l2.renderedtexture.setOpacity(self.ui.opacityrgb.value if self.ui.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        if not self.ui.drawgeo.value:
            self.l3.renderedtexture.setOpacity(0)
            return
        if self.ui.drawoption.value == 0:
            if self.ui.opacityshift.value and self.ui.drawl3.value:
                opval = self.ui.opacityl1.value if not self.ui.drawl1.value and not self.ui.drawl2.value else \
                        self.ui.opacityl2.value if not self.ui.drawl2.value or not self.ui.drawl1.value else \
                        self.ui.opacityl3.value
            else:
                opval = self.ui.opacityl3.value if self.ui.drawl3.value else 0
            self.l3.renderedtexture.setOpacity(opval)
            return
        self.l3.renderedtexture.setOpacity(self.ui.opacityrgb.value if self.ui.drawl3.value else 0)

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
        self.init_module_textures()

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.render_module()

    def get_layer(self, layer: int) -> GeoRenderLevelImage:
        return [self.l1, self.l2, self.l3][layer]
