from RWESharp.Ui import ViewUI, UI, SettingUI
from RWESharp.Configurable import BoolConfigurable, KeyConfigurable, PenConfigurable
from BaseMod.camera.ui.camera_vis_ui import Ui_CameraView
from BaseMod.camera.ui.camerasettings_ui import Ui_Cameras as Ui_CameraSettings
from BaseMod.camera.ui.cameras_ui import Ui_Cameras
from PySide6.QtGui import QAction, QColor, QPen
from PySide6.QtCore import QCoreApplication, QPoint, Qt
from PySide6.QtWidgets import QCheckBox, QTreeWidgetItem

from widgets.SettingsViewer import SettingsViewer


class CameraUI(UI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_Cameras()
        self.ui.setupUi(self)
        self.editor = self.mod.cameraeditor
        self.editor.cameraui = self

        self.ui.CameraTree.setSelectionMode(self.ui.CameraTree.SelectionMode.ExtendedSelection)

        self.add_key = KeyConfigurable(mod, "EDIT_cameras.add", "Ctrl+a", "Add Camera")

        self.add_key.link_button(self.ui.AddCamera)
        self.ui.AddCamera.clicked.connect(self.editor.add_camera)
        self.ui.RemoveCamera.clicked.connect(self.remove_cameras)

    def add_cameras(self):
        self.ui.CameraTree.clear()
        for i, v in enumerate(self.editor.viewport.level.l_cameras):
            item = QTreeWidgetItem([str(i), str([v.pos.x(), v.pos.y()])])
            self.ui.CameraTree.addTopLevelItem(item)
        self.ui.CameraTree.resizeColumnToContents(0)

    def remove_cameras(self):
        indexes = [v.row() for i, v in enumerate(self.ui.CameraTree.selectedIndexes()) if i % 2 == 0]
        self.editor.remove_cameras(indexes)

    def select_camera(self, row, clear=True):
        item = self.ui.CameraTree.itemAt(QPoint(0, row * self.ui.CameraTree.sizeHintForRow(0)))
        if clear:
            self.ui.CameraTree.setCurrentItem(item)
            return
        item.setSelected(True)

    def reset_selection(self):
        self.ui.CameraTree.clearSelection()


class CameraViewUI(ViewUI):
    def __init__(self, mod, parent=None):
        super().__init__(mod, parent)
        self.ui = Ui_CameraView()
        self.ui.setupUi(self)

        self.show_cameras = BoolConfigurable(mod, "VIEW_cameras.show", True, "Show Cameras")
        self.show_cameras_key = KeyConfigurable(mod, "VIEW_cameras.show_key", "Alt+c", "Show Cameras Key")
        self.showcamaction = QAction("Cameras")
        self.show_cameras.link_button_action(self.ui.ShowCameras, self.showcamaction, self.show_cameras_key)

        self.rectcolor = PenConfigurable(mod, "VIEW_cameras.rectcolor", QPen(QColor(0, 255, 0, 190), 4, Qt.PenStyle.DashDotLine), "Outer Camera rect color")
        self.rect2color = PenConfigurable(mod, "VIEW_cameras.rect2color", QPen(QColor(0, 120, 0, 190), 3), "Inner Camera rect color")
        self.rect3color = PenConfigurable(mod, "VIEW_cameras.rect3color", QPen(QColor(255, 255, 0, 120), 3, Qt.PenStyle.DotLine), "4x3 Camera rect color")
        self.rectcentercolor = PenConfigurable(mod, "VIEW_cameras.rectcentercolor", QPen(QColor(40, 40, 40, 120), 5), "Camera rect center color")
        self.polycolor = PenConfigurable(mod, "VIEW_cameras.polycolor", QPen(QColor(0, 255, 0, 210), 6, Qt.PenStyle.DashLine), "Outer Camera polygon color")
        self.circcolor = PenConfigurable(mod, "VIEW_cameras.polycolor", QPen(QColor(0, 255, 0, 210), 5), "Camera corner circle color")

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
