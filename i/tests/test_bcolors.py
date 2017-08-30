# Lol what?
import unittest
from ..i import bcolors

class BcolorsTestCase(unittest.TestCase):
    def test_colors(self):
        assert isinstance(bcolors.HEADER, str)
        assert isinstance(bcolors.OKBLUE, str)
        assert isinstance(bcolors.OKGREEN, str)
        assert isinstance(bcolors.WARNING, str)
        assert isinstance(bcolors.FAIL, str)
        assert isinstance(bcolors.ENDC, str)
        assert isinstance(bcolors.BOLD, str)
        assert isinstance(bcolors.UNDERLINE, str)
