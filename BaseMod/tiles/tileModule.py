import os.path
from BaseMod.tiles.tileRenderTexture import TileRenderTexture
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QImage, QColor
from RWESharp.Modify import Module
from RWESharp.Loaders import palette_to_colortable
from RWESharp.Configurable import KeyConfigurable, BoolConfigurable, IntConfigurable, StringConfigurable, FloatConfigurable
from RWESharp.Core import PATH_FILES_IMAGES_PALETTES


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

        self.drawltiles_key = KeyConfigurable(mod, "VIEW_tile.drawltiles_key", "Alt+t", "Hide tiles")
        self.drawl1_key = KeyConfigurable(mod, "VIEW_tile.drawl1_key", "Alt+Shift+1", "layer 1 key")
        self.drawl2_key = KeyConfigurable(mod, "VIEW_tile.drawl2_key", "Alt+Shift+2", "layer 2 key")
        self.drawl3_key = KeyConfigurable(mod, "VIEW_tile.drawl3_key", "Alt+Shift+3", "layer 3 key")

        if not os.path.exists(self.palettepath.value):
            self.palettepath.reset_value()
        self.palettepath.valueChanged.connect(self.change_colortable)
        self.colortable = None
        self.l1 = TileRenderTexture(self, 100, 0).add_myself()
        self.l2 = TileRenderTexture(self, 200, 1).add_myself()
        self.l3 = TileRenderTexture(self, 300, 2).add_myself()

        self.drawl1.valueChanged.connect(self.check_l1_change)
        self.drawl2.valueChanged.connect(self.check_l2_change)
        self.drawl3.valueChanged.connect(self.check_l3_change)
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
        if self.drawoption.value > 2:
            self.l1.renderedtexture.setOpacity(self.drawl1rendered.value if self.drawl1.value else 0)
            return
        self.l1.renderedtexture.setOpacity(self.drawl1notrendered.value if self.drawl1.value else 0)

    @Slot()
    def check_l2_change(self):
        if self.drawoption.value > 2:
            self.l2.renderedtexture.setOpacity(self.drawl2rendered.value if self.drawl2.value else 0)
            return
        self.l2.renderedtexture.setOpacity(self.drawl2notrendered.value if self.drawl2.value else 0)

    @Slot()
    def check_l3_change(self):
        if self.drawoption.value > 2:
            self.l3.renderedtexture.setOpacity(self.drawl3rendered.value if self.drawl3.value else 0)
            return
        self.l3.renderedtexture.setOpacity(self.drawl3notrendered.value if self.drawl3.value else 0)

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

    def get_layer(self, layer: int) -> TileRenderTexture:
        return [self.l1, self.l2, self.l3][layer]

