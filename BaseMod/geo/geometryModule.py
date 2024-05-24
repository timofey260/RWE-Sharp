from core.Modify.baseModule import Module
from BaseMod.geo.geoRenderTexture import GeoRenderTexture
from PySide6.QtCore import Qt, Slot


class GeoModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        from ..baseMod import BaseMod
        self.mod: BaseMod
        self.drawbeams = True
        self.drawmisc = True
        self.drawpipes = True
        self.l1 = GeoRenderTexture(self, 0)
        self.l2 = GeoRenderTexture(self, 1)
        self.l3 = GeoRenderTexture(self, 2)
        self.editorlayers.append((100, self.l3))
        self.editorlayers.append((200, self.l2))
        self.editorlayers.append((300, self.l1))
        self.mod.geoviewconfig.drawl1.valueChanged.connect(self.check_l1_change)
        self.mod.geoviewconfig.drawl2.valueChanged.connect(self.check_l2_change)
        self.mod.geoviewconfig.drawl3.valueChanged.connect(self.check_l3_change)
        self.mod.geoviewconfig.drawlbeams.valueChanged.connect(self.check_beams_change)
        self.mod.geoviewconfig.drawlpipes.valueChanged.connect(self.check_pipes_change)
        self.mod.geoviewconfig.drawlmisc.valueChanged.connect(self.check_misc_change)



    @Slot()
    def check_l1_change(self):
        self.l1.renderedtexture.setOpacity(self.mod.config.opacityl1.value if self.mod.geoviewconfig.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        self.l2.renderedtexture.setOpacity(self.mod.config.opacityl2.value if self.mod.geoviewconfig.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        self.l3.renderedtexture.setOpacity(self.mod.config.opacityl3.value if self.mod.geoviewconfig.drawl3.value else 0)

    # a lot of bullshit functions to speed up rendering
    @Slot()
    def check_beams_change(self):
        self.l1.redraw_beams()
        self.l2.redraw_beams()
        self.l3.redraw_beams()

    @Slot()
    def check_misc_change(self):
        self.l1.redraw_misc()
        self.l2.redraw_misc()
        self.l3.redraw_misc()

    @Slot()
    def check_pipes_change(self):
        self.l1.redraw_pipes()
        self.l2.redraw_pipes()
        self.l3.redraw_pipes()

    def init_module_textures(self):
        self.l1.renderedtexture.setOpacity(self.mod.config.opacityl1.value if self.mod.geoviewconfig.drawl1.value else 0)
        self.l2.renderedtexture.setOpacity(self.mod.config.opacityl2.value if self.mod.geoviewconfig.drawl2.value else 0)
        self.l3.renderedtexture.setOpacity(self.mod.config.opacityl3.value if self.mod.geoviewconfig.drawl3.value else 0)