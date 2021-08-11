class Skin():

    def __init__(self) -> None:
        # Refer to format.qwsk
        # .qwsk stands for QWilight SKin

        # Skin metadata
        self.title = str()
        self.description = str()
        self.author = str()

        self.first_date = {
            "year": int(),
            "month": int(),
            "day": int()
        }
        self.recent_date = {
            "year": int(),
            "month": int(),
            "day": int()
        }

        self.yaml_name = str()

        # Skin resource paths
        self.paths = {
            "resource_dir": "./resource",  # Initial Path
        }

        # Skin contents
        self.reference_size = {
            "width": 1280,
            "height": 720
        }
        self.framerate__main = 60
        self.framerate__specific = list()

        self.frame = list()
        """
        OBJECT NAME LIST
        
        - note
        - judgement
        - line
        - button
        - explose
        - comber_number
        - in_play_result
        """
        self.style = {
            "pipeline": [
                49, 1, 26, 3, 4, 7, 50, 8, 31, 102, 103, 100, 101, 2, 6, 9, 10, 11, 12, 13, 14, 30, 15, 16, 27, 28, 29, 33, 43, 44, 46, 47, 48
            ],
            "note": {
                "logn_note_edge": False,

            },
            "lines": {
                "modes": [
                    {
                        "mode": "1",
                        "line_num": []
                    },
                ]
            },
            "judge": {
                "setable_judgment_position": False,
            },
        }
