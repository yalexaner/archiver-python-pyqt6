import os
import sys
from datetime import datetime

from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal, QThreadPool
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QFileDialog

from archiver.archive_worker import ArchiverWorker


class Backend(QObject):
    threadpool = QThreadPool()

    selectedPaths = []
    selectedFilesChanged = pyqtSignal(list)

    archiveProgress = pyqtSignal(float)
    archiveFileName = pyqtSignal(str)

    @pyqtSlot()
    def open_file_dialog(self):
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        dialog.setViewMode(QFileDialog.ViewMode.List)

        paths, _ = dialog.getOpenFileNames(None, "Select File", "", "All Files (*)")
        for path in paths:
            if path not in self.selectedPaths:
                self.selectedPaths.append(path)

        self.selectedFilesChanged.emit(self.selectedPaths)

    @pyqtSlot()
    def open_dir_dialog(self):
        dialog = QFileDialog()
        dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptOpen)
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        dialog.setViewMode(QFileDialog.ViewMode.List)
        dialog.setOption(QFileDialog.Option.ShowDirsOnly, True)
        dialog.setOption(QFileDialog.Option.ReadOnly, True)

        path = dialog.getExistingDirectory(None, "Select Directory")
        if path not in self.selectedPaths:
            self.selectedPaths.append(path)

        self.selectedFilesChanged.emit(self.selectedPaths)

    @pyqtSlot()
    def clear(self):
        self.selectedPaths.clear()
        self.selectedFilesChanged.emit(self.selectedPaths)

    # noinspection PyUnresolvedReferences
    @pyqtSlot()
    def archive_files(self):
        zip_file_path = f"archive-{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.zip"
        self.archiveFileName.emit(zip_file_path)

        worker = ArchiverWorker(zip_file_path, self.selectedPaths, self.archiveProgress)
        self.threadpool.start(worker)


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
