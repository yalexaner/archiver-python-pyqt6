import os
import zipfile

from PyQt6.QtCore import QRunnable


class ArchiverWorker(QRunnable):

    def __init__(self, zip_file_path, selected_paths, archive_progress):
        super().__init__()
        self.zip_file_path = zip_file_path
        self.selected_paths = selected_paths

        self.archiveProgress = archive_progress
        self.archived_file_count = 0
        self.total_file_count = count_files(selected_paths)

    def run(self):
        for path in self.selected_paths:
            if os.path.isfile(path):
                self.archive_file(path)
            else:
                self.archive_directory(path)

    def archive_file(self, file_path):
        if not file_path:
            return

        with zipfile.ZipFile(self.zip_file_path, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zip_file:
            filename = os.path.basename(file_path)
            zip_file.write(file_path, arcname=filename)
            self.update_file_count_and_emit_progress()

    def archive_directory(self, dir_path):
        if not dir_path:
            return

        dir_name = os.path.basename(dir_path)
        with zipfile.ZipFile(self.zip_file_path, "a", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zip_file:
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    arc_path = os.path.join(dir_name, os.path.relpath(file_path, dir_path))
                    zip_file.write(file_path, arcname=arc_path)
                    self.update_file_count_and_emit_progress()

    # noinspection PyUnresolvedReferences
    def update_file_count_and_emit_progress(self):
        self.archived_file_count += 1

        progress: float = (self.archived_file_count / self.total_file_count) * 100
        self.archiveProgress.emit(progress)


def count_files(file_list):
    total_files = 0
    for item in file_list:
        if os.path.isfile(item):
            total_files += 1
        elif os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                total_files += len(files)
    return total_files
