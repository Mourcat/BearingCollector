import os
import sys

root_dir = os.path.split(os.path.abspath(sys.argv[0]))[0]
sys.path.insert(0, os.path.join(root_dir, "libs", "applibs"))

import json
import traceback 

from kivy.factory import Factory 
from bearingcollector import BearingCollector

__version__ = "1.0"

"""
Registering factories from factory.json.
"""
r = Factory.register

with open("factory_registers.json") as fd:
    custom_widgets = json.load(fd)
    for module, _classes in custom_widgets.items():
        for _class in _classes:
            r(_class, module=module)


try:
    BearingCollector().run()
except Exception:
    error = traceback.format_exc()

    """
    If the app encounters an error it automatically saves the
    error in a file called ERROR.log.
    You can use this for BugReport purposes.
    """
    with open("ERROR.log", "w") as error_file:
        error_file.write(error)

    print(error)
