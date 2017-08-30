import unittest
import json
import os
import seed_data
from terminaltables import AsciiTable
from ..i.i import I

class ITestCase(unittest.TestCase):

    def setUp(self):
        self.i = I(
            file = os.path.expanduser("~") + "/.i.test"
        )
        # Populate server list with seed data
        self.i.server_list = seed_data.server_list
        self.i.store_server_list()

    def test_has_storage_file(self):
        assert isinstance(self.i.file, str)
        assert os.path.isfile(self.i.file)

    def test_default_storage_file(self):
        self.i = I()
        assert ".i" in self.i.file

    def test_store_server_list(self):
        assert self.i.store_server_list()

    def test_load_server_list_from_file(self):
        assert isinstance(self.i.server_list, list)
        # Clear the file
        with open(self.i.file, "w") as file:
            file.truncate(0)
        # server list should be empty
        assert not self.i.get_server_list()

    def test_server_table(self):
        table = self.i.server_table()
        assert isinstance(table, AsciiTable)
        assert "Name" in table.table
        assert "Address" in table.table
        assert "Location" in table.table
        assert "sween" in table.table
        assert "pi" in table.table

    def tearDown(self):
        os.remove(self.i.file)
