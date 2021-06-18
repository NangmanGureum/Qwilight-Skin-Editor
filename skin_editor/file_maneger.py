import datetime
import os
import zipfile
import file_loader as fl
import skin_format as skfmt
import skin_converter as sc


def mkdir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError as e:
        print('Error: ' + str(e))


def new_file(filename, data):
    f = open(filename, 'w', encoding='utf-8')
    f.write(data)
    f.close()


def resource_unzip(zip_path: str, res_dir_path: str):
    res_zip = zipfile.ZipFile(zip_path)
    res_zip.extractall(res_dir_path)


def resource_path(path: str, target: str, state: str, frame: int = 0):
    obj = {
        "path": path,
        "target": target,
        "state": state,
        "frame": frame
    }

    if not frame == 0:
        obj["frame"] = frame

    return obj


def today_str():
    today_date = datetime.datetime.today()
    today_date_str = today_date.strftime('%Y%m%d')

    return today_date_str


def new_project(path, project_info):
    if not isinstance(project_info, dict):
        raise TypeError

    # Make New Data
    project_name = project_info["name"]
    today = today_str()

    skin_data = skfmt.Skin()
    skin_data.name = project_name
    skin_data.description = project_info["desc"]
    skin_data.author = project_info["author"]
    skin_data.start_date = today
    skin_data.final_date = today

    # Make Project Directory
    mkdir("%s/%s" % (path, project_name))
    mkdir("%s/%s/Resources" % (path, project_name))

    # More data and data to Json
    skin_data.dir_resource = "./Resources"
    skin_json = skin_data.export_json()

    # Make format file
    new_file("%s/%s/format.json" % (path, project_name), skin_json)


def conv_to_project(yaml_path: str, save_path: str):
    # YAML File Object
    yaml_file = fl.YAMLSkinFile()
    yaml_file.open(yaml_path)

    # Convert To Skin
    yaml_project = sc.yaml_to_project(yaml_file, today_str())

    # Project name
    project_name = yaml_project.name

    # Make Project Directory
    mkdir("%s/%s" % (save_path, project_name))
    mkdir("%s/%s/Resources" % (save_path, project_name))

    # More data and data to Json
    yaml_project.dir_resource = "./Resources"
    # skin_json = yaml_project.export_json()
    skin_json = "wait...."

    # Make format file
    new_file("%s/%s/format.json" % (save_path, project_name), skin_json)

    # Unzip Resource
    res_zip_path = yaml_file.file_path + yaml_project.resource + ".zip"
    resource_unzip(res_zip_path, "%s/%s/Resources" % (save_path, project_name))

    # Add Resource files' path in the object
    res_dir = "%s/%s/%s" % (save_path, project_name, "Resources")
    res_dir_list = os.listdir(res_dir)

    # Add resources' path in the skin
    for dir_name in res_dir_list:
        dir_path = "%s/%s" % (res_dir, dir_name)
        dir_files = os.listdir(dir_path)

        for file_name in dir_files:
            file_path = dir_path + "/" + file_name
            file_name_wo_extn = file_name.split(".")[0]

            path_in_project = "%s/%s" % (dir_name, file_name)

            if dir_name == "Pause":
                yaml_project.path_resources.insert(
                    resource_path(path_in_project, "pause", file_name_wo_extn)
                )
            else:
                file_name_split = file_name_wo_extn.split(" ")

                if file_name_split[0] == "JM":
                    yaml_project.path_resources.insert(
                        resource_path(path_in_project,
                                      "accurate_margin_num", file_name_split[1])
                    )
                elif file_name_split[0] == "HC":
                    yaml_project.path_resources.insert(
                        resource_path(path_in_project,
                                      "max_combo_num", file_name_split[1])
                    )
                elif file_name_split[0] == "IS":
                    yaml_project.path_resources.insert(
                        resource_path(path_in_project,
                                      "stroke_per_sec_num", file_name_split[1])
                    )
                elif file_name_split[0] == "A":
                    yaml_project.path_resources.insert(
                        resource_path(path_in_project,
                                      "music_speed", file_name_split[1])
                    )
                elif file_name_split[0] == "B":
                    yaml_project.path_resources.insert(
                        resource_path(path_in_project,
                                      "bpm_num", file_name_split[1])
                    )
                elif file_name_split[0] == "C":
                    try:
                        frame_num = int(file_name_split[2])
                    except IndexError:
                        frame_num = None
                    if frame_num:
                        yaml_project.path_resources.insert(
                            resource_path(path_in_project,
                                          "combo_num", file_name_split[1],
                                          frame=frame_num)
                        )
                    else:
                        yaml_project.path_resources.insert(
                            resource_path(path_in_project,
                                          "combo_num", file_name_split[1])
                        )
                elif file_name_split[0] == "H":
                    yaml_project.path_resources.insert(
                        resource_path(path_in_project,
                                      "life_num", file_name_split[1])
                    )


# For test
if __name__ == '__main__':
    # conv_to_project("../skin/Default.yaml", "../test_skin")
    conv_to_project("CRs_simple_skin_1.6/CR_simple.yaml", "test_skin")

"""
if __name__ == '__main__':
    test_name = input("Enter New Project Name: ")
    test_desc = input("Enter the Description of New Project: ")
    test_author = input("Enter New Project Author: ")

    test_skin_info = {
        "name": test_name,
        "desc": test_desc,
        "author": test_author
    }
    new_project("../test_skin", test_skin_info)
"""
