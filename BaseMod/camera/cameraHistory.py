from PySide6.QtCore import QRect

from RWS.Modify import HistoryElement
from RWS.Core import CELLSIZE


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
        self.redo_changes(False)

    def undo_changes(self):
        for i in self.cameras:
            self.history.level.l_cameras[i].pos -= self.offset
            self.history.level.l_cameras[i].pos.setX(round(self.history.level.l_cameras[i].pos.x(), 4))
            self.history.level.l_cameras[i].pos.setY(round(self.history.level.l_cameras[i].pos.y(), 4))
            self.module.cameras[i].update_camera()
        self.editor.reset_selection()
        self.editor.cameraui.add_cameras()

    def redo_changes(self, reset=True):
        for i in self.cameras:
            self.history.level.l_cameras[i].pos += self.offset
            self.history.level.l_cameras[i].pos.setX(round(self.history.level.l_cameras[i].pos.x(), 4))
            self.history.level.l_cameras[i].pos.setY(round(self.history.level.l_cameras[i].pos.y(), 4))
            self.module.cameras[i].update_camera()
        if reset:
            self.editor.reset_selection()
        self.editor.cameraui.add_cameras()


class CameraQuadMove(HistoryElement):
    def __init__(self, history, editor, module, quad: int, cameras: list[int]):
        super().__init__(history)
        self.editor = editor
        self.module = module
        self.cameras = cameras
        self.offsets = []
        self.quad = quad
        for i in self.cameras:
            oldpos = self.module.cameras[i].camera.quads[quad]
            newpos = self.module.cameras[i].newquads[quad]
            self.offsets.append([i, oldpos, newpos])
            self.module.cameras[i].camera.quads[quad] = newpos

            self.module.cameras[i].fix_offset(self.quad)
        #self.redo_changes(True)
        # self.editor.reset_selection()

    def undo_changes(self):
        for i in self.offsets:
            index = i[0]
            oldpos = i[1]
            self.module.cameras[index].camera.quads[self.quad] = oldpos
            self.module.cameras[index].fix_offset(self.quad)

        self.editor.reset_selection()

    def redo_changes(self, reset=True):
        for i in self.offsets:
            index = i[0]
            newpos = i[2]
            self.module.cameras[index].camera.quads[self.quad] = newpos
            self.module.cameras[index].fix_offset(self.quad)
        if reset:
            self.editor.reset_selection()


class MoveCameraOrder(HistoryElement):
    def __init__(self, history, editor, module, up: bool, cameras: list[int]):
        super().__init__(history)
        self.editor = editor
        self.module = module
        self.cameras = cameras
        self.cameras.sort(reverse=not up)
        self.up = up
        self.cameras_moved = []
        self.cams_amount = len(self.module.cameras)
        self.redo_changes(False)
        # self.editor.reset_selection()

    def undo_changes(self):
        if self.up:
            for i in reversed(self.cameras_moved):
                if i >= self.cams_amount - 1:
                    continue
                self.module.move_camera(i, i + 1)
        else:
            for i in reversed(self.cameras_moved):
                if i == 0:
                    continue
                self.module.move_camera(i, i - 1)
        self.editor.cameraui.add_cameras()
        self.editor.reset_selection()

    def redo_changes(self, reset=True):
        self.cameras_moved = []
        if self.up:
            for i in self.cameras:
                if i == 0:
                    continue
                self.cameras_moved.append(i - 1)
                self.module.move_camera(i, i - 1)
        else:
            for i in self.cameras:
                if i >= self.cams_amount - 1:
                    continue
                self.cameras_moved.append(i + 1)
                self.module.move_camera(i, i + 1)
        if reset:
            self.editor.reset_selection()
        self.editor.cameraui.add_cameras()

class LevelResizedCameras(HistoryElement):
    def __init__(self, history, newrect: QRect):
        super().__init__(history)
        self.module = self.level.viewport.modulenames["cameras"]
        self.newrect = newrect
        self.redo_changes()

    def undo_changes(self):
        for i in self.level.l_cameras.cameras:
            i.pos += self.newrect.topLeft() * CELLSIZE
        for i in self.module.cameras:
            i.update_camera()

    def redo_changes(self):
        for i in self.level.l_cameras.cameras:
            i.pos -= self.newrect.topLeft() * CELLSIZE
        for i in self.module.cameras:
            i.update_camera()
