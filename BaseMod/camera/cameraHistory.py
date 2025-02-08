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
    def __init__(self, history, editor, module, cameras: list, offset):
        super().__init__(history)
        self.editor = editor
        self.module = module
        self.cameras = cameras
        self.offset = offset
        self.redo_changes()

    def undo_changes(self):
        for i in self.cameras:
            i.camera.pos -= self.offset
            i.update_camera()

    def redo_changes(self):
        for i in self.cameras:
            i.camera.pos += self.offset
            i.update_camera()
