from RWESharp.Modify import Module
from widgets.Viewport import ViewPort
from BaseMod.camera.cameraRenderable import RenderCamera


class CameraModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.cameras: list[RenderCamera] = []
        self.mod.cameraview.show_cameras.valueChanged.connect(self.change_visibility)

    def init_scene_items(self, viewport):
        for i in viewport.level.l_cameras:
            self.cameras.append(RenderCamera(self, 5, i))
        self.change_visibility(self.mod.cameraview.show_cameras.value)

    def change_visibility(self, state):
        for i in self.cameras:
            i.change_visibility(state)
