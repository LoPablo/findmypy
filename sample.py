from findmypy.base import findMyPyManager
from findmypy.base import findMyPyConnection
import os
from dotenv import load_dotenv

load_dotenv()

test_connection = findMyPyConnection("steeve.cook@apple.com","super_secure_apple_password")
test = findMyPyManager(test_connection, True)
test.init_devices_list()
print(test.devices)

