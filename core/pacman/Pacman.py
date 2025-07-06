import subprocess
import sys
import os
import io
import re
from PySide6.QtWidgets import QProgressDialog, QApplication
from PySide6.QtCore import QThread


class LoadThread(QThread):
    """
    package manager to download mods(kinda)
    """
    def __init__(self, dialog: QProgressDialog, app: QApplication):
        super().__init__()
        self.dialog = dialog
        self.app = app

    def run(self, /):
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', "--progress-bar=raw", "-U", "style"], stdout=subprocess.PIPE)
        while True:
            char = proc.stdout.readline()
            if not char:
                self.quit()
                self.dialog.hide()
                self.app.quit()
                return
            string = char.decode()
            m = re.match(r"Progress (\d+) of (\d+)", string)
            if m is not None:
                val, total = int(m.group(1)), int(m.group(2))
                self.dialog.setValue(int(val * 100 / total))
            else:
                self.dialog.setLabelText(string)
            print(string, end="")


app = QApplication()
dialog = QProgressDialog("installing shit", "cancel", 0, 100)
dialog.show()
dialog.canceled.connect(app.quit)
load = LoadThread(dialog, app)
load.start()

sys.exit(app.exec())
