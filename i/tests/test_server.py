# import unittest
# from ..i.server import Server

# class ServerTestCase(unittest.TestCase):
#     def setUp(self):
#         self.server = Server("Brewpi", "pi@123.456.789")

#     def test_has_name(self):
#         assert isinstance(self.server.name, str)

#     def test_has_username(self):
#         assert isinstance(self.server.username, str)

#     def test_has_ip(self):
#         assert isinstance(self.server.ip, str)

#     def test_can_have_location(self):
#         server = Server("Brewpi", "pi@123.456.789", location = "Mad Ass")
#         assert "Mad Ass" in server.location

#     def test_json_encode(self):
#         assert json.loads(self.server.json_encode())
