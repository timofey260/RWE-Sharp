from RWESharp.ui.uiscripts.splash import Ui_Splash
from PySide6.QtWidgets import QSplashScreen
from RWESharp.Loaders.Loader import Loader
from RWESharp.utils import log


# from PySide6.QtCore import Slot
# from PySide6.QtMultimediaWidgets import QVideoWidget
# from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoFrame


class SplashDialog(QSplashScreen):
    def __init__(self, callback, parent=None):
        super().__init__(parent)
        # self.manager = manager
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

        self.loader = Loader(self)
        self.loader.finished.connect(callback)
        self.loader.finished.connect(self.loader.deleteLater)
        self.loader.finished.connect(self.close)
        self.loader.start()
        log("Loading...")
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

    def printmessage(self, message, message2=None):
        self.ui.label.setText(message)
        if message2 is not None:
            self.ui.label_2.setText(message2)
