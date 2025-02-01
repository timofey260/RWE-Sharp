from RWESharp.Modify import Module
from widgets.Viewport import ViewPort
from BaseMod.camera.cameraRenderable import RenderCamera


class CameraModule(Module):
    def __init__(self, mod):
        super().__init__(mod)
        self.cameras = []

    def init_scene_items(self, viewport):
        for i in viewport.level.l_cameras:
            self.cameras.append(RenderCamera(self, 5, i.pos))