from RWESharp.Modify import Module
from RWESharp.Configurable import BoolConfigurable
from BaseMod.props.propRenderable import PropRenderable


class PropModule(Module):
    def render_module(self):
        pass

    def __init__(self, mod):
        super().__init__(mod)
        self.opshift = BoolConfigurable(mod, "VIEW_props.opshift", True, "Opacity shift")
        self.props: list[PropRenderable] = []
        self.render_props()

    def render_props(self):
        for i in self.props:
            i.remove_graphics()
        self.props = []
        for i in self.manager.level.props:
            self.props.append(PropRenderable(self.mod, i).add_myself(self))

    def render_prop(self, index: int):
        p = PropRenderable(self.mod, self.manager.level.props[index]).add_myself(self)
        self.props.append(p)
        p.init_graphics()

    def remove_render_prop(self, index: int):
        p = self.props.pop(index)
        p.remove_graphics()
        self.renderables.remove(p)

    def remove_prop(self, index: int):
        self.remove_render_prop(index)
        self.manager.level.props.pop(index)

    def pop_prop(self):
        self.remove_prop(len(self.props) - 1)

    def add_prop(self, index: int, prop: list):
        self.manager.level.props.insert(index, prop)
        self.render_prop(index)

    def append_prop(self, prop: list):
        self.add_prop(len(self.props), prop)

    def move_prop(self, index: int, newindex: int):
        self.props.insert(newindex, self.props.pop(index))
        self.manager.level.props.insert(newindex, self.manager.level.props.pop(index))
