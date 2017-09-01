import unittest
import json
import os
import seed_data
import copy
from terminaltables import AsciiTable
from ..i.i import I

class ITestCase(unittest.TestCase):

    def setUp(self):
        self.i = I(
            file = os.path.expanduser("~") + "/.i.test"
        )
        # Populate server list with seed data
        self.i.servers = seed_data.servers
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
        assert isinstance(self.i.servers, list)
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

    def test_find_server(self):
        table = self.i.find("sween")
        assert isinstance(table, AsciiTable)
        assert "Name" in table.table
        assert "Address" in table.table
        assert "sween" in table.table
        assert "llaminator" not in table.table
        table = self.i.find("Not a server lol")
        assert "Name" in table.table
        assert "Address" in table.table
        assert "sween" not in table.table

    def test_server_validation(self):
        good_server = {
            "name": "a server name",
            "username": "pi",
            "ip": "123.456.789",
            "location": "Right here"
        }
        bad_server = {
            "name": "",
            "username": "no name",
            "ip": "123123",
            "location": "Over der"
        }

        assert self.i.validate(good_server)

        assert not self.i.validate(bad_server)

    def test_add_server(self):
        # Get some valid test server data
        good_server = copy.deepcopy(seed_data.servers[0])

        old_size = len(self.i.servers)

        self.i.add(good_server)
        assert len(self.i.servers) == old_size + 1

    def test_add_bad_server(self):
        # Get some valid test server data
        bad_server = copy.deepcopy(seed_data.bad_servers[1])

        assert not self.i.add(bad_server)

    def test_remove_server(self):
        server = copy.deepcopy(seed_data.extra_servers[0])
        old_size = len(self.i.servers)

        assert self.i.add(server)
        assert len(self.i.servers) == old_size + 1

        assert self.i.remove(server['name'])
        assert len(self.i.servers) == old_size


    def tearDown(self):
        os.remove(self.i.file)
