import os
import sys
import zipfile

from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QFileDialog

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

    @pyqtSlot(str)
    def archive_directory(self, dir_path):
        if dir_path:
            dir_name = os.path.basename(dir_path)
            zip_file_path = os.path.splitext(dir_path)[0] + ".zip"
            with zipfile.ZipFile(zip_file_path, "w") as zip_file:
                for root, dirs, files in os.walk(dir_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arc_path = os.path.join(dir_name, os.path.relpath(file_path, dir_path))
                        zip_file.write(file_path, arcname=arc_path)
            return zip_file_path
        return ""


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
