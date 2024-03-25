import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("File Archiver")

    property var selectedFiles: []

    Connections {
        target: backend

        // noinspection JSUnusedGlobalSymbols
        function onSelectedFilesChanged(files) {
            // noinspection JSUndeclaredVariable
            selectedFiles = files
        }
    }

    Text {
        id: app

        text: "File Archiver"
        font.family: "Helvetica"
        font.pixelSize: 24

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignTop

        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.topMargin: 16
        anchors.leftMargin: 16
        anchors.rightMargin: 8
    }

    Rectangle {
        id: selectedFilesField
        anchors.top: app.bottom
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.topMargin: 16
        anchors.leftMargin: 8
        anchors.rightMargin: 8
        height: parent.height / 2
        color: "white"
        border.color: "black"
        border.width: 1
        radius: 10

        ListView {
            id: selectedFilesList
            anchors.fill: parent
            anchors.topMargin: 2
            anchors.bottomMargin: 2
            anchors.leftMargin: 4
            anchors.rightMargin: 4
            model: selectedFiles
            delegate: Text {
                text: modelData
                font.pixelSize: 14
                wrapMode: Text.WordWrap
                padding: 5
            }
            clip: true
        }

        Text {
            id: placeholder
            anchors.centerIn: parent
            text: "Nothing selected yet"
            font.pixelSize: 16
            visible: selectedFilesList.count === 0
        }
    }

    RoundButton {
        id: selectFileButton
        anchors.top: selectedFilesField.bottom
        anchors.right: selectedFilesField.right
        radius: 14
        font.pixelSize: 16
        // font.color: blue
        topPadding: 8
        bottomPadding: 8
        leftPadding: 16
        rightPadding: 16
        anchors.topMargin: 8
        text: "Select File"
        icon.source: "icons/file.svg"
        icon.color: "green"
        onClicked: {
            backend.open_file_dialog();
        }
    }

    RoundButton {
        id: selectDirectoryButton
        anchors.top: selectFileButton.top
        anchors.right: selectFileButton.left
        radius: 14
        font.pixelSize: 16
        anchors.rightMargin: 8
        topPadding: 8
        bottomPadding: 8
        leftPadding: 16
        rightPadding: 16
        text: "Select Directory"
        icon.source: "icons/folder.svg"
        icon.color: "green"
        onClicked: {
            backend.open_dir_dialog();
        }
    }

    RoundButton {
        id: archiveButton
        anchors.top: selectedFilesField.bottom
        anchors.left: selectedFilesField.left
        radius: 14
        font.pixelSize: 16
        topPadding: 8
        bottomPadding: 8
        leftPadding: 16
        rightPadding: 16
        anchors.topMargin: 8
        text: "Archive all Selected"
        icon.source: "icons/archive.svg"
        icon.color: "green"
        enabled: selectedFiles.length > 0
        onClicked: {
            backend.archiveFiles();
        }
    }

    Button {
        id: clearSelectedFilesButton
        anchors.top: selectedFilesField.top
        anchors.right: selectedFilesField.right
        flat: true
        spacing: 1
        // radius: 14
        font.pixelSize: 12
        anchors.rightMargin: 8
        anchors.topMargin: 2
        hoverEnabled: true
        text: "clear"
        icon.source: "icons/clear.svg"
        icon.color: "red"
        icon.height: 16
        icon.width: 16
        onClicked: {
            backend.clear();
        }
    }
}
