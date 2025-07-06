import subprocess
import sys
import os
import io
import re
from PySide6.QtWidgets import QProgressDialog, QApplication
from PySide6.QtCore import QThread

# package manager to download mods(kinda)
class LoadThread(QThread):
    def __init__(self, dialog):
        super().__init__()
        self.dialog = dialog

    def run(self, /):
        proc = subprocess.Popen([sys.executable, '-m', 'pip', 'install', "--progress-bar=raw", "-U", "pyside6"], stdout=subprocess.PIPE)
        while True:
            char = proc.stdout.readline()
            if not char:
                break
            string = char.decode()
            m = re.match(r"Progress (\d+) of (\d+)", string)
            if m is not None:
                val, total = int(m.group(1)), int(m.group(2))
                self.dialog.setValue(int(val * 100 / total))
            print(string, end="")

app = QApplication()
dialog = QProgressDialog("installing shit", "cancel", 0, 100)
dialog.setValue(50)
load = LoadThread(dialog)
load.start()

load.start()
app.exec()
