import os
import zipfile


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
