from RWESharp.Modify import Module
from BaseMod.props.propRenderable import PropRenderable


class PropModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.props: list[PropRenderable] = []
        mod.propsview.ui.ShowProps.toggled.connect(self.set_visibility)
        mod.propsview.ui.Outline.toggled.connect(lambda x: self.set_outline(x, mod.propsview.outline_color.value))
        mod.propsview.ui.OutlineColor.colorPicked.connect(lambda x: self.set_outline(True, x))
        # Handle(self)

    def init_scene_items(self, viewport):
        self.render_props()
        super().init_scene_items(viewport)

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
        self.props.insert(index, p)
        p.init_graphics(self.viewport)

    def remove_render_prop(self, index: int):
        p = self.props.pop(index)
        p.remove_graphics(self.viewport)
        p.remove_myself()

    def remove_prop(self, index: int):
        self.remove_render_prop(index)
        self.level.l_props.pop(index)

    def pop_prop(self):
        self.remove_prop(len(self.props) - 1)

    def add_prop(self, index: int, prop: list):
        self.level.l_props.insert(index, prop)
        self.render_prop(index)

    def append_prop(self, prop: list):
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
