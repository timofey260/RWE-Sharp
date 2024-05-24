from core.Modify.baseModule import Module
from BaseMod.geo.geoRenderTexture import GeoRenderTexture
from PySide6.QtCore import Qt, Slot


class GeoModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.drawl1 = True
        self.drawl2 = True
        self.drawl3 = True
        self.drawbeams = True
        self.drawmisc = True
        self.drawpipes = True
        self.l1 = GeoRenderTexture(self, 0)
        self.l2 = GeoRenderTexture(self, 1)
        self.l3 = GeoRenderTexture(self, 2)
        self.editorlayers.append((100, self.l3))
        self.editorlayers.append((200, self.l2))
        self.editorlayers.append((300, self.l1))

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_l1_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawl1 = state
        else:
            self.drawl1 = state == Qt.CheckState.Checked
        self.l1.renderedtexture.setOpacity(self.mod.config.opacityl1.value if self.drawl1 else 0)

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_l2_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawl2 = state
        else:
            self.drawl2 = state == Qt.CheckState.Checked
        self.l2.renderedtexture.setOpacity(self.mod.config.opacityl2.value if self.drawl2 else 0)

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_l3_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawl3 = state
        else:
            self.drawl3 = state == Qt.CheckState.Checked
        self.l3.renderedtexture.setOpacity(self.mod.config.opacityl3.value if self.drawl3 else 0)

    @Slot(Qt.CheckState) # a lot of bullshit functions to speed up rendering
    @Slot(bool)
    def check_beams_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawbeams = state
        else:
            self.drawbeams = state == Qt.CheckState.Checked
        self.l1.redraw_beams()
        self.l2.redraw_beams()
        self.l3.redraw_beams()

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_misc_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawmisc = state
        else:
            self.drawmisc = state == Qt.CheckState.Checked
        self.l1.redraw_misc()
        self.l2.redraw_misc()
        self.l3.redraw_misc()

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_pipes_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawpipes = state
        else:
            self.drawpipes = state == Qt.CheckState.Checked
        self.l1.redraw_pipes()
        self.l2.redraw_pipes()
        self.l3.redraw_pipes()


    def init_module_textures(self):
        self.l1.renderedtexture.setOpacity(self.mod.config.opacityl1.value)
        self.l2.renderedtexture.setOpacity(self.mod.config.opacityl2.value)
        self.l3.renderedtexture.setOpacity(self.mod.config.opacityl3.value)