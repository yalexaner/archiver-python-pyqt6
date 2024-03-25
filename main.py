import os
import sys
import zipfile

from PyQt6.QtCore import QObject, pyqtSlot
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication, QFileDialog


class Backend(QObject):
    @pyqtSlot(result=str)
    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select File", "", "All Files (*)")
        return file_path

    @pyqtSlot(str)
    def archive_file(self, file_path):
        if file_path:
            zip_file_path = os.path.splitext(file_path)[0] + ".zip"
            with zipfile.ZipFile(zip_file_path, "w") as zip_file:
                zip_file.write(file_path, os.path.basename(file_path))
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
