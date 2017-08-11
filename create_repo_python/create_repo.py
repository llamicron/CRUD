from sys import argv
import os


class CreateRepo:
    def __init__(self):
        self.creds_file = os.path.expanduser("~") + "/.create_repo.conf"
        self.username = "test_username"
        self.password = "test_password"

    def get_creds_from_file(self):
        if os.path.isfile(self.creds_file):
            with open(self.creds_file) as file:
                return file.read()
        return False

    def delete_creds_file(self):
        if os.path.isfile(self.creds_file):
            os.remove(self.creds_file)
        return True

    def create_creds_file(self):
        if os.path.isfile(self.creds_file):
            return True
        else:
            open(self.creds_file, "w")
            return True

    def write_creds_to_file(self):
        self.create_creds_file()
        with open(self.creds_file, "w+") as file:
            file.truncate()
            file.write("username=%s" % self.username)
            file.write("password=%s" % self.password)
            return True
