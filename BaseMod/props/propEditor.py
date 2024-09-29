from RWESharp.Modify import Editor
from BaseMod.props.propExplorer import PropExplorer


class PropEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.explorer = PropExplorer(self, self.manager.window)