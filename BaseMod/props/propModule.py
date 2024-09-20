from RWESharp.Modify import Module
from BaseMod.props.propRenderable import PropRenderable


class PropModule(Module):
    def render_module(self):
        for i in self.manager.level.props:
            self.props.append(PropRenderable(self.mod, 0, i).add_myself(self))

    def __init__(self, mod):
        super().__init__(mod)
        self.props = []

