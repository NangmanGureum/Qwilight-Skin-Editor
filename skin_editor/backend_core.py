from os import mkdir
from skin_editor.project_manager.make_dir_file import load_file_utf8, write_file, path_os
from skin_editor.project_object import skin_project as skin


def new_project(path: str, name: str):
    # Make a project directory
    mkdir(path, name)
    project_path = path_os(path, name)

    # Make directories in the project directory
    mkdir(project_path, "resource")
    new_skin = skin.Skin()


def save_project(project_path: str, file_name: str):
    if file_name.endswith(".qwsk"):
        file_name = file_name.replace(".qwsk", "")
    data = ""
    write_file(project_path, file_name, "qwsk", data)


def load_project(file_path: str):
    data = load_file_utf8(file_path)
