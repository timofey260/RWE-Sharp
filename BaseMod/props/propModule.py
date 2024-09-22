from RWESharp.Modify import Module
from RWESharp.Configurable import BoolConfigurable
from BaseMod.props.propRenderable import PropRenderable


class PropModule(Module):
    def render_module(self):
        pass

    def __init__(self, mod):
        super().__init__(mod)
        self.opshift = BoolConfigurable(mod, "VIEW_props.opshift", True, "Opacity shift")
        self.props = []
        for i in self.manager.level.props:
            self.props.append(PropRenderable(self.mod, i).add_myself(self))
