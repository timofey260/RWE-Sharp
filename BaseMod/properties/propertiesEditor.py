from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import QPen, QColor

from BaseMod.properties.PropertiesHistory import BorderChange, TileSeedChange, WaterChange
from RWESharp2.Configurable import IntConfigurable
from RWESharp2.Core import CELLSIZE, wladd
from RWESharp2.Modify import Editor
from RWESharp2.Renderable import Handle, GridHandleRectangle


class PropertiesEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.handlerect = GridHandleRectangle(self, QRect(0, 0, 5, 5))
        self.handlerect.visrect.setPen(QPen(QColor(0, 0, 255), 10, Qt.PenStyle.DashLine))
        self.handlerect.recth.rectChanged.connect(self.extratiles_changed)
        self.borderhandlerect = GridHandleRectangle(self, QRect(0, 0, 40, 40))
        self.borderhandlerect.visrect.setPen(QPen(QColor(255, 0, 0), 10, Qt.PenStyle.DashLine))
        self.borderhandlerect.recth.rectChanged.connect(self.border_changed)

        self.xofs = IntConfigurable(None, "", 0, "X offset")  # none because we don't want to save this
        self.yofs = IntConfigurable(None, "", 0, "Y offset")
        self.width = IntConfigurable(None, "", 0, "Level Width")
        self.height = IntConfigurable(None, "", 0, "Level Height")

        self.left = IntConfigurable(None, "", 0, "Extra tiles left")
        self.top = IntConfigurable(None, "", 0, "Extra tiles top")
        self.right = IntConfigurable(None, "", 0, "Extra tiles right")
        self.bottom = IntConfigurable(None, "", 0, "Extra tiles bottom")
        self.left.valueChanged.connect(self.change_extratiles_manually)
        self.top.valueChanged.connect(self.change_extratiles_manually)
        self.right.valueChanged.connect(self.change_extratiles_manually)
        self.bottom.valueChanged.connect(self.change_extratiles_manually)

        self.waterlevelhandle = Handle(self)
        self.waterlevelhandle.mouseReleased.connect(self.waterhandle_moved)

        self.waterheight = IntConfigurable(None, "", 0, "Water Height")
        self.watertype = IntConfigurable(None, "", 0, "Water Type")
        self.waterheight.valueChanged.connect(self.water_changed)
        self.watertype.valueChanged.connect(self.water_changed)

        self.seed = IntConfigurable(None, "", 0, "Tile Seed")
        self.seed.valueChanged.connect(self.seed_changed)
        self.changing_extra = False
        self.changing_water = False

    def init_scene_items(self, viewport):
        super().init_scene_items(viewport)
        self.reposition()

    def seed_changed(self, seed):
        if self.level.l_info.tile_seed == seed:
            return
        self.level.add_history(TileSeedChange, seed)

    def waterhandle_moved(self):
        if self.changing_water:
            return
        newlevel = int(self.level.level_height - (self.waterlevelhandle.offset.y() / CELLSIZE) - wladd)
        self.waterheight.update_value(newlevel)

    def water_changed(self):
        if self.changing_water:
            return
        state = max(0, self.watertype.value - 1)
        level = -1 if self.watertype.value == 0 else max(0, self.waterheight.value)
        if state == self.level.l_info.water_in_front and level == self.level.l_info.water_level:
            return
        self.level.add_history(WaterChange, level, state)

    def change_extratiles_manually(self):
        if self.changing_extra:
            return
        newrect = QRect(self.left.value, self.top.value, self.level.level_width - self.left.value - self.right.value, self.level.level_height - self.top.value - self.bottom.value)
        self.handlerect.setRect(newrect)
        self.extratiles_changed()

    def extratiles_changed(self):
        rect = self.handlerect.getrect
        newtiles = [max(rect.x(), 0), max(rect.y(), 0), max(self.level.level_width - rect.x() - rect.width(), 0), max(self.level.level_height - rect.y() - rect.height(), 0)]
        if self.level.extra_tiles == newtiles:
            return
        self.level.add_history(BorderChange, newtiles)

    def confirm_resize(self):
        if self.borderhandlerect.getrect == QRect(0, 0, self.level.level_width, self.level.level_height):
            return
        self.level.level_resized(self.borderhandlerect.getrect)
        self.reposition()

    def border_changed(self):
        rect = self.borderhandlerect.getrect
        self.xofs.update_value(rect.x())
        self.yofs.update_value(rect.y())
        self.width.update_value(rect.width())
        self.height.update_value(rect.height())

    def reposition(self):
        self.borderhandlerect.setRect(QRect(0, 0, self.level.level_width, self.level.level_height))
        self.width.update_value_default(self.level.level_width)
        self.height.update_value_default(self.level.level_height)
        self.xofs.update_value(0)
        self.yofs.update_value(0)

        self.update_params()
        self.reposition_extra()

    def update_params(self):
        self.seed.update_value_default(self.level.l_info.tile_seed)
        self.changing_water = True
        self.waterheight.update_value_default(self.level.l_info.water_level)
        self.watertype.update_value_default(0 if self.level.l_info.water_level == -1 else self.level.l_info.water_in_front + 1)
        self.waterlevelhandle.handle.setEnabled(self.watertype.value > 0)
        self.waterlevelhandle.setOpacity(1 if self.watertype.value > 0 else 0)
        top = self.level.level_height * CELLSIZE - (wladd + self.level.l_info.water_level) * CELLSIZE
        self.waterlevelhandle.setPos(QPoint(0, top))
        self.changing_water = False

    def reposition_extra(self):
        width = self.level.level_width
        height = self.level.level_height

        et = self.level.extra_tiles
        tilerect = QRect(et[0], et[1], width - et[2] - et[0], height - et[3] - et[1])
        self.handlerect.setRect(tilerect)

        self.changing_extra = True
        self.left.update_value_default(self.level.extra_tiles[0])
        self.top.update_value_default(self.level.extra_tiles[1])
        self.right.update_value_default(self.level.extra_tiles[2])
        self.bottom.update_value_default(self.level.extra_tiles[3])
        self.changing_extra = False

    def level_resized(self, newrect: QRect):
        super().level_resized(newrect)
        self.reposition()
