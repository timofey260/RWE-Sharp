import traceback
import requests
import os
from RWESharp.utils import log
from RWESharp.info import ISMAC, ISWIN, ISLINUX, PATH, PATH_DRIZZLE
from PySide6.QtWidgets import QMessageBox, QProgressDialog
import zipfile
import urllib
import urllib.parse as parse

CONTENT_DRIZZLEINFO = "drizzleinfo"
CONTENT_DRIZZLELINK = "drizzle-link"

class RWESharpDatabase:
    def __init__(self, database_path):
        self.database_path = database_path
        self.database_prefix = os.path.dirname(database_path)
        self.path_drizzle = None
        self.made_connection = False
        self.content = None
        self.log(f"Using database prefix {self.database_prefix}")

    def connect(self) -> bool:
        self.log(f"Trying to get content of {self.database_path}")
        try:
            data = requests.get(self.database_path)
            if data.status_code != 200:
                self.log(f"Unknown status code({data.status_code})!", True)
                raise requests.exceptions.ConnectionError()

            content = data.json()
            self.made_connection = True
            self.log("Content recieved!")
            self.path_drizzle = parse.urljoin(self.database_prefix, content[CONTENT_DRIZZLEINFO])
            self.content = content


        except requests.exceptions.ConnectionError:
            self.log("Connection Error! Canceling", True)
            return False
        except requests.exceptions.Timeout:
            self.log("Timeout Error! Canceling", True)
            return False
        except:
            self.log("Unknown exception! Canceling", True)
            traceback.print_exc()
            return False
        return True

    def get_drizzle_link(self) -> str | None:
        self.log(f"Trying to get drizzle from {self.path_drizzle}")
        if self.path_drizzle is None:
            self.log("Drizzle path is not found!", True)
            return None

        try:
            data = requests.get(self.path_drizzle)
            if data.status_code != 200:
                self.log(f"Unknown status code({data.status_code})! Canceling", True)
                return None
            name = "windows" if ISWIN else "linux" if ISLINUX else "mac" if ISMAC else ""
            content: dict = data.json()
            link = content[CONTENT_DRIZZLELINK].get(name)
            if content[CONTENT_DRIZZLELINK].get(name) is None:
                text = "No Drizzle for your operating system detected!\nSorry but you have to build it from source :("
                self.log(text)
                message = QMessageBox()
                message.setIcon(QMessageBox.Icon.Critical)
                message.setText(text)
                message.setWindowTitle("Invalid Operating system")
                message.setStandardButtons(QMessageBox.StandardButton.Ok)
                message.exec()
                return None
            return link
        except:
            log("Unknown exception! Canceling", True)
            return None
        return None

    def install_drizzle_from_link(self, link) -> bool:
        if link is None:
            return False
        # Downloading
        self.log("Downloading Drizzle...")
        def getit(v1: int, v2: int, v3: int):
            print(
                f"\rDownloaded {v1}/{round(v3 / v2)} blocks, {round(v1 * v2 / 1_048_576)}mb/{round(v3 / 1_048_576)}mb",
                end="")
        filename, headers = urllib.request.urlretrieve(link, filename=os.path.join(PATH, "drizzle.zip"), reporthook=getit)
        print("")  # fix previous print
        self.log("Extracting Drizzle")
        with zipfile.ZipFile(filename) as file:
            os.makedirs(PATH_DRIZZLE, exist_ok=True)
            file.extractall(PATH_DRIZZLE)
        return True


    def log(self, message, error=False):
        log("[DATABASE] " + message, error)
