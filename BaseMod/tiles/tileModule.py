from core.Modify.baseModule import Module
from BaseMod.tiles.tileRenderTexture import TileRenderTexture
from PySide6.QtCore import Qt, Slot


class TileModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.drawl1 = True
        self.drawl2 = True
        self.drawl3 = True
        self.l1 = TileRenderTexture(self, 0)
        self.l2 = TileRenderTexture(self, 1)
        self.l3 = TileRenderTexture(self, 2)
        self.editorlayers.append((150, self.l3))
        self.editorlayers.append((250, self.l2))
        self.editorlayers.append((350, self.l1))

    def init_module_textures(self):
        self.l1.renderedtexture.setOpacity(self.mod.config.opacityl1.value)
        self.l2.renderedtexture.setOpacity(self.mod.config.opacityl2.value)
        self.l3.renderedtexture.setOpacity(self.mod.config.opacityl3.value)

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_l1_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawl1 = state
        else:
            self.drawl1 = state == Qt.CheckState.Checked
        self.l1.renderedtexture.setOpacity(.9 if self.drawl1 else 0)

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_l2_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawl2 = state
        else:
            self.drawl2 = state == Qt.CheckState.Checked
        self.l2.renderedtexture.setOpacity(.5 if self.drawl2 else 0)

    @Slot(Qt.CheckState)
    @Slot(bool)
    def check_l3_change(self, state: Qt.CheckState | bool):
        if isinstance(state, bool):
            self.drawl3 = state
        else:
            self.drawl3 = state == Qt.CheckState.Checked
        self.l3.renderedtexture.setOpacity(.2 if self.drawl3 else 0)


