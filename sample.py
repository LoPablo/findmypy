from findmypy.base import findpy_manager
from findmypy.base import findpy_connection
import os
from dotenv import load_dotenv

load_dotenv()

test_connection = findpy_connection(os.getenv('APPLEID'),os.getenv('PASSWORD'))
test = findpy_manager(test_connection, True)
test.init_devices_list()
print(test.devices)

