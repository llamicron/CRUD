import unittest
import json
import os
from ..i.i import I

class ITestCase(unittest.TestCase):
    def setUp(self):
        self.i = I(
            file = os.path.expanduser("~") + "/.i.test"
        )

    def test_has_storage_file(self):
        assert isinstance(self.i.file, str)
        assert os.path.isfile(self.i.file)

    # def test_file_is_created_on_object_creation(self):
    #     if os.path.isfile(self.i.file):
    #         os.remove(self.i.file)
    #     self.i = I()
    #     assert os.path.isfile(self.i.file)

    def test_store_server_list(self):
        assert self.i.server_list
        assert self.i.store_server_list()

    def test_load_server_list_from_file(self):
        assert isinstance(self.i.server_list, list)
