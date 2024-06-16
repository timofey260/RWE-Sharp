from core.Modify.baseModule import Module
from BaseMod.geo.geoRenderTexture import GeoRenderTexture
from PySide6.QtCore import Qt, Slot
from core.configTypes.BaseTypes import BoolConfigurable, FloatConfigurable, IntConfigurable
from core.configTypes.QtTypes import KeyConfigurable


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
        self.opacityl1 = FloatConfigurable(mod, "VIEW_geo.opacityl1", .9, "opacity of the first layer")
        self.opacityl2 = FloatConfigurable(mod, "VIEW_geo.opacityl2", .5, "opacity of the second layer")
        self.opacityl3 = FloatConfigurable(mod, "VIEW_geo.opacityl3", .2, "opacity of the third layer")
        self.opacityrgb = FloatConfigurable(mod, "VIEW_geo.opacityrgb", .5, "opacity of all layers on old rendering option")

        self.drawlbeams = BoolConfigurable(mod, "VIEW_geo.drawlbeams", True, "Draw Beams")
        self.drawlpipes = BoolConfigurable(mod, "VIEW_geo.drawlpipes", True, "Draw pipes")
        self.drawlmisc = BoolConfigurable(mod, "VIEW_geo.drawlmisc", True, "Draw rocks, spears etc")

        self.drawoption = IntConfigurable(mod, "VIEW_geo.drawOption", 0, "method of drawing")

        self.drawlgeo_key = KeyConfigurable(mod, "VIEW_geo.drawlall_key", "Alt+G", "key to show geo")
        self.drawl1_key = KeyConfigurable(mod, "VIEW_geo.drawl1_key", "Alt+1", "key to show 1st layer")
        self.drawl2_key = KeyConfigurable(mod, "VIEW_geo.drawl2_key", "Alt+2", "key to show 2nd layer")
        self.drawl3_key = KeyConfigurable(mod, "VIEW_geo.drawl3_key", "Alt+3", "key to show 3rd layer")
        self.drawlbeams_key = KeyConfigurable(mod, "VIEW_geo.drawl3beamskey", "Alt+b", "key to show 3rd layer")
        self.drawlpipes_key = KeyConfigurable(mod, "VIEW_geo.drawlpipes_key", "Alt+v", "key to show 3rd layer")
        self.drawlmisc_key = KeyConfigurable(mod, "VIEW_geo.drawlmisc_key", "Alt+c", "key to show 3rd layer")
        self.draw = True
        self.l1 = GeoRenderTexture(self, 0)
        self.l2 = GeoRenderTexture(self, 1)
        self.l3 = GeoRenderTexture(self, 2)
        self.append_layer(100, self.l3)
        self.append_layer(200, self.l2)
        self.append_layer(300, self.l1)

        self.drawl1.valueChanged.connect(self.check_l1_change)
        self.drawl2.valueChanged.connect(self.check_l2_change)
        self.drawl3.valueChanged.connect(self.check_l3_change)
        self.drawlbeams.valueChanged.connect(self.check_beams_change)
        self.drawlpipes.valueChanged.connect(self.check_pipes_change)
        self.drawlmisc.valueChanged.connect(self.check_misc_change)
        self.drawoption.valueChanged.connect(self.redraw_option)
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
        if self.drawoption.value == 0:
            self.l1.renderedtexture.setOpacity(self.opacityl1.value if self.drawl1.value else 0)
            return
        self.l1.renderedtexture.setOpacity(self.opacityrgb.value if self.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if self.drawoption.value == 0:
            self.l2.renderedtexture.setOpacity(self.opacityl2.value if self.drawl2.value else 0)
            return
        self.l2.renderedtexture.setOpacity(self.opacityrgb.value if self.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        if self.drawoption.value == 0:
            self.l3.renderedtexture.setOpacity(self.opacityl3.value if self.drawl3.value else 0)
            return
        self.l3.renderedtexture.setOpacity(self.opacityrgb.value if self.drawl3.value else 0)

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
