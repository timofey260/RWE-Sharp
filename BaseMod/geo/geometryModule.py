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

        self.ui.drawl1.valueChanged.connect(self.check_layers_change)
        self.ui.drawl2.valueChanged.connect(self.check_layers_change)
        self.ui.drawl3.valueChanged.connect(self.check_layers_change)
        self.ui.popacity.valueChanged.connect(self.check_layers_change)
        self.ui.sopacity.valueChanged.connect(self.check_layers_change)
        self.ui.sopacityrgb.valueChanged.connect(self.check_layers_change)
        self.ui.popacityrgb.valueChanged.connect(self.init_module_textures)
        self.ui.renderall.valueChanged.connect(self.remove_items_from_scene)

        self.ui.drawlbeams.valueChanged.connect(self.check_beams_change)
        self.ui.drawlpipes.valueChanged.connect(self.check_pipes_change)
        self.ui.drawlmisc.valueChanged.connect(self.check_misc_change)
        self.ui.drawoption.valueChanged.connect(self.render_module)
        self.ui.render.connect(self.render_module)
        self.ui.imagepath.valueChanged.connect(self.update_image)
        self.manager.layer.valueChanged.connect(self.init_module_textures)

    def update_image(self):
        self.l1.update_image()
        self.l1.draw_layer(True)
        self.l2.update_image()
        self.l2.draw_layer(True)
        self.l3.update_image()
        self.l3.draw_layer(True)

    @Slot()
    def check_layers_change(self):
        if self.ui.drawoption.value == 1:
            self.l1.setOpacity(self.ui.popacityrgb.value if self.layer == 0 else self.ui.sopacityrgb.value)
            self.l2.setOpacity(self.ui.popacityrgb.value if self.layer == 1 else self.ui.sopacityrgb.value)
            self.l3.setOpacity(self.ui.popacityrgb.value if self.layer == 2 else self.ui.sopacityrgb.value)
            return
        self.l1.setOpacity(self.ui.popacity.value if self.layer == 0 else self.ui.sopacity.value)
        if self.layer == 1 and not self.ui.renderall.value:
            self.l1.setOpacity(0)
        self.l2.setOpacity(self.ui.popacity.value if self.layer == 1 else self.ui.sopacity.value)
        if self.layer == 2 and not self.ui.renderall.value:
            self.l1.setOpacity(0)
            self.l2.setOpacity(0)
        self.l3.setOpacity(self.ui.popacity.value if self.layer == 2 else self.ui.sopacity.value)

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
        self.check_layers_change()

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
