from core.Modify.baseModule import Module
from BaseMod.geo.geoRenderTexture import GeoRenderTexture
from PySide6.QtCore import Qt, Slot


class GeoModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.l1 = GeoRenderTexture(self, 0)
        self.l2 = GeoRenderTexture(self, 1)
        self.l3 = GeoRenderTexture(self, 2)
        self.editorlayers.append((100, self.l3))
        self.editorlayers.append((200, self.l2))
        self.editorlayers.append((300, self.l1))
        # self.manager.window.ui.ToolGeoApplyToL1.checkStateChanged.connect(self.check_l1_change)
        # self.manager.window.ui.ToolGeoApplyToL2.checkStateChanged.connect(self.check_l2_change)
        # self.manager.window.ui.ToolGeoApplyToL3.checkStateChanged.connect(self.check_l3_change)

    @Slot(Qt.CheckState)
    def check_l1_change(self, state: Qt.CheckState):
        self.drawl1 = state == Qt.CheckState.Checked
        self.l1.renderedtexture.setOpacity(1 if self.drawl1 else 0)

    @Slot(Qt.CheckState)
    def check_l2_change(self, state: Qt.CheckState):
        self.drawl2 = state == Qt.CheckState.Checked
        self.l2.renderedtexture.setOpacity(1 if self.drawl2 else 0)

    @Slot(Qt.CheckState)
    def check_l3_change(self, state: Qt.CheckState):
        self.drawl3 = state == Qt.CheckState.Checked
        self.l2.renderedtexture.setOpacity(1 if self.drawl3 else 0)

    def init_module_textures(self):
        self.l1.renderedtexture.setOpacity(.9)
        self.l2.renderedtexture.setOpacity(.5)
        self.l3.renderedtexture.setOpacity(.2)