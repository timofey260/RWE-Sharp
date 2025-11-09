import sys

from PySide6.QtCore import QThread, Qt
from PySide6.QtWidgets import QProgressDialog
import os
import subprocess
from RWESharp.info import PATH_LEVELS, PATH_DRIZZLE, ISWIN

drizzle = os.path.join(PATH_DRIZZLE, "Drizzle.ConsoleApp.exe" if ISWIN else "Drizzle.ConsoleApp")
levelrenderstack = []

class LevelRenderer:
    @staticmethod
    def render_level(level_path: str):
        path, name = os.path.split(level_path)
        dialog = QProgressDialog(f"Rendering level {name}", "Abort", 0, 1)
        dialog.show()

        codethread = LevelRenderer.RenderProcess(level_path, dialog, len(levelrenderstack))
        levelrenderstack.append(codethread)  # battling python's garbage collection
        codethread.start()


    class RenderProcess(QThread):
        def __init__(self, level, dialog: QProgressDialog, stackindex):
            super().__init__()
            self.level = level
            self.dialog = dialog
            self.stackindex = stackindex

        def run(self, /):
            proc = subprocess.Popen([drizzle, "render", self.level],
                                    stdout=subprocess.PIPE,
                                    executable=drizzle)
            self.dialog.canceled.connect(proc.terminate)
            while True:
                char = proc.stdout.readline()
                decoded = char.decode()
                self.dialog.setLabelText(decoded)
                print(decoded)
                if not char:
                    self.quit()
                    levelrenderstack.pop(self.stackindex)
                    return


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    app = QApplication()
    LevelRenderer.render_level(os.path.join(PATH_LEVELS, "HE_LEG.txt"))
    sys.exit(app.exec())
