import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("File Archiver")

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            id: selectedFileText
            text: "No file selected"
            font.pixelSize: 16
        }

        Text {
            id: archivedFileText
            text: ""
            font.pixelSize: 16
            color: "green"
        }

        Button {
            text: "Select File"
            onClicked: {
                const filePath = backend.open_file_dialog();
                if (filePath) {
                    selectedFileText.text = "Selected file: " + filePath
                    const archivedFilePath = backend.archive_file(filePath);
                    archivedFileText.text = "Archived file: " + archivedFilePath
                } else {
                    selectedFileText.text = "No file selected"
                    archivedFileText.text = ""
                }
            }
        }

        Button {
            text: "Select Directory"
            onClicked: {
                const dirPath = backend.open_dir_dialog();
                if (dirPath) {
                    const archivedFilePath = backend.archive_directory(dirPath);
                    archivedFileText.text = "Archived directory: " + archivedFilePath;
                } else {
                    archivedFileText.text = "";
                }
            }
        }
    }
}
