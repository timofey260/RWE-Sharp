from RWESharp.Modify import EditorMode
from RWESharp.Configurable import ColorConfigurable
from BaseMod.effects.effectRenderTexture import EffectRenderLevelImage
from PySide6.QtGui import QColor


class EffectEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        self.coloroff = ColorConfigurable(mod, "EDIT_effect.color_off", QColor(210, 37, 219, 100), "No value color")
        self.coloron = ColorConfigurable(mod, "EDIT_effect.color_on", QColor(37, 204, 18, 130), "Full value color")
        self.layer = EffectRenderLevelImage(self, 100, 0).add_myself(self)