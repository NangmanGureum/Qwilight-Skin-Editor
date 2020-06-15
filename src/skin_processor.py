import yaml_loader as yl
import ez_version as v


def dictobj(name, value):
    return {"name": str(name),
            "value": value
            }

def ui_draw(ver, name):
    if v.isnewer(ver, "1.3.0"):


class Skin:

    def __init__(self):

        self.name = ""
        self.client_ver = v.ver("0.1")
        self.resource = ""
        self.luafile = ""

        self.frame = []
        self.framerate = []
        self.color = []
        self.render_order = []
        self.style = []
        self.drawing = []

    def load(self, yamlfile):
        if not isinstance(yamlfile, yl.YAMLFile):
            raise TypeError

        self.name = yamlfile.file_name
        self.client_ver = v.ver(yamlfile.header["date"])
        self.resource = yamlfile.header["zip"]
        self.luafile = yamlfile.header["lua"]

        # Load Number of frames and Framerates
        for value_name in yamlfile.frame:
            obj_name = value_name.split('-')[0]
            if value_name.endswith("framerate"):
                self.framerate.append(dictobj(obj_name,
                                              yamlfile.frame[value_name]))
            elif value_name.endswith("frame"):
                self.frame.append(dictobj(obj_name,
                                          yamlfile.frame[value_name]))

        for value_name in yamlfile.paint:
            if value_name != "default-faint":
                self.color.append(dictobj(value_name.replace('-', '_'),
                                          yamlfile.paint[value_name]))
            else:
                self.color.append(dictobj("legacy_"
                                          + value_name.replace('-', '_'),
                                          yamlfile.paint[value_name]))

        for value_name in yamlfile.function:
            if value_name == "pipeline":
                pipeline_str = str(yamlfile.function["pipeline"])
                for obj_num in pipeline_str.split(","):
                    self.render_order.append(int(obj_num))
                del pipeline_str

            elif value_name.startswith("ui-drawing-"):
                img_num = int(value_name.split('-')[-1])
                input_num = str(yamlfile.function[value_name]).split(",")
                self.drawing.append({"num": img_num,
                                     "target": input_num})


# For test
if __name__ == '__main__':
    example_file_path = "your_yaml_file_path"
    file_object = yl.YAMLFile(example_file_path)
    example_skin = Skin()
    example_skin.load(file_object)

    # Debug Data
    print("Name:", example_skin.name)
    print("Client Version for:", example_skin.client_ver)
    print("Resouse Zip:", example_skin.resource)
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
    print(example_skin.render_order)
    print("")
    print("Style")
    print(example_skin.style)
    print("Drawing")
    print(example_skin.drawing)
