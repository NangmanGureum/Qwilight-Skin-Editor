import datetime
import os
import skin_format as skfmt


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


def new_project(path, project_info):
    if not isinstance(project_info, dict):
        raise TypeError

    # Make New Data
    project_name = project_info["name"]
    today_date = datetime.datetime.today()
    today_date_str = today_date.strftime('%Y%m%d')

    skin_data = skfmt.Skin()
    skin_data.name = project_name
    skin_data.description = project_info["desc"]
    skin_data.author = project_info["author"]
    skin_data.start_date = today_date_str
    skin_data.final_date = today_date_str

    # Make Project Directory
    mkdir("%s/%s" % (path, project_name))
    mkdir("%s/%s/Resources" % (path, project_name))

    # More data and data to Json
    skin_data.dir_resource = "./Resources"
    skin_json = skin_data.export_json()

    # Make format file
    new_file("%s/%s/format.json" % (path, project_name), skin_json)


# For test
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
