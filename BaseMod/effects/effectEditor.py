from RWESharp.Modify import EditorMode
from RWESharp.Configurable import ColorConfigurable, KeyConfigurable
from RWESharp.Renderable import RenderEllipse
from BaseMod.effects.effectRenderTexture import EffectRenderLevelImage
from PySide6.QtGui import QColor
from PySide6.QtCore import QRect


class EffectEditor(EditorMode):
    def __init__(self, mod):
        super().__init__(mod)
        self.coloroff = ColorConfigurable(mod, "EDIT_effect.color_off", QColor(210, 37, 219, 100), "No value color")
        self.coloron = ColorConfigurable(mod, "EDIT_effect.color_on", QColor(37, 204, 18, 130), "Full value color")
        self.layer = EffectRenderLevelImage(self, 100, 0).add_myself(self)

        self.effectup = KeyConfigurable(mod, "EDIT_effect.effectup", "w", "Previous effect")
        self.effectdown = KeyConfigurable(mod, "EDIT_effect.effectdown", "s", "Next effect")
        self.effectmoveup = KeyConfigurable(mod, "EDIT_effect.effectmoveup", "Shift+w", "Move effect back")
        self.effectmovedown = KeyConfigurable(mod, "EDIT_effect.effectmovedown", "Shift+s", "Move effect forward")
        self.duplicate = KeyConfigurable(mod, "EDIT_effect.duplicate", "Ctrl+d", "Duplicate effect")
        self.delete = KeyConfigurable(mod, "EDIT_effect.delete", "Delete", "Delete effect")

        self.brush = RenderEllipse(mod, 0, QRect(0, 0, 1, 1))

    def select_effect(self, index):
        self.layer.change_index(index)
