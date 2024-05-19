from core.Modify.baseModule import Module
from BaseMod.tiles.tileRenderTexture import TileRenderTexture

class TileModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.l1 = TileRenderTexture(self, 0)
        self.l2 = TileRenderTexture(self, 1)
        self.l3 = TileRenderTexture(self, 2)
        self.editorlayers.append((150, self.l3))
        self.editorlayers.append((250, self.l2))
        self.editorlayers.append((350, self.l1))

    def init_module_textures(self):
        self.l1.renderedtexture.setOpacity(.9)
        self.l2.renderedtexture.setOpacity(.5)
        self.l3.renderedtexture.setOpacity(.2)