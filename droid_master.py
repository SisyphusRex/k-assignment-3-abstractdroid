"""This file holds the droid master class"""

# Walter Podewil
# CIS 226
# October 2, 2024

# System Imports
import os
import pathlib
import importlib.util
import importlib

# First Party Imports

# Third Party Imports


class DroidMaster:
    """The Purpose of this class is to find all of the creatable droid types and their relative creation methods"""

    def __init__(self):
        self.droid_type_names = []

    def find_droid_types(self, input_path: str) -> list:
        """Finds droid files and adds droid names to list"""
        droid_type_names = []
        for source_file in pathlib.Path(input_path).glob("*.py"):
            # .stem returns filenam without file extension
            name = source_file.stem
            # .spec_from_file_location creates a modulespec object of the file
            spec = importlib.util.spec_from_file_location(name, source_file)
            # .module_from_spec creates a module based on the spec created
            mod = importlib.util.module_from_spec(spec)
            # .loader.exec_module executes the module in own namespace
            spec.loader.exec_module(mod)
            if hasattr(mod, "DROID_TYPE_NAME"):
                droid_type_names.append(getattr(mod, "DROID_TYPE_NAME"))
            return droid_type_names

    def format_name_to_path(self, droid_name, droid_directory_path):
        file_name = droid_name.lower()
        path_name = droid_directory_path("\\", ".")
        return f"{path_name}{file_name}"

    def dict_to_list(self, input_dict: dict) -> list:
        """Converts dict to list of keys"""
        my_list = []
        for key in input_dict:
            my_list.append(key)
        return my_list
