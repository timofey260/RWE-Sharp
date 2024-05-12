from ui.uiscripts.splash import Ui_Splash
from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtCore import Slot
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QVideoFrame

class SplashDialog(QDialog):
    def __init__(self, manager, parent=None):
        super().__init__(parent)
        self.manager = manager
        self.ui = Ui_Splash()
        self.ui.setupUi(self)

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