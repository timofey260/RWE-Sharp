from PySide6.QtCore import Slot
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QWidget


class FunnyVideo(QWidget):
    def __init__(self, manager, closeonfinish, url, title):
        super().__init__()
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.manager = manager
        self.video = QVideoWidget(self)
        self.audio = QAudioOutput(self)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.video)
        self.player.setAudioOutput(self.audio)
        self.player.setSource(url)  # reasons beyond
        self.closeonfinish = closeonfinish
        self.player.mediaStatusChanged.connect(self.frame)
        self.player.play()
        size = 250
        self.setMinimumSize(size, size)
        self.video.setMinimumSize(size, size)
        self.setWindowTitle(title)
        self.show()

    @Slot(QMediaPlayer.MediaStatus)
    def frame(self, status: QMediaPlayer.MediaStatus):
        if status == status.NoMedia or status == status.EndOfMedia:
            self.deleteLater()
            if self.closeonfinish:
                self.manager.application.app.exit()
