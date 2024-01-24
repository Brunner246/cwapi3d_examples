import sys

print("sandbox start")

import utility_controller as uc

plugin_path = uc.get_plugin_path()

sys.path.append(plugin_path)

from Sandbox.TestObject import Display

Display()

print("sandbox end")


# or

# import sys
#
# print("sandbox start")
#
# import utility_controller as uc
#
# plugin_path = uc.get_plugin_path()
#
# sys.path.append(plugin_path)
#
# import Sandbox.TestObject
#
# Sandbox.TestObject.Display()
#
# print("sandbox end")