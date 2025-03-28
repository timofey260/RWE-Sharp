import os.path

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

        self.ui.drawl1.valueChanged.connect(self.check_l1_change)
        self.ui.drawl1rendered.valueChanged.connect(self.check_l1_change)
        self.ui.drawl1notrendered.valueChanged.connect(self.check_l1_change)
        self.ui.drawl2.valueChanged.connect(self.check_l2_change)
        self.ui.drawl2rendered.valueChanged.connect(self.check_l2_change)
        self.ui.drawl2notrendered.valueChanged.connect(self.check_l2_change)
        self.ui.drawl3.valueChanged.connect(self.check_l3_change)
        self.ui.drawl3rendered.valueChanged.connect(self.check_l3_change)
        self.ui.drawl3notrendered.valueChanged.connect(self.check_l3_change)

        self.ui.drawoption.valueChanged.connect(self.redraw_option)
        self.ui.render.connect(self.render_module)
        self.ui.matborder.valueChanged.connect(self.change_border)

    def change_border(self, enabled):
        self.l1.change_material_border(enabled)
        self.l2.change_material_border(enabled)
        self.l3.change_material_border(enabled)

    def redraw_option(self):
        self.render_module(True)

    def init_module_textures(self):
        self.check_l1_change()
        self.check_l2_change()
        self.check_l3_change()

    def check_l1_change(self):
        if not self.ui.drawtiles.value:
            self.l1.renderedtexture.setOpacity(0)
            return
        if self.ui.opacityshift.value:
            self.check_l2_change()
        opacityl1 = self.ui.drawl1rendered.value if self.ui.drawoption.value > 2 else self.ui.drawl1notrendered.value
        self.l1.renderedtexture.setOpacity(opacityl1 if self.ui.drawl1.value else 0)

    def check_l2_change(self):
        if not self.ui.drawtiles.value:
            self.l2.renderedtexture.setOpacity(0)
            return
        if self.ui.opacityshift.value:
            self.check_l3_change()
        opacityl1 = self.ui.drawl1rendered.value if self.ui.drawoption.value > 2 else self.ui.drawl1notrendered.value
        opacityl2 = self.ui.drawl2rendered.value if self.ui.drawoption.value > 2 else self.ui.drawl2notrendered.value
        if self.ui.opacityshift.value and self.ui.drawl2.value:
            opval = opacityl1 if not self.ui.drawl1.value else opacityl2
        else:
            opval = opacityl2 if self.ui.drawl2.value else 0
        self.l2.renderedtexture.setOpacity(opval)

    def check_l3_change(self):
        if not self.ui.drawtiles.value:
            self.l3.renderedtexture.setOpacity(0)
            return
        opacityl1 = self.ui.drawl1rendered.value if self.ui.drawoption.value > 2 else self.ui.drawl1notrendered.value
        opacityl2 = self.ui.drawl2rendered.value if self.ui.drawoption.value > 2 else self.ui.drawl2notrendered.value
        opacityl3 = self.ui.drawl3rendered.value if self.ui.drawoption.value > 2 else self.ui.drawl3notrendered.value
        if self.ui.opacityshift.value and self.ui.drawl3.value:
            opval = opacityl1 if not self.ui.drawl1.value and not self.ui.drawl2.value else \
                opacityl2 if not self.ui.drawl2.value or not self.ui.drawl1.value else opacityl3
        else:
            opval = opacityl3 if self.ui.drawl3.value else 0
        self.l3.renderedtexture.setOpacity(opval)

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

