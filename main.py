import os
import sys
from datetime import datetime

from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QFileDialog

from archiver.archiver import archive_file, archive_directory

selectedFiles = []


class Backend(QObject):
    selectedFilesChanged = pyqtSignal(list)

    @pyqtSlot(result=str)
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select File", "", "All Files (*)")
        selectedFiles.append(file_path)
        self.selectedFilesChanged.emit(selectedFiles)
        return file_path

    @pyqtSlot(result=str)
    def open_dir_dialog(self):
        dir_dialog = QFileDialog()
        dir_dialog.setFileMode(QFileDialog.FileMode.Directory)
        dir_dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        dir_dialog.setOption(QFileDialog.Option.ReadOnly, True)

        dir_path = dir_dialog.getExistingDirectory(None, "Select Directory")
        selectedFiles.append(dir_path)
        self.selectedFilesChanged.emit(selectedFiles)
        return dir_path

    @pyqtSlot()
    def clear(self):
        selectedFiles.clear()
        self.selectedFilesChanged.emit(selectedFiles)

    @pyqtSlot()
    def archive_files(self):
        # generate archive name with current date and time
        zip_file_path = f"archive-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.zip"

        for file in selectedFiles:
            if os.path.isfile(file):
                archive_file(zip_file_path, file)
            else:
                archive_directory(zip_file_path, file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    qml_file = os.path.join(os.path.dirname(__file__), "main.qml")
    engine.load(qml_file)

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
