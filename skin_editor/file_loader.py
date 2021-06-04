import os
import pathlib
import yaml


class YAMLSkinFile():
    def __init__(self):
        pass

    def open(self, file_path):
        # Open the file
        self.file = open(file_path, 'r', encoding='UTF8')
        self.file_name = os.path.basename(self.file.name)
        self.file_path = os.path.dirname(self.file.name)

        # Windows / Mac
        os_name = os.uname().sysname
        if os_name == "Windows":
            self.file_path += "\\"
        elif os_name == "Linux" or os_name == "Darwin":
            self.file_path += "/"

        # Skin type check
        if self.file_name.startswith("@"):
            self.for_game = False
        else:
            self.for_game = True

        # Read Skin Data
        self.yaml_data = yaml.load(self.file, Loader=yaml.SafeLoader)

        self.full_info = {
            "file_name": self.file_name,
            "for_game": self.for_game,
            "data": self.yaml_data
        }


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

    def load(self, file_name):
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
