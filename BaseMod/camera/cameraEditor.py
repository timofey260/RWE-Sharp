from RWESharp.Modify import Editor
from RWESharp.Renderable import Handle, RenderList
from BaseMod.camera.cameraRenderable import RenderCamera
from BaseMod.camera.cameraHistory import AddCamera, RemoveCamera
from BaseMod.LevelParts import CameraLevelPart


class CameraHandles(RenderList):
    def __init__(self, module, depth, camera: CameraLevelPart.Camera, rendercamera: RenderCamera):
        super().__init__(module, depth)
        self.camera = camera
        self.rendercamera = rendercamera

        self.poshandle = Handle(module)
        self.renderables.append(self.poshandle)
        self.poshandle.setPos(self.camera.pos)
        self.poshandle.posChanged.connect(self.rendercamera.setPos)
        self.poshandle.mouseReleased.connect(self.changepos)  # todo

    def changepos(self, x):
        self.camera.pos = x


class CameraEditor(Editor):
    def __init__(self, mod):
        super().__init__(mod)
        self.cameraui = None
        self.handles: list[CameraHandles] = []

    def init_scene_items(self, viewport):
        self.add_handles()
        super().init_scene_items(viewport)
        
    def remove_items_from_scene(self, viewport):
        self.clear_handles()
        super().remove_items_from_scene(viewport)

    def clear_handles(self):
        for i in self.handles:
            i.remove_graphics(self.viewport)
            i.remove_myself()
        self.handles.clear()

    def add_camera(self):
        module = self.viewport.modulenames["cameras"]
        self.level.add_history(AddCamera(self.level.history, module, len(module.cameras), self.editor_pos))
        self.add_handles(True)

    def remove_camera(self):
        pass

    def add_handles(self, init=False):
        self.clear_handles()
        for i, v in enumerate(self.level.l_cameras):
            self.handles.append(CameraHandles(self, 0, v, self.viewport.modulenames["cameras"].cameras[i]))
        if init:
            for i in self.handles:
                i.init_graphics(self.viewport)
        self.cameraui.add_cameras()
