from RWESharp.Modify import Module
from RWESharp.Configurable import BoolConfigurable
from BaseMod.props.propRenderable import PropRenderable
from BaseMod.props.Handle import Handle


class PropModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.opshift = BoolConfigurable(mod, "VIEW_props.opshift", True, "Opacity shift")
        self.props: list[PropRenderable] = []
        Handle(self)

    def init_scene_items(self, viewport):
        self.render_props()
        super().init_scene_items(viewport)

    def render_props(self):
        for i in self.props:
            i.remove_graphics(self.viewport)
        self.props = []
        for i in self.level.props:
            self.props.append(PropRenderable(self, i))

    def render_prop(self, index: int):
        p = PropRenderable(self, self.level.props[index])
        self.props.append(p)
        p.init_graphics(self.viewport)

    def remove_render_prop(self, index: int):
        p = self.props.pop(index)
        p.remove_graphics(self.viewport)
        p.remove_myself()

    def remove_prop(self, index: int):
        self.remove_render_prop(index)
        self.level.props.pop(index)

    def pop_prop(self):
        self.remove_prop(len(self.props) - 1)

    def add_prop(self, index: int, prop: list):
        self.level.props.insert(index, prop)
        self.render_prop(index)

    def append_prop(self, prop: list):
        self.add_prop(len(self.props), prop)

    def move_prop(self, index: int, newindex: int):
        self.props.insert(newindex, self.props.pop(index))
        self.level.props.insert(newindex, self.level.props.pop(index))

    def level_resized(self):
        self.render_props()
