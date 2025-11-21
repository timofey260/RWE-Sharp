from RWS.Modify import Module
from BaseMod.effects.effectRenderTexture import EffectRenderLevelImage


class EffectsModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.texture = EffectRenderLevelImage(self, 100, 0)
        self.coloron = self.mod.effectview.coloron
        self.coloroff = self.mod.effectview.coloroff

    def redraw(self):
        self.texture.renderedtexture.setOpacity(1 if self.basemod.effectview.showadditional.value else 0)
        self.texture.draw_layer()

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.redraw()

