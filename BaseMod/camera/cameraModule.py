from RWESharp.Modify import Module
from widgets.Viewport import ViewPort
from BaseMod.camera.cameraRenderable import RenderCamera
from BaseMod.LevelParts import CameraLevelPart
from PySide6.QtCore import QPointF

cameradepth = 5


class CameraModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.cameras: list[RenderCamera] = []
        self.mod.cameraview.show_cameras.valueChanged.connect(self.change_visibility)

    def init_scene_items(self, viewport):
        for i in viewport.level.l_cameras:
            self.cameras.append(RenderCamera(self, cameradepth, i))
        self.change_visibility(self.mod.cameraview.show_cameras.value)

    def change_visibility(self, state):
        for i in self.cameras:
            i.change_visibility(state)

    def pop_camera(self, index):
        rc = self.cameras.pop(index)
        rc.remove_graphics(self.viewport)
        rc.remove_myself()
        pop = self.level.l_cameras.pop(index)
        self.reindex()
        return pop

    def add_new_camera(self, index, pos):
        cam = CameraLevelPart.Camera(pos, [QPointF(), QPointF(), QPointF(), QPointF()])
        self.add_camera(index, cam)

    def add_camera(self, index, camera: CameraLevelPart.Camera):
        self.level.l_cameras.cameras.insert(index, camera)
        rc = RenderCamera(self, cameradepth, camera)
        rc.init_graphics(self.viewport)
        rc.textindex.setPlainText(str(index))
        self.cameras.insert(index, rc)

    def move_camera(self, index, newindex):
        cam = self.level.l_cameras.cameras.pop(index)
        rc = self.cameras.pop(index)

        self.level.l_cameras.cameras.insert(index, cam)
        self.cameras.insert(max(0, newindex), rc)
        self.reindex()

    def reindex(self):
        for i, v in enumerate(self.cameras):
            v.textindex.setPlainText(str(i))

