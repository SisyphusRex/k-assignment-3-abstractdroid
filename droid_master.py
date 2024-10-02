"""This file holds the droid master class"""

# Walter Podewil
# CIS 226
# October 2, 2024

# System Imports
import os
import pathlib
import importlib.util

# First Party Imports

# Third Party Imports


class DroidMaster:
    """The Purpose of this class is to find all of the creatable droid types and their relative creation methods"""

    def __init__(self):
        self.droid_type_names = []

    def find_droid_types(self, path: str) -> None:
        """Finds droid files and adds droid names to list"""
        for source_file in pathlib.Path(path).glob("*.py"):
            # .stem returns filenam without file extension
            name = source_file.stem
            # .spec_from_file_location creates a modulespec object of the file
            spec = importlib.util.spec_from_file_location(name, source_file)
            # .module_from_spec creates a module based on the spec created
            mod = importlib.util.module_from_spec(spec)
            # .loader.exec_module executes the module in own namespace
            spec.loader.exec_module(mod)
            if hasattr(mod, "DROID_TYPE_NAME"):
                self.__add_droid_name(getattr(mod, "DROID_TYPE_NAME"))

    def __add_droid_name(self, name: str) -> None:
        self.droid_type_names.append(name)
