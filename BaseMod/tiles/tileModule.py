from PySide6.QtCore import Slot
from PySide6.QtGui import QImage, QColor

from BaseMod.tiles.tileRenderTexture import TileRenderLevelImage
from RWESharp.Modify import Module


class TileModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.ui = self.mod.tileview
        self.l1 = TileRenderLevelImage(self, 100, 0)
        self.l2 = TileRenderLevelImage(self, 200, 1)
        self.l3 = TileRenderLevelImage(self, 300, 2)

        self.ui.drawprendered.valueChanged.connect(self.check_layers_change)
        self.ui.drawpnotrendered.valueChanged.connect(self.check_layers_change)
        self.ui.drawsrendered.valueChanged.connect(self.check_layers_change)
        self.ui.drawsnotrendered.valueChanged.connect(self.check_layers_change)
        self.ui.renderall.valueChanged.connect(self.check_layers_change)

        self.ui.drawl1.valueChanged.connect(self.check_layers_change)
        self.ui.drawl2.valueChanged.connect(self.check_layers_change)
        self.ui.drawl3.valueChanged.connect(self.check_layers_change)

        self.ui.drawoption.valueChanged.connect(self.redraw_option)
        self.ui.render.connect(self.render_module)
        self.ui.matborder.valueChanged.connect(self.change_border)
        self.manager.layer.valueChanged.connect(self.check_layers_change)

    def change_border(self, enabled):
        self.l1.change_material_border(enabled)
        self.l2.change_material_border(enabled)
        self.l3.change_material_border(enabled)

    def redraw_option(self):
        self.render_module(True)

    def init_module_textures(self):
        self.check_layers_change()

    @Slot()
    def check_layers_change(self):
        if self.ui.drawoption.value > 2:
            self.l1.setOpacity(self.ui.drawprendered.value if self.layer == 0 else self.ui.drawsrendered.value)
            self.l2.setOpacity(self.ui.drawprendered.value if self.layer == 1 else self.ui.drawsrendered.value)
            self.l3.setOpacity(self.ui.drawprendered.value if self.layer == 2 else self.ui.drawsrendered.value)
            return
        self.l1.setOpacity(self.ui.drawpnotrendered.value if self.layer == 0 else self.ui.drawsnotrendered.value)
        if self.layer == 1 and not self.ui.renderall.value:
            self.l1.setOpacity(0)
        self.l2.setOpacity(self.ui.drawpnotrendered.value if self.layer == 1 else self.ui.drawsnotrendered.value)
        if self.layer == 2 and not self.ui.renderall.value:
            self.l1.setOpacity(0)
            self.l2.setOpacity(0)
        self.l3.setOpacity(self.ui.drawpnotrendered.value if self.layer == 2 else self.ui.drawsnotrendered.value)

    def render_module(self, clear=False):
        self.l1.draw_layer(clear)
        self.l2.draw_layer(clear)
        self.l3.draw_layer(clear)
        self.init_module_textures()
        if self.ui.drawoption.value == 6:
            self.mod.gridui.backgroundcolor.update_value(self.ui.colortable[4])
            # self.mod.gridmodule.rect.drawrect.setBrush(self.ui.colortable[4])
        elif self.ui.drawoption.value in [4, 5]:
            self.mod.gridui.backgroundcolor.update_value(self.ui.colortable[3])
            # self.mod.gridmodule.rect.drawrect.setBrush(self.ui.colortable[3])

        elif self.ui.drawoption.value == 3:
            self.mod.gridui.backgroundcolor.update_value(QColor(255, 255, 255))
            # self.mod.gridmodule.rect.drawrect.setBrush(QColor(255, 255, 255))

        else:
            self.mod.gridui.backgroundcolor.update_value(self.mod.gridui.backgroundcolor.default)
            # self.mod.gridmodule.rect.drawrect.setBrush(self.mod.gridmodule.backgroundcolor.value)

    def get_layer(self, layer: int) -> TileRenderLevelImage:
        return [self.l1, self.l2, self.l3][layer]

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.render_module()

