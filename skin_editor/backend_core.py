from os import mkdir
from skin_editor.project_manager.make_dir_file import write_file, path_os


def new_project(path: str, name: str):
    # Make a project directory
    mkdir(path, name)
    project_path = path_os(path, name)

    # Make directories in the project directory
    mkdir(project_path, "resource")


def save_project(project_path: str, file_name: str):
    if file_name.endswith(".qwsk"):
        file_name = file_name.replace(".qwsk", "")
    data = ""
    res_list = ""
    write_file(project_path, file_name, "qwsk", data)
    write_file(project_path, "res", "qwsr", res_list)
