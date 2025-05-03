from RWESharp.Modify import Mod, ModInfo
from PySide6.QtCore import QTimer
from discordrpc.presence import RPC as DRPC
from discordrpc.button import Button
import time
from RWESharp.Core import REPO, NAME, REPO_DOWNLOAD_LATEST


class RPC(Mod):
    def __init__(self, manager, path):
        super().__init__(manager, ModInfo.import_from_mod_path(path), path)
        self.timer = QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.change)
        self.timer.start()
        self.rpc = DRPC(1226198202454380677)
        self.start = time.time()
        # todo settings

    def change(self):
        button = Button("Github", REPO, "Download", REPO_DOWNLOAD_LATEST)
        self.rpc.set_activity(self.manager.selected_viewport.level.shortname, "Lediting", 0,
                              int(self.start), large_image="icon", large_text=NAME,
                              buttons=button)
