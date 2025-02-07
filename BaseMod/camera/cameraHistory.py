from RWESharp.Modify import HistoryElement


class AddCamera(HistoryElement):
    def __init__(self, history, module, index, pos):
        super().__init__(history)
        self.module = module
        self.index = index
        self.pos = pos
        self.redo_changes()

    def undo_changes(self):
        self.module.pop_camera(self.index)

    def redo_changes(self):
        self.module.add_new_camera(self.index, self.pos)


class RemoveCamera(HistoryElement):
    def __init__(self, history, module, index):
        super().__init__(history)
        self.cam = module.pop_camera(index)
        self.module = module
        self.index = index
        self.redo_changes()

    def undo_changes(self):
        self.module.add_camera(self.index, self.cam)

    def redo_changes(self):
        self.module.pop_camera(self.index)

