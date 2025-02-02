from RWESharp.Ui import ViewUI, UI
from RWESharp.Configurable import BoolConfigurable, KeyConfigurable
from BaseMod.camera.ui.camera_vis_ui import Ui_CameraView
from PySide6.QtGui import QAction


class CameraViewUI(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_CameraView()
        self.ui.setupUi(self)

        self.show_cameras = BoolConfigurable(mod, "VIEW_cameras.show", True, "Show Cameras")
        self.show_cameras_key = KeyConfigurable(mod, "VIEW_cameras.show_key", "Ctrl+5", "Show Cameras Key")
        self.showcamaction = QAction("Cameras")
        self.show_cameras.link_button_action(self.ui.ShowCameras, self.showcamaction, self.show_cameras_key)

        self.mod.manager.view_menu.addAction(self.showcamaction)
