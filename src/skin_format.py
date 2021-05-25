import yaml_loader as yl


def dictobj(name, value):
    return {"name": str(name),
            "value": value
            }


class Skin:
    # Reference: https://taehui.ddns.net/bbs/board.php?bo_table=rtfm&wr_id=3
    #            (Korean)

    def __init__(self):
        # Initialize
        self.name = ""
        self.resource = ""
        self.luafile = ""
        self.skin_size = dict()
        self.skin_size_blank = False

        self.frame = []
        self.framerate = []
        self.color = []
        self.pipeline = []
        self.drawing = []
        self.input_mode = []
        self.function = []
        self.font = []

    def importYAML(self, yamlfile):
        # Check type
        if not isinstance(yamlfile, yl.YAMLFile):
            raise TypeError

        # Load header
        self.name = yamlfile.file_name
        self.resource = yamlfile.header["zip"]
        self.luafile = yamlfile.header["lua"]
        try:
            self.skin_size = {
                "length": yamlfile.header["default-length"],
                "height": yamlfile.header["default-height"]
            }
        except KeyError:
            self.skin_size = {
                "length": 1280,
                "height": 720
            }
            self.skin_size_blank = True

        # Load numbers of frames and framerates
        for value_name in yamlfile.frame:
            obj_name = value_name.replace('-', '_')
            if value_name.endswith("framerate"):
                obj_name = obj_name.replace('_framerate', '')
                self.framerate.append(dictobj(obj_name,
                                              yamlfile.frame[value_name]))
            elif value_name.endswith("frame"):
                obj_name = obj_name.replace('_frame', '')
                self.frame.append(dictobj(obj_name,
                                          yamlfile.frame[value_name]))

        # Load colors (paint)
        for value_name in yamlfile.paint:
            self.color.append(dictobj(value_name.replace('-', '_'),
                                      yamlfile.paint[value_name]))

        # Load styles in playing (function)
        for value_name in yamlfile.function:
            # Render order(pipeline)
            if value_name.endswith("pipeline"):
                pipelines_str = str(yamlfile.function[value_name])
                pipelines_list = []
                for obj_num in pipelines_str.split(","):
                    pipelines_list.append(int(obj_num))
                del pipelines_str
                self.pipeline.append(
                    dictobj(value_name.replace('-', '_'), pipelines_list))
                del pipelines_list

            # Key style number configure
            elif value_name.startswith("ui-drawing-"):
                img_num = int(value_name.split('-')[-1])
                input_num = str(yamlfile.function[value_name]).split(",")
                self.drawing.append({"num": img_num,
                                     "target": input_num})

            # Order key style by each Key modes
            elif value_name.startswith("ui-input-mode-"):
                mode_num = int(value_name.split('-')[-1])
                order_num = str(yamlfile.function[value_name]).split(",")
                self.input_mode.append({"mode": mode_num,
                                        "target": order_num})

            else:
                value = yamlfile.function[value_name]
                try:
                    int(value)
                except ValueError:
                    pass
                else:
                    value = int(value)

                try:
                    float(value)
                except ValueError:
                    pass
                else:
                    value = float(value)
                self.function.append(dictobj(value_name.replace('-', '_'),
                                             yamlfile.function[value_name]))

        # Load styles in playing (function)
        for value_name in yamlfile.font:
            self.font.append(dictobj(value_name.replace('-', '_'),
                                     yamlfile.font[value_name]))

    def exportYAML(self):
        # Header
        header = {"zip": self.resource, "lua": self.luafile}
        if not self.skin_size_blank:
            header["default-length"] = self.skin_size["length"]
            header["default-height"] = self.skin_size["height"]

        # Frames and framerates
        # Initialize for frames and framerates list
        frame = {}

        # Frames
        for eatch_object in self.frame:
            key_name = (eatch_object["name"] + "-frame").replace('_', '-')
            frame[key_name] = eatch_object["value"]

        # Framerates
        for eatch_object in self.framerate:
            key_name = (eatch_object["name"] + "-framerate").replace('_', '-')
            frame[key_name] = eatch_object["value"]

        # Paint
        # Initialize for paint list
        paint = {}

        # From color to YAML Paint
        for eatch_object in self.color:
            key_name = eatch_object["name"].replace('_', '-')
            paint[key_name] = eatch_object["value"]

        # Function
        # Initialize for style(function) list
        skin_func = {}

        # For debug
        print(header)
        print(frame)
        print(paint)


# For test
if __name__ == '__main__':
    example_file_path = "../skin/Default.yaml"
    file_object = yl.YAMLFile()
    file_object.load(example_file_path)
    example_skin = Skin()
    example_skin.importYAML(file_object)

    # Debug Data
    print("="*20)
    print("Name:", example_skin.name)
    print("Resource Zip:", example_skin.resource)
    print("Lua Script:", example_skin.luafile)
    print("")
    print("Frames of each objects")
    print(example_skin.frame)
    print("")
    print("Framerate of each objects")
    print(example_skin.framerate)
    print("")
    print("Color")
    print(example_skin.color)
    print("")
    print("Pipeline")
    print(example_skin.pipeline)
    print("")
    print("Drawing")
    print(example_skin.drawing)
    print("")
    print("Key Sets")
    print(example_skin.drawing)
    print("")
    print("Functions")
    print(example_skin.function)
    print("")
    print("")
    print("Exporting...")
    example_skin.exportYAML()
