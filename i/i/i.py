#!/Users/llamicron/python_env/bin/python
import os
import json
from terminaltables import AsciiTable

class I:

    def __init__(self, file = None):
        if not file:
            self.file = os.path.expanduser("~") + "/.i"
        else:
            self.file = file

        self._create_file()

        self.server_list = self.get_server_list()

    def _create_file(self):
        if not os.path.isfile(self.file):
            open(self.file, "w+")
            return True
        return False

    def get_server_list(self):
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
            return data
        except ValueError:
            return []

    def store_server_list(self):
        with open(self.file, "w") as file:
            json.dump(self.server_list, file, indent = 2)
        return True

    def server_table(self):
        table_data = [
            ["Name", "Address", "Location"]
        ]
        for server in self.server_list:
            row = [
                server['name'],
                server['username'] + "@" + server['ip'],
            ]
            if server['location']:
                row.append(server['location'])
            else:
                row.append("")
            table_data.append(row)
        return AsciiTable(table_data)

    def find(self, find):
        for server in self.server_list:
            if find in server['name']:
                table_data = [["Name", "Address", "Location"]]
                row = [
                    server["name"],
                    server["username"] + "@" + server['ip']
                ]
                if server['location']:
                    row.append(server['location'])
                table_data.append(row)
                return AsciiTable(table_data)
        return AsciiTable([["Name", "Address", "Location"]])
