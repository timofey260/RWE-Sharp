from PySide6.QtCore import Slot

from BaseMod.geo.geoRenderTexture import GeoRenderLevelImage
from RWESharp.Configurable import BoolConfigurable, FloatConfigurable, IntConfigurable
from RWESharp.Modify import Module


class GeoModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.drawgeo = BoolConfigurable(mod, "VIEW_geo.drawgeo", True, "Draw geometry")
        self.drawAll = BoolConfigurable(mod, "VIEW_geo.drawall", False, "Draw all layers")
        self.drawl1 = BoolConfigurable(mod, "VIEW_geo.drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable(mod, "VIEW_geo.drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable(mod, "VIEW_geo.drawl3", True, "Draw layer 3")
        self.opacityl1 = FloatConfigurable(mod, "VIEW_geo.opacityl1", .9, "Opacity of the first layer")
        self.opacityl2 = FloatConfigurable(mod, "VIEW_geo.opacityl2", .5, "Opacity of the second layer")
        self.opacityl3 = FloatConfigurable(mod, "VIEW_geo.opacityl3", .2, "Opacity of the third layer")
        self.opacityrgb = FloatConfigurable(mod, "VIEW_geo.opacityrgb", .5, "Opacity of all layers on old rendering option")

        self.drawlbeams = BoolConfigurable(mod, "VIEW_geo.drawlbeams", True, "Draw Beams")
        self.drawlpipes = BoolConfigurable(mod, "VIEW_geo.drawlpipes", True, "Draw pipes")
        self.drawlmisc = BoolConfigurable(mod, "VIEW_geo.drawlmisc", True, "Draw rocks, spears etc")

        self.drawoption = IntConfigurable(mod, "VIEW_geo.drawOption", 0, "method of drawing")
        self.opacityshift = BoolConfigurable(mod, "VIEW_geo.opacityShift", True, "Does not change opacity of hidden layers")

        self.draw = True
        self.l1 = GeoRenderLevelImage(self, 150, 0).add_myself(self)
        self.l2 = GeoRenderLevelImage(self, 250, 1).add_myself(self)
        self.l3 = GeoRenderLevelImage(self, 350, 2).add_myself(self)

        self.drawl1.valueChanged.connect(self.check_l1_change)
        self.drawl2.valueChanged.connect(self.check_l2_change)
        self.drawl3.valueChanged.connect(self.check_l3_change)
        self.opacityl1.valueChanged.connect(self.check_l1_change)
        self.opacityl2.valueChanged.connect(self.check_l2_change)
        self.opacityl3.valueChanged.connect(self.check_l3_change)
        self.opacityrgb.valueChanged.connect(self.init_module_textures)
        self.opacityshift.valueChanged.connect(self.init_module_textures)

        self.drawlbeams.valueChanged.connect(self.check_beams_change)
        self.drawlpipes.valueChanged.connect(self.check_pipes_change)
        self.drawlmisc.valueChanged.connect(self.check_misc_change)
        self.drawoption.valueChanged.connect(self.render_module)
        self.drawgeo.valueChanged.connect(self.hide_geo)

    @Slot()
    def hide_geo(self):
        self.draw = False
        self.drawl1.update_value(self.drawgeo.value)
        self.drawl2.update_value(self.drawgeo.value)
        self.drawl3.update_value(self.drawgeo.value)
        self.draw = True
        self.render_module()

    @Slot()
    def check_l1_change(self):
        if not self.drawgeo.value:
            self.l1.renderedtexture.setOpacity(0)
            return
        if self.opacityshift.value:
            self.check_l2_change()
        if self.drawoption.value == 0:
            self.l1.renderedtexture.setOpacity(self.opacityl1.value if self.drawl1.value else 0)
            return
        self.l1.renderedtexture.setOpacity(self.opacityrgb.value if self.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if not self.drawgeo.value:
            self.l2.renderedtexture.setOpacity(0)
            return
        if self.opacityshift.value:
            self.check_l3_change()
        if self.drawoption.value == 0:
            if self.opacityshift.value and self.drawl2.value:
                opval = self.opacityl1.value if not self.drawl1.value else \
                        self.opacityl2.value
            else:
                opval = self.opacityl2.value if self.drawl2.value else 0
            self.l2.renderedtexture.setOpacity(opval)
            return
        self.l2.renderedtexture.setOpacity(self.opacityrgb.value if self.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        if not self.drawgeo.value:
            self.l3.renderedtexture.setOpacity(0)
            return
        if self.drawoption.value == 0:
            if self.opacityshift.value and self.drawl3.value:
                opval = self.opacityl1.value if not self.drawl1.value and not self.drawl2.value else \
                        self.opacityl2.value if not self.drawl2.value or not self.drawl1.value else \
                        self.opacityl3.value
            else:
                opval = self.opacityl3.value if self.drawl3.value else 0
            self.l3.renderedtexture.setOpacity(opval)
            return
        self.l3.renderedtexture.setOpacity(self.opacityrgb.value if self.drawl3.value else 0)

    def showlayer(self, currentlayer):
        self.drawl1.update_value(currentlayer == 0)
        self.drawl2.update_value(currentlayer <= 1)
        self.drawl3.update_value(True)

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

    def get_layer(self, layer: int) -> GeoRenderLevelImage:
        return [self.l1, self.l2, self.l3][layer]
