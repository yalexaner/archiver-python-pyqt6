import os
import sys
from datetime import datetime

from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QFileDialog

from archiver.archiver import archive_file, archive_directory

selectedPaths = []


class Backend(QObject):
    selectedFilesChanged = pyqtSignal(list)

    @pyqtSlot()
    def open_file_dialog(self):
        global selectedPaths

        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.ViewMode.List)

        paths, _ = dialog.getOpenFileNames(None, "Select File", "", "All Files (*)")
        for path in paths:
            if path not in selectedPaths:
                selectedPaths.append(path)

        self.selectedFilesChanged.emit(selectedPaths)

    @pyqtSlot()
    def open_dir_dialog(self):
        global selectedPaths

        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        dialog.setOption(QFileDialog.Option.ReadOnly, True)

        path = dialog.getExistingDirectory(None, "Select Directory")
        if path not in selectedPaths:
            selectedPaths.append(path)

        self.selectedFilesChanged.emit(selectedPaths)

    @pyqtSlot()
    def clear(self):
        selectedPaths.clear()
        self.selectedFilesChanged.emit(selectedPaths)

    @pyqtSlot()
    def archive_files(self):
        # generate archive name with current date and time
        zip_file_path = f"archive-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.zip"

        for file in selectedPaths:
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
