import unittest
import os
from create_repo import CreateRepo

class CreateRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = CreateRepo()

    def test_read_from_credentials_file(self):
        self.repo.delete_creds_file()
        assert self.repo.get_creds_from_file() == False
        self.repo.create_creds_file()
        self.repo.write_creds_to_file()
        assert self.repo.get_creds_from_file()

