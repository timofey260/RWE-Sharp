from PySide6.QtWidgets import QMainWindow, QFileDialog, QSpacerItem, QSizePolicy
from PySide6.QtCore import Slot
from ui.uiscripts.mainui import Ui_MainWindow, QWidget
from ui.aboutuiconnector import AboutDialog
from ui.settingsuiconnector import SettingsUI
from ui.hotkeysuiconnector import HotkeysUI
from core.info import PATH_LEVELS, PATH_FILES

import os
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput


class FunnyVideo(QWidget):
    def __init__(self, manager):
        super().__init__()
        self.manager = manager
        self.video = QVideoWidget(self)
        self.audio = QAudioOutput(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video)
        self.player.setAudioOutput(self.audio)
        self.player.setSource(os.path.join(PATH_FILES, "fnuuy.mp4").replace("\\", "/"))  # reasons beyond
        self.player.mediaStatusChanged.connect(self.frame)
        self.player.play()
        size = 250
        self.setMinimumSize(size, size)
        self.video.setMinimumSize(size, size)
        self.setWindowTitle("Goodbye")
        self.show()

    @Slot(QMediaPlayer.MediaStatus)
    def frame(self, status: QMediaPlayer.MediaStatus):
        if status == status.EndOfMedia:
            self.manager.application.app.exit()


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

        self.ui.actionOpen.triggered.connect(self.open_file)
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
        self.manager.basemod.bmconfig.opendrizzle_key.link_action(self.ui.actionDrizzleOpen)

        self.manager.basemod.bmconfig.about_key.link_action(self.ui.actionAbout)

        self.ui.viewPort.add_managed_fields(self.manager)

        # self.ui.menuRecent.addAction(QAction("lol", self.ui.menuRecent))
        self.ui.ToolsTabs.currentChanged.connect(self.change_editor)
        self.about = None
        self.settings: SettingsUI | None = None
        self.hotkeys: HotkeysUI | None = None

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.ui.QuickOverlay.addItem(self.verticalSpacer)

        self.manager.basemod.bmconfig.save_key.link_action(self.ui.actionSave)
        self.ui.actionSave.triggered.connect(self.manager.save_level)

        self.manager.basemod.bmconfig.undo_key.link_action(self.ui.actionUndo)
        self.ui.actionUndo.triggered.connect(self.manager.undo)
        self.manager.basemod.bmconfig.redo_key.link_action(self.ui.actionRedo)
        self.ui.actionRedo.triggered.connect(self.manager.redo)

        self.ui.DockTools.link_action(self.ui.actionEditors)
        self.ui.DockView.link_action(self.ui.actionView)
        self.ui.DockPrefabs.link_action(self.ui.actionPrefabs)

        self.hotkeys = HotkeysUI(self.manager, self)
        self.settings = SettingsUI(self.manager, self)

        self.vid = None

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
        if self.manager.basemod.bmconfig.funny_vid.value:
            self.vid = FunnyVideo(self.manager)
        else:
            self.manager.application.app.exit()

    def closeEvent(self, event):
        self.close()

    @Slot()
    def open_file(self) -> None:
        name, _ = QFileDialog.getOpenFileName(None, "Open Level", PATH_LEVELS, "Level files (*.txt *.wep *.rwl)")
        if name == "":
            return
        self.manager.change_level(name)
