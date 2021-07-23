import os
import platform


def path_os(path_1: str, path_2: str) -> str:
    os_name = platform.system()
    if os_name == "Linux" or os_name == "Darwin":  # For Linux or macOS
        path = "%s/%s" % (path_1, path_2)
    elif os_name == "Windows":  # For Windows
        path = "%s\\%s" % (path_1, path_2)

    return path


def mkdir(path: str, name: str):
    full_path = path_os(path, name)
    os.mkdir(full_path)


def write_file(path: str, name: str, f_ext: str, data):
    full_file_name = "%s.%s" % (name, f_ext)
    full_path = path_os(path, full_file_name)

    if isinstance(data, str):
        file = open(full_path, 'w', encoding='utf-8')
        file.write(data)
        file.close()
    else:
        file = open(full_path, "wb")
        file.write(data)
        file.close()


def load_file():
    print("asdf")
