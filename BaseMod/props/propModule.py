from RWESharp.Modify import Module
from BaseMod.props.propRenderable import PropRenderable
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsItemGroup
from PySide6.QtGui import QPixmap


class PropModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.props: list[PropRenderable] = []
        mod.propsview.ui.ShowProps.toggled.connect(self.set_visibility)
        mod.propsview.ui.Outline.toggled.connect(lambda x: self.set_outline(x, mod.propsview.outline_color.value))
        mod.propsview.ui.OutlineColor.colorPicked.connect(lambda x: self.set_outline(True, x))
        # self.group = QGraphicsItemGroup()
        # prop = QPixmap.fromImage(self.manager.props.find_prop("Big Brick").images[0])
        # for x in range(0, 5000, 50):
        #     for y in range(0, 5000, 50):
        #         item = QGraphicsPixmapItem(prop)
        #         item.setPos(x, y)
        #         self.group.addToGroup(item)
        # Handle(self)

    def move_event(self):
        super().move_event()
        # self.group.setPos(self.viewport.topleft.pos())

    def init_scene_items(self, viewport):
        self.render_props()
        super().init_scene_items(viewport)
        # self.viewport.scene().addItem(self.group)

    def render_props(self):
        for i in self.props:
            i.remove_graphics(self.viewport)
        self.props = []
        for i in self.level.l_props:
            self.props.append(PropRenderable(self, i))
        self.set_visibility(self.mod.propsview.showprops.value)
        self.set_outline(self.mod.propsview.showoutline.value, self.mod.propsview.outline_color.value)

    def render_prop(self, index: int):
        p = PropRenderable(self, self.level.l_props[index])
        p.poly.init_graphics(self.viewport)  # because
        for i in p.rope_graphics:
            self.viewport.workscene.addItem(i)
        self.props.insert(index, p)
        p.init_graphics(self.viewport)
        p.set_visible(self.mod.propsview.showprops.value)
        p.set_outline(self.mod.propsview.showoutline.value, self.mod.propsview.outline_color.value)

    def remove_render_prop(self, index: int):
        p = self.props.pop(index)
        p.remove_graphics(self.viewport)
        p.remove_myself()

    def remove_prop(self, index: int):
        self.remove_render_prop(index)
        self.level.l_props.pop(index)

    def pop_prop(self):
        self.remove_prop(len(self.props) - 1)

    def add_prop(self, index: int, prop):
        self.level.l_props.insert(index, prop)
        self.render_prop(index)

    def append_prop(self, prop):
        self.add_prop(len(self.props), prop)

    def move_prop(self, index: int, newindex: int):
        self.props.insert(newindex, self.props.pop(index))
        self.level.l_props.insert(newindex, self.level.l_props.pop(index))

    def level_resized(self):
        self.render_props()

    def set_visibility(self, state):
        for i in self.props:
            i.set_visible(state)

    def set_outline(self, state, color):
        for i in self.props:
            i.set_outline(state, color)
