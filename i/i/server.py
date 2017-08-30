# class Server:
#     def __init__(self, name, ip, location=None):
#         if "@" not in ip:
#             raise ValueError("ip argument must contain username and ip, e.g.: pi@123.456.789")
#         self.name = name
#         self.username = self._get_username(ip)
#         self.ip = self._get_ip(ip)
#         self.location = location

#     def _get_username(self, ip):
#         return ip.split("@")[0]

#     def _get_ip(self, ip):
#         return ip.split("@")[1]

#     def json_encode(self):
