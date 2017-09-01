import unittest
from ..i import seed_data

class SeedDataTestCase(unittest.TestCase):
    def test_good_servers(self):
        assert seed_data.servers

    def test_bad_servers(self):
        assert seed_data.bad_servers

    def test_extra_servers(self):
        assert seed_data.extra_servers
