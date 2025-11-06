import traceback

from PySide6.QtWidgets import QTabWidget
from PySide6.QtCore import Qt

class LevelTabs(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setMovable(True)
        self.manager = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        print("shit")
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event, /):
        print("shit2222")
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            from core.Level.RWELevel import RWELevel
            for i in links:
                try:
                    level = RWELevel(self.manager, i)
                    self.manager.open_level(level)
                except:
                    traceback.print_exc()
        else:
            event.ignore()