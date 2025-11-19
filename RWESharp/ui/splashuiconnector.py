import os.path

from RWESharp.ui.uiscripts.splash import Ui_Splash
from PySide6.QtWidgets import QSplashScreen
from RWESharp.Loaders.Loader import Loader
from RWESharp.utils import log
from PySide6.QtWidgets import QMessageBox
from RWESharp.info import drizzle_exists, REPO_DATABASE, PATH_DRIZZLE
from RWESharp.Loaders.Database import RWESharpDatabase


class SplashDialog(QSplashScreen):
    def __init__(self, callback, parent=None):
        super().__init__(parent)
        # self.manager = manager
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        self.hasdrizzle = self.check_drizzle()
        self.loader = Loader(self)
        self.loader.finished.connect(callback)
        # self.loader.finished.connect(self.loader.deleteLater)
        self.loader.finished.connect(self.close)
        self.loader.start()
        log("Loading Drizzle Data...")
        self.show()
        # self.setWindowFlag(Qt.WindowType.SplashScreen, True)

        # self.layout = QVBoxLayout(self.ui.widget)
        # self.ui.widget.setLayout(self.layout)
        # self.vid = QVideoWidget(self.ui.widget)
        # self.player = QMediaPlayer()
        # self.layout.addWidget(self.vid)
        # self.player.setSource("F:/Desktop/RWE#/Every 2012 intro.mp4")
        # self.player.setVideoOutput(self.vid)
        # self.audio_output = QAudioOutput()
        # self.player.setAudioOutput(self.audio_output)
        # self.player.play()
        # self.player.mediaStatusChanged.connect(self.frame) # hehe funny thing

    # @Slot(QMediaPlayer.MediaStatus)
    # def frame(self, status: QMediaPlayer.MediaStatus):
    #     if status == status.EndOfMedia:
    #         print("end")

    def check_drizzle(self):
        if not drizzle_exists:
            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.Warning)
            text = f"Drizzle is not installed!\nWould you like for RWE# to download it automatically from Database?"
            message.setText(text)
            message.setDetailedText("RWE# cannot function without drizzle!")
            # todo insert server link
            message.setStandardButtons(QMessageBox.StandardButton.Close | QMessageBox.StandardButton.Yes)
            message.setDefaultButton(QMessageBox.StandardButton.Close)
            value = message.exec()
            if value == QMessageBox.StandardButton.Close:
                return False

            database = RWESharpDatabase(REPO_DATABASE)
            connection = database.connect()
            if not connection:
                print("Failed to connect to Database! No way to install Drizzle")
                return False
            link = database.get_drizzle_link()
            if link is None:
                print("Drizzle not found! Cannot proceed without Drizzle")
                return False

            installed = database.install_drizzle_from_link(link)
            if not installed:
                print("Drizzle is failed to install! Cannot proceed without Drizzle")
                return False
            return os.path.exists(PATH_DRIZZLE)
        return True


    def printmessage(self, message, message2=None):
        self.ui.label.setText(message)
        if message2 is not None:
            self.ui.label_2.setText(message2)
