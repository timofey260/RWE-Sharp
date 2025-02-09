from RWESharp.Modify import HistoryElement


class AddCamera(HistoryElement):
    def __init__(self, history, editor, module, index, pos):
        super().__init__(history)
        self.module = module
        self.index = index
        self.pos = pos
        self.editor = editor
        self.module.add_new_camera(self.index, self.pos)

    def undo_changes(self):
        self.module.pop_camera(self.index)
        self.editor.add_handles()

    def redo_changes(self):
        self.module.add_new_camera(self.index, self.pos)
        self.editor.add_handles()


class RemoveCamera(HistoryElement):
    def __init__(self, history, editor, module, cameras: list[int]):
        super().__init__(history)
        cameras.sort(reverse=True)
        self.cams: [..., int] = []
        self.module = module
        self.cameras = list[int]
        self.editor = editor
        for i in cameras:
            self.cams.append([module.pop_camera(i), i])
        self.editor.add_handles()

    def undo_changes(self):
        for i in self.cams:
            self.module.add_camera(i[1], i[0])
        self.editor.add_handles()

    def redo_changes(self):
        for i in self.cams:
            self.module.pop_camera(i[1])
        self.editor.add_handles()


class CameraMove(HistoryElement):
    def __init__(self, history, editor, module, cameras: list[int], offset):
        super().__init__(history)
        self.editor = editor
        self.module = module
        self.cameras = cameras
        self.offset = offset
        self.redo_changes(True)

    def undo_changes(self):
        for i in self.cameras:
            self.history.level.l_cameras[i].pos -= self.offset
            self.module.cameras[i].update_camera()
        self.editor.reset_selection()

    def redo_changes(self, reset=False):
        for i in self.cameras:
            self.history.level.l_cameras[i].pos += self.offset
            self.module.cameras[i].update_camera()
        if reset:
            self.editor.reset_selection()


class CameraQuadMove(HistoryElement):
    def __init__(self, history, editor, module, quad: int, cameras: list[int], offset):
        super().__init__(history)
        self.editor = editor
        self.module = module
        self.cameras = cameras
        self.offset = offset
        self.quad = quad
        self.redo_changes(True)

    def undo_changes(self):
        for i in self.cameras:
            self.history.level.l_cameras[i].quads[self.quad] -= self.offset
            self.module.cameras[i].update_camera()
        self.editor.reset_selection()

    def redo_changes(self, reset=False):
        for i in self.cameras:
            self.history.level.l_cameras[i].quads[self.quad] += self.offset
            self.module.cameras[i].update_camera()
        if reset:
            self.editor.reset_selection()
