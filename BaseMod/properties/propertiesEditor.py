from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderRect, GridHandleRectangle, HandleRectangle
from RWESharp.Configurable import IntConfigurable
from BaseMod.properties.PropertiesHistory import BorderChange, TileSeedChange
from PySide6.QtCore import QPoint, QRect, QRectF

class PropertiesEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.handlerect = GridHandleRectangle(self, QRect(0, 0, 5, 5))
        self.handlerect.recth.rectChanged.connect(self.extratiles_changed)
        self.borderhandlerect = GridHandleRectangle(self, QRect(0, 0, 40, 40))
        self.borderhandlerect.recth.rectChanged.connect(print)

        self.xofs = IntConfigurable(None, "", 0, "X offset")  # none because we don't want to save this
        self.yofs = IntConfigurable(None, "", 0, "Y offset")
        self.width = IntConfigurable(None, "", 0, "Level Width")
        self.height = IntConfigurable(None, "", 0, "Level Height")

        self.left = IntConfigurable(None, "", 0, "Extra tiles left")
        self.top = IntConfigurable(None, "", 0, "Extra tiles top")
        self.right = IntConfigurable(None, "", 0, "Extra tiles right")
        self.bottom = IntConfigurable(None, "", 0, "Extra tiles bottom")

        self.seed = IntConfigurable(None, "", 0, "Tile Seed")
        self.seed.valueChanged.connect(self.seed_changed)

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.reposition()

    def seed_changed(self, seed):
        if self.level.l_info.tile_seed == seed:
            return
        self.level.add_history(TileSeedChange, seed)

    def extratiles_changed(self, rect: QRect):
        newtiles = [max(rect.x(), 0), max(rect.y(), 0), max(self.level.level_width - rect.x() - rect.width(), 0), max(self.level.level_height - rect.y() - rect.height(), 0)]
        self.level.add_history(BorderChange, newtiles)

    def reposition(self):
        self.borderhandlerect.setRect(QRect(0, 0, self.level.level_width, self.level.level_height))
        self.width.update_value_default(self.level.level_width)
        self.height.update_value_default(self.level.level_height)

        self.update_params()
        self.reposition_extra()

    def update_params(self):
        self.seed.update_value_default(self.level.l_info.tile_seed)

    def reposition_extra(self):
        width = self.level.level_width
        height = self.level.level_height

        et = self.level.extra_tiles
        tilerect = QRect(et[0], et[1], width - et[2] - et[0], height - et[3] - et[1])
        self.handlerect.setRect(tilerect)
        self.left.update_value_default(self.level.extra_tiles[0])
        self.top.update_value_default(self.level.extra_tiles[1])
        self.right.update_value_default(self.level.extra_tiles[2])
        self.bottom.update_value_default(self.level.extra_tiles[3])
