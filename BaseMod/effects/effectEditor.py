from RWESharp.Modify import Editor
from RWESharp.Configurable import ColorConfigurable, KeyConfigurable, IntConfigurable
from RWESharp.Renderable import RenderEllipse
from RWESharp.Core import CELLSIZE
from BaseMod.effects.effectRenderTexture import EffectRenderLevelImage
from BaseMod.effects.effectHistory import EffectBrush
from BaseMod.effects.effectExplorer import EffectExplorer
from PySide6.QtGui import QColor, QMoveEvent, QGuiApplication, QAction
from PySide6.QtCore import QRect, QPoint, QSize, Qt


class EffectEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.effectui = None
        self.coloroff = ColorConfigurable(mod, "EDIT_effect.color_off", QColor(210, 37, 219, 100), "No value color")
        self.coloron = ColorConfigurable(mod, "EDIT_effect.color_on", QColor(37, 204, 18, 130), "Full value color")
        self.layer = EffectRenderLevelImage(self, 100, 0)
        self.effectindex = IntConfigurable(None, "EDIT_effect.effectindex", 0, "Current effect")
        self.brushsize = IntConfigurable(mod, "EDIT_effect.brushsize", 4, "Current effect")

        self.brush = RenderEllipse(self, 0, QRect(0, 0, 1, 1))
        self.effectindex.valueChanged.connect(self.select_effect)
        self.lastpos = QPoint()

        self.effect_explorer = EffectExplorer(self, self.manager.window)

    def select_effect(self, index):
        self.effectindex.update_value(index)
        self.layer.change_index(self.effectindex.value)

    def mouse_move_event(self, event: QMoveEvent):
        super().mouse_move_event(event)
        pos = self.viewport.viewport_to_editor(self.mouse_pos)
        self.update_brush()
        if len(self.level.l_effects) == 0:
            return
        if self.mouse_left or self.mouse_right:
            if self.lastpos != pos:
                self.level.last_history_element.add_move(pos)
        self.lastpos = pos

    def update_brush(self):
        pos = self.viewport.viewport_to_editor(self.mouse_pos)
        brushpos = (pos - QPoint(self.brushsize.value, self.brushsize.value)) * CELLSIZE
        rect = QRect(brushpos, QSize(self.brushsize.value * 2, self.brushsize.value * 2) * CELLSIZE)
        if self.brushsize.value % 2 == 0:
            rect.moveTo(brushpos + QPoint(CELLSIZE // 2, CELLSIZE // 2))
        self.brush.setRect(rect)

    def mouse_left_press(self):
        pos = self.viewport.viewport_to_editor(self.mouse_pos)
        if len(self.level.l_effects) == 0:
            return 
        self.level.add_history(EffectBrush, self.effectindex.value, pos, self.brushsize.value, False, self.shift)

    def mouse_right_press(self):
        if self.mouse_left or len(self.level.l_effects) == 0:
            return
        pos = self.viewport.viewport_to_editor(self.mouse_pos)
        self.level.add_history(EffectBrush, self.effectindex.value, pos, self.brushsize.value, True, self.shift)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.effectui.add_effects()
        self.effectui.effect_settings()
