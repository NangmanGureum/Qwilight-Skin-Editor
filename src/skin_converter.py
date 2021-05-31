import file_loader as fl
import skin_format as sf


def dictobj(name, value):
    return {"name": str(name),
            "value": value
            }


def to_project(yaml_file: fl.YAMLSkinFile, today: str) -> sf.Skin:
    # New Obj
    project = sf.Skin()

    # Load Skin Info
    yaml_info = yaml_file.full_info
    yaml_data = yaml_info["data"]

    # Check Metadata
    try:
        yaml_meta = yaml_data["--editor__metadata"]
    except KeyError:
        project.name = yaml_info["file_name"]
        project.description = "Export By The Editor"
        project.author = ""
        project.start_date = today
        project.final_date = today
    else:
        project.name = yaml_meta["name"]
        project.description = yaml_meta["description"]
        project.author = yaml_meta["author"]
        project.start_date = yaml_meta["start_date"]
        project.final_date = yaml_meta["final_date"]

    # Skin Object Initialize

    # Skin Header
    project.resource = ""
    project.lua_script = ""
    project.skin_size = dict()
    project.skin_size_blank = False
    # Skin Data
    project.frame = []
    project.framerate = []
    project.color = []
    project.pipeline = []
    project.drawing = []
    project.input_mode = []
    project.function = []
    project.font = []

    # Load header
    project.resource = yaml_data.header["zip"]
    project.luafile = yaml_data.header["lua"]
    try:
        project.skin_size = {
            "length": yaml_data.header["default-length"],
            "height": yaml_data.header["default-height"]
        }
    except KeyError:
        project.skin_size = {
            "length": 1280,
            "height": 720
        }
        project.skin_size_blank = True
    # Load numbers of frames and framerates
    for value_name in yaml_data.frame:
        obj_name = value_name.replace('-', '_')
        if value_name.endswith("framerate"):
            obj_name = obj_name.replace('_framerate', '')
            project.framerate.append(dictobj(obj_name,
                                             yaml_data.frame[value_name]))
        elif value_name.endswith("frame"):
            obj_name = obj_name.replace('_frame', '')
            project.frame.append(dictobj(obj_name,
                                         yaml_data.frame[value_name]))
    # Load colors (paint)
    for value_name in yaml_data.paint:
        project.color.append(dictobj(value_name.replace('-', '_'),
                                     yaml_data.paint[value_name]))
    # Load styles in playing (function)
    for value_name in yaml_data.function:
        # Render order(pipeline)
        if value_name.endswith("pipeline"):
            pipelines_str = str(yaml_data.function[value_name])
            pipelines_list = []
            for obj_num in pipelines_str.split(","):
                pipelines_list.append(int(obj_num))
            del pipelines_str
            project.pipeline.append(
                dictobj(value_name.replace('-', '_'), pipelines_list))
            del pipelines_list
        # Key style number configure
        elif value_name.startswith("ui-drawing-"):
            img_num = int(value_name.split('-')[-1])
            input_num = str(yaml_data.function[value_name]).split(",")
            project.drawing.append({"num": img_num,
                                    "target": input_num})
        # Order key style by each Key modes
        elif value_name.startswith("ui-input-mode-"):
            mode_num = int(value_name.split('-')[-1])
            order_num = str(yaml_data.function[value_name]).split(",")
            project.input_mode.append({"mode": mode_num,
                                       "target": order_num})
        else:
            value = yaml_data.function[value_name]
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
            project.function.append(dictobj(value_name.replace('-', '_'),
                                            yaml_data.function[value_name]))
    # Load font size(font)
    for value_name in yaml_data.font:
        project.font.append(dictobj(value_name.replace('-', '_'),
                                    yaml_data.font[value_name]))
