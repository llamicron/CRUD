#!/Users/llamicron/python_env/bin/python
import os
import json
# from server import Server

class I:

    def __init__(self, file = None):
        if not file:
            self.file = os.path.expanduser("~") + "/.i"
        else:
            self.file = file
        self._create_file()

        self.server_list = self._get_server_list()

    def _create_file(self):
        if not os.path.isfile(self.file):
            open(self.file, "w+")
            return True
        return False

    def _get_server_list(self):
        with open(self.file, "r") as file:
            data = json.load(file)
        return data

    def store_server_list(self):
        with open(self.file, "w") as file:
            json.dump(self.server_list, file, indent = 2)
        return True
