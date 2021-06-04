from skin_editor import file_loader as fl
import unittest


class LoadFileTest(self, TestCase):

    def setUp(self):
        pass

    def make_an_object(self):
        an_object = fl.YAMLSkinFile()

    def load_a_yaml_file(self):
        an_object = fl.YAMLSkinFile()

        an_object.open("test_skin/Test.yaml")
        skin_mode = an_object.for_game
        self.assertEqual(skin_mode, True)


if __name__ == '__main__':
    unittest.main()
