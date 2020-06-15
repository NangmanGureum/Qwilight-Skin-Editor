import os
import yaml


class YAMLFile():

    def __init__(self, file_name):
        yaml_file = open(file_name, 'r')
        self.file_path = os.path.dirname(os.path.realpath(yaml_file.name))
        self.file_path += "\\"
        self.file_name = os.path.basename(yaml_file.name).split(".")[0]
        data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
        del yaml_file

        self.header = data["format"]
        self.frame = data["frame"]
        self.paint = data["paint"]
        self.function = data["function"]
        self.font = data["font"]

        del data
