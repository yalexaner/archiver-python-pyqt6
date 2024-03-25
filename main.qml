import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("File Selector")

    ColumnLayout {
        anchors.centerIn: parent
        spacing: 20

        Text {
            id: selectedFileText
            text: "No file selected"
            font.pixelSize: 16
        }

        Button {
            text: "Select File"
            onClicked: {
                var filePath = backend.open_file_dialog()
                if (filePath) {
                    selectedFileText.text = "Selected file: " + filePath
                } else {
                    selectedFileText.text = "No file selected"
                }
            }
        }
    }
}
