from RWESharp.Ui import ViewUI, UI, SettingUI
from RWESharp.Configurable import BoolConfigurable, KeyConfigurable
from BaseMod.camera.ui.camera_vis_ui import Ui_CameraView
from BaseMod.camera.ui.camerasettings_ui import Ui_Cameras as Ui_CameraSettings
from BaseMod.camera.ui.cameras_ui import Ui_Cameras
from PySide6.QtGui import QAction
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QCheckBox

from widgets.SettingsViewer import SettingsViewer


class CameraUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_Cameras()
        self.ui.setupUi(self)


class CameraViewUI(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_CameraView()
        self.ui.setupUi(self)

        self.show_cameras = BoolConfigurable(mod, "VIEW_cameras.show", True, "Show Cameras")
        self.show_cameras_key = KeyConfigurable(mod, "VIEW_cameras.show_key", "Alt+c", "Show Cameras Key")
        self.showcamaction = QAction("Cameras")
        self.show_cameras.link_button_action(self.ui.ShowCameras, self.showcamaction, self.show_cameras_key)

        self.VQuickCameras = QCheckBox()
        self.VQuickCameras.setObjectName(u"VQuickCameras")
        self.VQuickCameras.setText(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.VQuickCameras.setChecked(True)
        self.mod.add_quickview_option(self.VQuickCameras)
        self.show_cameras.link_button_action(self.VQuickCameras, self.showcamaction, self.show_cameras_key)

        self.mod.manager.view_menu.addAction(self.showcamaction)


class CameraSettingsUI(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_CameraSettings()
        self.ui.setupUi(viewer)
        # todo
