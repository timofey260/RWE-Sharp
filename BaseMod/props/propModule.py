from RWESharp.Modify import Module
from BaseMod.props.propRenderable import PropRenderable


class PropModule(Module):
    def render_module(self):
        pass

    def __init__(self, mod):
        super().__init__(mod)
        self.props = []
        for i in self.manager.level.props:
            self.props.append(PropRenderable(self.mod, 5, i).add_myself(self))

