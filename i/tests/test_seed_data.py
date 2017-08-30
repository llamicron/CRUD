import unittest
from ..i import seed_data

class SeedDataTestCase(unittest.TestCase):
    def test_valid_list(self):
        assert seed_data.server_list
