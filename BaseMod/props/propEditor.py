import math

from RWESharp.Modify import Editor
from RWESharp.Core import CELLSIZE, SPRITESIZE
from RWESharp.Configurable import ColorConfigurable
from RWESharp.Loaders import Prop
from RWESharp.Core import lingoIO
from RWESharp.Renderable import RenderLine, RenderPoly, RenderRect
from RWESharp.Utils import rotate_point

from BaseMod.props.propExplorer import PropExplorer
from BaseMod.props.propRenderable import PropRenderable
from BaseMod.props.propHistory import PropPlace, PropRemove
from BaseMod.props.propUtils import find_mid
from BaseMod.props.RopePhysics import RopeModel
from BaseMod.LevelParts import PropLevelPart

from PySide6.QtCore import QPointF, QLineF, Qt, QRect, QPoint, QTimer
from PySide6.QtGui import QPolygonF, QColor, QPen

import random as rnd


class PropEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.props = self.manager.props
        self.propsui = None
        self.explorer = PropExplorer(self, self.manager.window)
        self.prop: Prop = self.props.find_prop("loopantennafront")
        self.placingprop = PropRenderable(self, self.prop)
        self.depth = 0
        self.notes = []
        self.setprop([self.props.find_prop("CogA1")])
        self.prop_settings = {"renderorder": 0, "seed": rnd.randint(0, 1000), "renderTime": 0}
        self.editingprop = False
        self.cursor_color = ColorConfigurable(mod, "EDIT_prop.cursor_color", QColor(Qt.GlobalColor.red))
        self.select_color = ColorConfigurable(mod, "EDIT_prop.select_color", QColor(Qt.GlobalColor.green))
        self.debugline = RenderLine(self, 0, QLineF())
        self.selectrect = RenderRect(self, 0, QRect(), QPen(Qt.GlobalColor.white, 3, Qt.PenStyle.DashLine))
        self.debugpoly = RenderPoly(self, 0, QPolygonF())
        self.cursor_color.valueChanged.connect(self.debugline.drawline.setPen)
        self.cursor_color.valueChanged.connect(self.debugpoly.drawpoly.setPen)
        self.selected = []
        self.selected_poly: list[RenderPoly] = []
        self.selectpoint = QPoint()

        self.prop_simulation: RopeModel = None
        self.updatetimer = QTimer()
        self.updatetimer.setInterval(3.333333333)
        self.updatetimer.timeout.connect(self.update_rope)
        self.updatetimer.start()

    def update_rope(self):
        if not self.prop.rope or self.prop_simulation is None or self.viewport is None:
            return
        #middle = (self.placingprop.transform[0] + self.placingprop.transform[1] + self.placingprop.transform[2] + self.placingprop.transform[3]) * (1 / 4)
        ropepos = self.viewport.viewport_to_editor_float(self.mouse_pos.toPointF()) * CELLSIZE
        pA = (self.placingprop.transform[0] + self.placingprop.transform[3]) * .5 + ropepos
        pB = (self.placingprop.transform[1] + self.placingprop.transform[2]) * .5 + ropepos
        self.prop_simulation.posA = pA
        self.prop_simulation.posB = pB
        self.prop_simulation.modelRopeUpdate() # todo disable rope colission
        self.placingprop.rope_segments = [i["pos"] - ropepos for i in self.prop_simulation.segments]
        self.placingprop.retransform()

    def setprop(self, props: list[Prop]):
        if len(props) > 0:
            self.prop = props[0]
        self.placingprop.setprop(self.prop)
        self.apply_settings()
        if self.propsui is not None:
            self.propsui.display_settings()
        self.reset_transform()
        self.placingprop.set_variation(self.prop_settings.get("variation", 1))
        self.apply_tags()
        if self.prop.rope:
            self.create_rope_simulation()

    def create_rope_simulation(self):
        if self.prop.rope:
            ropepos = self.editor_pos
            pA = (self.placingprop.transform[0] + self.placingprop.transform[3]) * .5 + ropepos
            pB = (self.placingprop.transform[1] + self.placingprop.transform[2]) * .5 + ropepos
            collDep = ((self.layer - 1) * 10) + self.depth + self.prop["collisionDepth"]
            if collDep < 10:
                cd = 0
            elif collDep < 20:
                cd = 1
            else:
                cd = 2
            if self.prop.images[0].height() == 0:
                fac = 0
            else:
                fac = math.dist(self.placingprop.transform[0].toTuple(), self.placingprop.transform[3].toTuple()) / self.prop.images[0].height()
            self.prop_simulation = RopeModel(self.level.l_geo, pA, pB, self.prop, fac, cd, self.prop_settings["release"])
            self.placingprop.create_rope_graphics_from_model(self.prop_simulation)

    def apply_tags(self):
        tags = self.prop.tags
        for tag in tags:
            match tag:
                case "randomRotat":
                    self.rotate(rnd.randint(0, 360))
                case "randomFlipX":
                    self.flipx() if rnd.choice([True, False]) else False
                case "randomFlipY":
                    self.flipy() if rnd.choice([True, False]) else False

    def flipx(self):
        self.transform[0].setX(-self.transform[0].x())
        self.transform[1].setX(-self.transform[1].x())
        self.transform[2].setX(-self.transform[2].x())
        self.transform[3].setX(-self.transform[3].x())
        self.create_rope_simulation()
        self.placingprop.move_event()

    def flipy(self):
        self.transform[0].setY(-self.transform[0].y())
        self.transform[1].setY(-self.transform[1].y())
        self.transform[2].setY(-self.transform[2].y())
        self.transform[3].setY(-self.transform[3].y())
        self.create_rope_simulation()
        self.placingprop.move_event()

    def rotate(self, rot):
        newtransform = []
        for t in self.transform:
            newtransform.append(rotate_point(t, rot))
        self.placingprop.transform = newtransform
        self.create_rope_simulation()
        self.placingprop.move_event()

    def move_event(self):
        super().move_event()
        self.manager.set_status(f"{self.editor_pos.x()}, {self.editor_pos.y()} | {self.prop_settings.get('variation', 0)}, {self.prop.vars}")
        if not self.editingprop:
            self.placingprop.setPos(self.viewport.viewport_to_editor_float(self.mouse_pos.toPointF()) * CELLSIZE)
        self.debugline.drawline.setOpacity(0)
        self.debugpoly.drawpoly.setOpacity(0)
        if self.control and self.selectpoint != QPoint(0, 0):
            rect = QRect.span(self.selectpoint, self.editor_pos)
            self.selectrect.setRect(rect)
            self.selectrect.drawrect.setOpacity(1)
            self.reset_selection()
            for i, prop in enumerate(self.level.l_props):
                for p in prop.quad:
                    if rect.contains(p.toPoint()):
                        self.selected.append(i)
                        poly = RenderPoly(self, 0, QPolygonF(prop.quad), self.select_color.value)
                        self.selected_poly.append(poly)
                        #poly.init_graphics(self.viewport)
                        break
            return
        if self.shift and len(self.level.l_props) > 0:
            self.debugline.drawline.setOpacity(1)
            self.debugpoly.drawpoly.setOpacity(1)
            closest = self.level.l_props[self.find_nearest(self.editor_pos)]
            self.debugline.setLine(QLineF(self.editor_pos, find_mid(closest)))
            self.debugpoly.setPoly(QPolygonF(closest.quad))

    def mouse_left_press(self):
        if self.control:
            self.selectpoint = self.editor_pos
            self.reset_selection()
            return
        if not self.shift:
            self.place()
            return
        if len(self.level.l_props) == 0:
            return
        closest = self.find_nearest(self.editor_pos)
        self.level.add_history(PropRemove, closest)

    def mouse_right_press(self):
        self.variationadd()

    def variationadd(self):
        if self.prop_settings.get("variation") is not None:
            self.prop_settings["variation"] = (self.prop_settings["variation"] + 1) % (self.prop.vars + 1)
            self.placingprop.set_variation(self.prop_settings["variation"])
            self.propsui.display_settings()

    def reset_selection(self):
        for i in self.selected_poly:
            i.remove_myself()
        self.selected_poly = []
        self.selected = []

    def mouse_left_release(self):
        self.selectpoint = QPoint(0, 0)
        self.selectrect.drawrect.setOpacity(0)

    def free_transform(self):
        if self.editingprop:
            self.editingprop = False
            self.placingprop.delete_handlers()
            self.viewport.clean()
            self.create_rope_simulation()
            return
        self.editingprop = True
        self.placingprop.free_transform()
        self.viewport.clean()

    def find_nearest(self, pos: QPointF):
        closesti = -1
        closest = 99999
        for i, v in enumerate(self.level.l_props):
            p = (find_mid(v) - pos).manhattanLength()
            if p < closest:
                closest = p
                closesti = i
        return closesti

    def reset_transform(self):
        w, h, = self.prop.size.width() / 2, self.prop.size.height() / 2
        self.transform = [QPointF(-w, -h), QPointF(w, -h), QPointF(w, h), QPointF(-w, h)]
        self.placingprop.move_event()

    @property
    def transform(self) -> [QPointF, QPointF, QPointF, QPointF]:
        return self.placingprop.transform

    @transform.setter
    def transform(self, value: [QPointF, QPointF, QPointF, QPointF]):
        self.placingprop.transform = value

    def apply_settings(self):
        self.prop_settings = {"renderorder": 0, "seed": rnd.randint(0, 1000), "renderTime": 0}
        random = self.prop["random"] if self.prop.get("random") is not None else 1
        notes = self.prop.notes.copy()
        if self.prop.type in ["standard", "variedStandard"]:
                if self.prop.colorTreatment == "bevel":
                    notes.append("The highlights and shadows on this prop are generated by code,\nso it can be rotated to any degree and they will remain correct.\n")
                else:
                    notes.append("Be aware that shadows and highlights will not rotate with the prop,\nso extreme rotations may cause incorrect shading.\n")
                if self.prop.type == "variedStandard":
                    self.prop_settings["variation"] = 0 if random else 1

                if random:
                    notes.append("Will put down a random variation.\nA specific variation can be selected from settings.\n")
                else:
                    notes.append("This prop comes with many variations.\nWhich variation can be selected from settings.\n")
        elif self.prop.type == "rope":
                self.prop_settings["release"] = 0
        elif self.prop.type in ["variedDecal", "variedSoft"]:
            self.prop_settings["variation"] = 0 if random else 1
            self.prop_settings["customDepth"] = self.prop.get("depth")
            if self.prop.type == "variedSoft" and self.prop.get("colorize"):
                self.prop_settings["applyColor"] = 1
                notes.append("It's recommended to render this prop after the effects\nif the color is activated, as the effects won't affect the color layers.\n")
        elif self.prop.type in ["simpleDecal", "soft", "softEffect", "antimatter"]:
            self.prop_settings["customDepth"] = self.prop["depth"]

        if self.prop.type in ["soft", "softEffect", "variedSoft"]:
            if self.prop.get("selfShade") == 1:
                notes.append("The highlights and shadows on this prop are generated by code,\nso it can be rotated to any degree and they will remain correct.\n")
            else:
                notes.append("Be aware that shadows and highlights will not rotate with the prop,\nso extreme rotations may cause incorrect shading.\n")
        if self.prop.name.lower() in ["wire", "zero-g wire"]:
            self.prop_settings["thickness"] = 2
            notes.append("The thickness of the wire can be set in settings.\n")
        elif self.prop.name.lower() in ["zero-g tube"]:
            self.prop_settings["applyColor"] = 0
            notes.append("The tube can be colored white through the settings.\n")
        for tag in self.prop.tags:
            match tag:
                case "customColor":
                    self.prop_settings["color"] = 0
                    notes.append("Custom color available\n")
                case "customColorRainBow":
                    self.prop_settings["color"] = 1
                    notes.append("Custom color available\n")
        newnotes = []
        for note in self.notes:
            if note in newnotes:
                pass
            else:
                newnotes.append(note)
        self.notes = notes

    def place(self):
        quads = [i + self.placingprop.offset for i in self.transform]
        settings = {"settings": self.prop_settings.copy()}
        if self.prop.rope:
            ropepos = self.viewport.viewport_to_editor_float(self.mouse_pos.toPointF()) * CELLSIZE
            settings["points"] = [lingoIO.point((i + ropepos).toTuple()) for i in self.placingprop.rope_segments]
        prop = PropLevelPart.PlacedProp(self.prop, -self.depth, quads, settings)
        self.level.add_history(PropPlace, prop)
