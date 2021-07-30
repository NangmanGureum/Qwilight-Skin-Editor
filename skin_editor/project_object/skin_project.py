class Skin():

    def __init__(self) -> None:
        # Refer to format.qwsk
        # .qwer stands for QWilight SKin

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

        
        """
