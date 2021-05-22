import os
import yaml


class YAMLFile():
    def __init__(self):
        # Initialize
        self.file_path = ""
        self.file_name = ""
        self.header = {}
        self.frame = {}
        self.paint = {}
        self.function = {}
        self.font = {}

    def road(self, file_name):
        # Open YAML file
        yaml_file = open(file_name, 'r', encoding='UTF8')

        # Load some stuffs from a file
        self.file_path = os.path.dirname(os.path.realpath(yaml_file.name))
        self.file_path += "\\"
        self.file_name = os.path.basename(yaml_file.name).split(".")[0]
        data = yaml.load(yaml_file, Loader=yaml.SafeLoader)

        # Delete raw file
        del yaml_file

        # Load some stuffs from YAML data of the file
        self.header = data["format"]
        self.frame = data["frame"]
        self.paint = data["paint"]
        self.function = data["function"]
        try:
            self.font = data["font"]
        except KeyError:
            self.font = dict()

        # Delete raw YAML data
        del data
