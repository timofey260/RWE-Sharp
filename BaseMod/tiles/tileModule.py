import os.path

from PySide6.QtCore import Slot
from PySide6.QtGui import QImage, QColor

from BaseMod.tiles.tileRenderTexture import TileRenderLevelImage
from RWESharp.Configurable import BoolConfigurable, IntConfigurable, StringConfigurable, FloatConfigurable
from RWESharp.Core import PATH_FILES_IMAGES_PALETTES
from RWESharp.Loaders import palette_to_colortable
from RWESharp.Modify import Module


class TileModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        from BaseMod.baseMod import BaseMod
        self.mod: BaseMod
        self.drawtiles = BoolConfigurable(mod, "VIEW_tile.drawtiles", True, "Draw tiles")
        self.drawl1 = BoolConfigurable(mod, "VIEW_tile.drawl1", True, "Draw layer 1")
        self.drawl2 = BoolConfigurable(mod, "VIEW_tile.drawl2", True, "Draw layer 2")
        self.drawl3 = BoolConfigurable(mod, "VIEW_tile.drawl3", True, "Draw layer 3")
        self.drawlheads = BoolConfigurable(mod, "VIEW_tile.drawlheads", True, "Draw tile heads")
        self.drawlmats = BoolConfigurable(mod, "VIEW_tile.drawlmats", True, "Draw materials")

        self.drawoption = IntConfigurable(mod, "VIEW_tile.drawoption", 0, "Option how to draw tiles")
        self.palettepath = StringConfigurable(mod, "VIEW_tile.palettepath",
                                              os.path.join(PATH_FILES_IMAGES_PALETTES, "palette0.png"),
                                              "Path to palettes")

        self.drawl1notrendered = FloatConfigurable(mod, "VIEW_tile.drawl1notrend", .9, "Layer 1 draw opacity(classic and henry)")
        self.drawl2notrendered = FloatConfigurable(mod, "VIEW_tile.drawl2notrend", .5, "Layer 2 draw opacity(classic and henry)")
        self.drawl3notrendered = FloatConfigurable(mod, "VIEW_tile.drawl3notrend", .2, "Layer 3 draw opacity(classic and henry)")

        self.drawl1rendered = FloatConfigurable(mod, "VIEW_tile.drawl1rend", 1, "Layer 1 draw opacity(rendered)")
        self.drawl2rendered = FloatConfigurable(mod, "VIEW_tile.drawl2rend", 1, "Layer 2 draw opacity(rendered)")
        self.drawl3rendered = FloatConfigurable(mod, "VIEW_tile.drawl3rend", 1, "Layer 3 draw opacity(rendered)")

        self.opacityshift = BoolConfigurable(mod, "VIEW_tile.opacityShift", True,
                                             "Does not change opacity of hidden layers")

        if not os.path.exists(self.palettepath.value):
            self.palettepath.reset_value()
        self.palettepath.valueChanged.connect(self.change_colortable)
        self.colortable = None
        self.l1 = TileRenderLevelImage(self, 100, 0).add_myself(self)
        self.l2 = TileRenderLevelImage(self, 200, 1).add_myself(self)
        self.l3 = TileRenderLevelImage(self, 300, 2).add_myself(self)

        self.drawl1.valueChanged.connect(self.check_l1_change)
        self.drawl1rendered.valueChanged.connect(self.check_l1_change)
        self.drawl1notrendered.valueChanged.connect(self.check_l1_change)
        self.drawl2.valueChanged.connect(self.check_l2_change)
        self.drawl2rendered.valueChanged.connect(self.check_l2_change)
        self.drawl2notrendered.valueChanged.connect(self.check_l2_change)
        self.drawl3.valueChanged.connect(self.check_l3_change)
        self.drawl3rendered.valueChanged.connect(self.check_l3_change)
        self.drawl3notrendered.valueChanged.connect(self.check_l3_change)

        self.drawoption.valueChanged.connect(self.redraw_option)
        self.drawtiles.valueChanged.connect(self.hide_tiles)
        self.change_colortable()

    @Slot()
    def hide_tiles(self):
        self.drawl1.update_value(self.drawtiles.value)
        self.drawl2.update_value(self.drawtiles.value)
        self.drawl3.update_value(self.drawtiles.value)

    @Slot()
    def change_colortable(self):
        self.colortable = palette_to_colortable(QImage(self.palettepath.value))

    @Slot()
    def redraw_option(self):
        self.render_module(True)

    def init_module_textures(self):
        self.check_l1_change()
        self.check_l2_change()
        self.check_l3_change()

    @Slot()
    def check_l1_change(self):
        if not self.drawtiles.value:
            return
        if self.opacityshift.value:
            self.check_l2_change()
        opacityl1 = self.drawl1rendered.value if self.drawoption.value > 2 else self.drawl1notrendered.value
        self.l1.renderedtexture.setOpacity(opacityl1 if self.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if not self.drawtiles.value:
            return
        if self.opacityshift.value:
            self.check_l3_change()
        opacityl1 = self.drawl1rendered.value if self.drawoption.value > 2 else self.drawl1notrendered.value
        opacityl2 = self.drawl2rendered.value if self.drawoption.value > 2 else self.drawl2notrendered.value
        if self.opacityshift.value and self.drawl2.value:
            opval = opacityl1 if not self.drawl1.value else opacityl2
        else:
            opval = opacityl2 if self.drawl2.value else 0
        self.l2.renderedtexture.setOpacity(opval)

    @Slot()
    def check_l3_change(self):
        if not self.drawtiles.value:
            return
        opacityl1 = self.drawl1rendered.value if self.drawoption.value > 2 else self.drawl1notrendered.value
        opacityl2 = self.drawl2rendered.value if self.drawoption.value > 2 else self.drawl2notrendered.value
        opacityl3 = self.drawl3rendered.value if self.drawoption.value > 2 else self.drawl3notrendered.value
        if self.opacityshift.value and self.drawl3.value:
            opval = opacityl1 if not self.drawl1.value and not self.drawl2.value else \
                opacityl2 if not self.drawl2.value or not self.drawl1.value else opacityl3
        else:
            opval = opacityl3 if self.drawl3.value else 0
        self.l3.renderedtexture.setOpacity(opval)

    def render_module(self, clear=False):
        self.l1.draw_layer(clear)
        self.l2.draw_layer(clear)
        self.l3.draw_layer(clear)
        self.init_module_textures()
        if self.drawoption.value == 6:
            self.mod.gridmodule.rect.drawrect.setBrush(self.colortable[4])
        elif self.drawoption.value in [4, 5]:
            self.mod.gridmodule.rect.drawrect.setBrush(self.colortable[3])
        elif self.drawoption.value == 3:
            self.mod.gridmodule.rect.drawrect.setBrush(QColor(255, 255, 255))
        else:
            self.mod.gridmodule.rect.drawrect.setBrush(self.mod.gridmodule.backgroundcolor.value)

    def showlayer(self, currentlayer):
        self.drawl1.update_value(currentlayer == 0)
        self.drawl2.update_value(currentlayer <= 1)
        self.drawl3.update_value(True)

    def get_layer(self, layer: int) -> TileRenderLevelImage:
        return [self.l1, self.l2, self.l3][layer]

