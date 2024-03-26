import os
import zipfile

from PyQt6.QtCore import QRunnable


class ArchiverWorker(QRunnable):

    def __init__(self, zip_file_path, selected_paths):
        super().__init__()
        self.zip_file_path = zip_file_path
        self.selected_paths = selected_paths

    def run(self):
        for file in self.selected_paths:
            if os.path.isfile(file):
                archive_file(self.zip_file_path, file)
            else:
                archive_directory(self.zip_file_path, file)


def archive_file(zip_file_path, file_path):
    if not file_path:
        return

    with zipfile.ZipFile(zip_file_path, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zip_file:
        filename = os.path.basename(file_path)
        zip_file.write(file_path, arcname=filename)


def archive_directory(zip_file_path, dir_path):
    if not dir_path:
        return

    dir_name = os.path.basename(dir_path)
    with zipfile.ZipFile(zip_file_path, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zip_file:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                arc_path = os.path.join(dir_name, os.path.relpath(file_path, dir_path))
                zip_file.write(file_path, arcname=arc_path)
