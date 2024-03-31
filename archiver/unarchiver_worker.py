import os
import zipfile

from PyQt6.QtCore import QRunnable


class UnzipWorker(QRunnable):

    def __init__(self, zip_file, unzip_status):
        super().__init__()
        self.zip_file = zip_file
        self.unzip_status = unzip_status

    def run(self):
        directory = self.zip_file.replace(".zip", "")
        directory = os.path.normpath(directory)

        if not os.path.exists(directory):
            os.mkdir(directory)
        else:
            self.unzip_status.emit("Directory already exists")
            return

        with zipfile.ZipFile(self.zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory)

        self.unzip_status.emit("Created directory " + directory)
