from PySide6.QtWidgets import QMainWindow, QFileDialog, QSpacerItem, QSizePolicy, QWidget, QGridLayout
from PySide6.QtCore import Slot, Qt, QUrl
from PySide6.QtGui import QDesktopServices

from ui.FunnyVideo import FunnyVideo
from ui.uiscripts.mainui import Ui_MainWindow
from ui.aboutuiconnector import AboutDialog
from ui.settingsuiconnector import SettingsDialogUI
from ui.hotkeysuiconnector import HotkeysUI
from core.utils import modify_path_url
from core.info import PATH_LEVELS, PATH_FILES_VIDEOS, PATH_DRIZZLE, ISWIN, REPO_ISSUES, REPO

import os


class MainWindow(QMainWindow):
    '''
    Main window and bare ui of RWE#
    '''
    def __init__(self, app, filename=None):
        """
        :param filename:  file to load by default
        """
        from core.Manager import Manager
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tabWidget.clear()
        self.ui.tabWidget.setTabsClosable(True)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.open_about)
        self.ui.actionPreferences.triggered.connect(self.open_settings)
        self.ui.actionHotkeys.triggered.connect(self.open_hotkeys)
        self.manager = Manager(self, app, filename)
        self.manager.basemod.bmconfig.hotkey_key.link_action(self.ui.actionHotkeys)
        self.manager.basemod.bmconfig.settings_key.link_action(self.ui.actionPreferences)
        self.manager.basemod.bmconfig.view_key.link_action(self.ui.actionView)
        self.manager.basemod.bmconfig.edit_key.link_action(self.ui.actionEditors)
        self.manager.basemod.bmconfig.prefabs_key.link_action(self.ui.actionPrefabs)

        self.manager.basemod.bmconfig.new_key.link_action(self.ui.actionNew)
        self.manager.basemod.bmconfig.open_key.link_action(self.ui.actionOpen)
        self.manager.basemod.bmconfig.save_as_key.link_action(self.ui.actionSave_As)
        self.manager.basemod.bmconfig.close_key.link_action(self.ui.actionClose)
        self.manager.basemod.bmconfig.render_key.link_action(self.ui.actionRender)
        self.manager.basemod.bmconfig.opendrizzle_key.link_action(self.ui.actionLaunch_Drizzle)

        self.manager.basemod.bmconfig.zoom_in_key.link_action(self.ui.actionZoom_In)
        self.ui.actionZoom_In.triggered.connect(lambda: self.manager.selected_viewport.do_zoom(0.2))
        self.manager.basemod.bmconfig.zoom_out_key.link_action(self.ui.actionZoom_Out)
        self.ui.actionZoom_Out.triggered.connect(lambda: self.manager.selected_viewport.do_zoom(-0.2))

        self.manager.basemod.bmconfig.about_key.link_action(self.ui.actionAbout)

        # self.ui.viewPort.add_managed_fields(self.manager)

        # self.ui.menuRecent.addAction(QAction("lol", self.ui.menuRecent))
        self.ui.ToolsTabs.currentChanged.connect(self.change_editor)
        self.ui.tabWidget.currentChanged.connect(self.manager.mount_editor)
        self.about = None
        self.settings: SettingsDialogUI | None = None
        self.hotkeys: HotkeysUI | None = None

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.ui.QuickOverlay.addItem(self.verticalSpacer)

        self.manager.basemod.bmconfig.save_key.link_action(self.ui.actionSave)
        self.ui.actionSave.triggered.connect(self.manager.save_level)
        self.manager.basemod.bmconfig.save_as_key.link_action(self.ui.actionSave_As)
        self.ui.actionSave_As.triggered.connect(self.manager.save_level_as)

        self.manager.basemod.bmconfig.undo_key.link_action(self.ui.actionUndo)
        self.ui.actionUndo.triggered.connect(self.manager.undo)
        self.manager.basemod.bmconfig.redo_key.link_action(self.ui.actionRedo)
        self.ui.actionRedo.triggered.connect(self.manager.redo)

        self.ui.DockTools.link_action(self.ui.actionEditors)
        self.ui.DockView.link_action(self.ui.actionView)
        self.ui.DockPrefabs.link_action(self.ui.actionPrefabs)

        self.ui.actionRender.triggered.connect(lambda: self.level_render(self.ui.tabWidget.currentWidget().level))
        self.ui.actionLaunch_Drizzle.triggered.connect(lambda:
            QDesktopServices.openUrl(modify_path_url(os.path.join(PATH_DRIZZLE, "Drizzle.Editor.exe" if ISWIN else "Drizzle.Editor"))))
        self.ui.actionRender_All_Levels.triggered.connect(self.render_all)
        self.ui.actionDrizzleOpenExplorer.triggered.connect(lambda: QDesktopServices.openUrl(modify_path_url(PATH_DRIZZLE)))
        self.ui.actionOpen_Levels_Folder.triggered.connect(lambda: QDesktopServices.openUrl(modify_path_url(PATH_LEVELS)))
        self.ui.actionRWE_Github.triggered.connect(lambda: QDesktopServices.openUrl(REPO))
        self.ui.actionRWE_Issues.triggered.connect(lambda: QDesktopServices.openUrl(REPO_ISSUES))
        self.ui.actionOpen_ShowLevelFile.triggered.connect(lambda: self.open_level_folder(self.ui.tabWidget.currentWidget().level))

        self.hotkeys = HotkeysUI(self.manager, self)
        self.settings = SettingsDialogUI(self.manager, self)

        self.setWindowModality(Qt.WindowModality.NonModal)
        self.setDockNestingEnabled(True)

        self.vid = None

    def level_render(self, level):
        print(level)  #todo
        a, _ = os.path.split(level.file)
        print(QDesktopServices.openUrl(modify_path_url(a)), a)

    def render_all(self):
        for i in range(self.ui.tabWidget.count()):
            self.level_render(self.ui.tabWidget.widget(i).level)

    def add_viewport(self, viewport):
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.addTab(viewport, viewport.level.shortname))

    def open_level_folder(self, level):
        if level.file is None or self.ui.tabWidget.count() <= 0:
            return
        a, _ = os.path.split(level.file)
        QDesktopServices.openUrl(modify_path_url(a))

    @Slot(int)
    def change_editor(self, val) -> None:
        self.manager.change_editor(val)

    @Slot()
    def open_about(self) -> None:
        self.about = AboutDialog(self)
        self.about.show()

    @Slot()
    def open_settings(self) -> None:
        self.settings.setVisible(True)

    @Slot()
    def open_hotkeys(self) -> None:
        self.hotkeys.setVisible(True)

    @Slot()
    def close(self) -> None:
        if self.manager.basemod.bmconfig.funny_vid.value and self.manager.basemod.bmconfig.funny.value:
            self.vid = FunnyVideo(self.manager, True, os.path.join(PATH_FILES_VIDEOS, "fnuuy.mp4").replace("\\", "/"), "GoodBye")
        else:
            self.manager.application.exit()

    def closeEvent(self, event):
        self.close()

    @Slot()
    def open_file(self) -> None:
        name, _ = QFileDialog.getOpenFileName(None, "Open Level", PATH_LEVELS, "Level files (*.txt *.wep *.rwl)")
        if name == "":
            return
        self.manager.change_level(name)

    @Slot()
    def new_file(self) -> None:
        self.manager.change_level(None)

    @Slot()
    def close_tab(self, index):
        self.ui.tabWidget.removeTab(index)
        # todo confirmation
