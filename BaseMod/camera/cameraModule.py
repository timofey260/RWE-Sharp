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
        return self.viewport.level.l_cameras.pop(index)

    def add_new_camera(self, index, pos):
        cam = CameraLevelPart.Camera(pos, [QPointF(), QPointF(), QPointF(), QPointF()])
        self.add_camera(index, cam)

    def add_camera(self, index, camera: CameraLevelPart.Camera):
        self.viewport.level.l_cameras.cameras.insert(index, camera)
        rc = RenderCamera(self, cameradepth, camera)
        rc.init_graphics(self.viewport)
        self.cameras.insert(index, rc)
