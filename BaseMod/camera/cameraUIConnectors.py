from PySide6.QtCore import QCoreApplication, QPoint, Qt
from PySide6.QtGui import QAction, QColor, QPen
from PySide6.QtWidgets import QCheckBox, QTreeWidgetItem

from BaseMod.camera.ui.camera_vis_ui import Ui_CameraView
from BaseMod.camera.ui.cameras_ui import Ui_Cameras
from BaseMod.camera.ui.camerasettings_ui import Ui_Cameras as Ui_CameraSettings
from RWESharp2.Configurable import BoolConfigurable, KeyConfigurable, PenConfigurable, ColorConfigurable
from RWESharp2.Ui import ViewUI, UI, SettingUI
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
        self.remove_key = KeyConfigurable(mod, "EDIT_cameras.remove", "Ctrl+d", "Remove Cameras")
        self.moveup_key = KeyConfigurable(mod, "EDIT_cameras.moveup", "Shift+w", "Move Cameras up")
        self.movedown_key = KeyConfigurable(mod, "EDIT_cameras.movedown", "Shift+s", "Move Cameras down")

        self.add_key.link_button(self.ui.AddCamera)
        self.remove_key.link_button(self.ui.RemoveCamera)
        self.moveup_key.link_button(self.ui.MoveUp)
        self.movedown_key.link_button(self.ui.MoveDown)

        self.ui.AddCamera.clicked.connect(self.editor.add_camera)
        self.ui.RemoveCamera.clicked.connect(self.remove_cameras)
        self.ui.CameraTree.itemClicked.connect(self.select_cameras)

        self.ui.MoveUp.clicked.connect(self.move_up)
        self.ui.MoveDown.clicked.connect(self.move_down)

    def move_up(self):
        self.editor.move_up(self.selection)

    def move_down(self):
        self.editor.move_down(self.selection)

    def select_cameras(self):
        self.editor.reset_selection(False)
        selection = self.selection
        self.editor.select_indexes(selection)

    def add_cameras(self):
        self.ui.CameraTree.clear()
        for i, v in enumerate(self.editor.viewport.modulenames["cameras"].cameras):
            item = QTreeWidgetItem([str(i), str([v.camera.pos.x(), v.camera.pos.y()])])
            self.ui.CameraTree.addTopLevelItem(item)
            item.setSelected(v in self.editor.selected)
        self.ui.CameraTree.resizeColumnToContents(0)

    def remove_cameras(self):
        self.editor.remove_cameras(self.selection)

    def select_camera(self, row, clear=True):
        item = self.ui.CameraTree.itemAt(QPoint(0, row * self.ui.CameraTree.sizeHintForRow(0)))
        if clear:
            self.ui.CameraTree.setCurrentItem(item)
            return
        item.setSelected(True)

    def reset_selection(self):
        self.ui.CameraTree.clearSelection()

    @property
    def selection(self):
        return [v.row() for i, v in enumerate(self.ui.CameraTree.selectedIndexes()) if i % 2 == 0]


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
        self.circcolor = PenConfigurable(mod, "VIEW_cameras.circcolor", QPen(QColor(0, 255, 0, 210), 5), "Camera corner circle color")
        self.indexcolor = ColorConfigurable(mod, "VIEW_cameras.fontcolor", QColor(168, 168, 168), "Font color")

        self.showrect = BoolConfigurable(mod, "VIEW_cameras.showrect", True, "Show Outer Camera rect")
        self.showrect2 = BoolConfigurable(mod, "VIEW_cameras.showrect2", True, "Show Inner Camera rect")
        self.showrect3 = BoolConfigurable(mod, "VIEW_cameras.showrect3", True, "Show 4x3 Camera rect")
        self.showrectcenter = BoolConfigurable(mod, "VIEW_cameras.showrectcenter", True, "Show Camera rect center")
        self.showpoly = BoolConfigurable(mod, "VIEW_cameras.showpoly", True, "Show Outer Camera polygon")
        self.showcirc = BoolConfigurable(mod, "VIEW_cameras.showcirc", True, "Show Camera corner circle")
        self.showindex = BoolConfigurable(mod, "VIEW_cameras.showfont", True, "Show Font")

        self.VQuickCameras = QCheckBox()
        self.VQuickCameras.setObjectName(u"VQuickCameras")
        self.VQuickCameras.setText(QCoreApplication.translate("MainWindow", u"Cameras", None))
        self.VQuickCameras.setChecked(True)
        self.mod.add_quickview_option(self.VQuickCameras)
        self.show_cameras.link_button_action(self.VQuickCameras, self.showcamaction, self.show_cameras_key)

        self.mod.manager.view_menu.addAction(self.showcamaction)
        self.showrect.link_button(self.ui.ShowOuter)
        self.showrect2.link_button(self.ui.ShowInner)
        self.showrect3.link_button(self.ui.Show43)
        self.showrectcenter.link_button(self.ui.ShowCenter)
        self.showpoly.link_button(self.ui.ShowCameraShape)
        self.showcirc.link_button(self.ui.ShowEdgeCircles)
        self.showindex.link_button(self.ui.ShowIndex)


class CameraSettingsUI(SettingUI):
    def __init__(self, mod):
        super().__init__(mod)
        self.viewui = self.mod.cameraview

        self.rectcolor = SettingUI.ManageableSetting(PenConfigurable(None, "rectcolor", QPen(), "Outer Camera rect color"),
                                                     self.viewui.rectcolor).add_myself(self)
        self.rect2color = SettingUI.ManageableSetting(PenConfigurable(None, "rect2color", QPen(), "Inner Camera rect color"),
                                                      self.viewui.rect2color).add_myself(self)
        self.rect3color = SettingUI.ManageableSetting(PenConfigurable(None, "rect3color", QPen(), "4x3 Camera rect color"),
                                                      self.viewui.rect3color).add_myself(self)
        self.rectcentercolor = SettingUI.ManageableSetting(PenConfigurable(None, "rectcentercolor", QPen(), "Camera rect center color"),
                                                           self.viewui.rectcentercolor).add_myself(self)
        self.polycolor = SettingUI.ManageableSetting(PenConfigurable(None, "polycolor", QPen(), "Outer Camera polygon color"),
                                                     self.viewui.polycolor).add_myself(self)
        self.circcolor = SettingUI.ManageableSetting(PenConfigurable(None, "circcolor", QPen(), "Camera corner circle color"),
                                                     self.viewui.circcolor).add_myself(self)
        self.indexcolor = SettingUI.ManageableSetting(ColorConfigurable(None, "fontcolor", QColor(), "Font color"),
                                                      self.viewui.indexcolor).add_myself(self)

    def init_ui(self, viewer: SettingsViewer):
        self.ui = Ui_CameraSettings()
        self.ui.setupUi(viewer)

        self.rectcolor.setting.link_pen_picker(self.ui.rect1)
        self.rect2color.setting.link_pen_picker(self.ui.rect2)
        self.rect3color.setting.link_pen_picker(self.ui.rect3)
        self.rectcentercolor.setting.link_pen_picker(self.ui.center)
        self.polycolor.setting.link_pen_picker(self.ui.poly)
        self.circcolor.setting.link_pen_picker(self.ui.circle)
        self.indexcolor.setting.link_color_picker(self.ui.Index)
