"""This file holds the droid master class"""

# Walter Podewil
# CIS 226
# October 2, 2024

# System Imports
import os
import pathlib
import importlib.util
import importlib
import inspect

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
        """Takes droid name and directory path and returns droid file path"""
        file_name = droid_name.lower()
        path_name = droid_directory_path.replace("\\", ".")
        return f"{path_name}.{file_name}"

    def dict_to_list(self, input_dict: dict) -> list:
        """Converts dict to list of keys"""
        my_list = []
        for key in input_dict:
            my_list.append(key)
        return my_list

    def get_params(self, droid_object: object) -> dict:
        """This method accesses the parameters of the class constructor"""
        droid_constructor_parameters = {}
        constructor_parameters = inspect.signature(droid_object.__init__).parameters
        for name, parameters in constructor_parameters.items():
            if name != "self":
                my_str = str(parameters)
                param_name, param_type = my_str.split(": ")
                droid_constructor_parameters.update({param_name: param_type})

        return droid_constructor_parameters

    def import_module_and_create_class_object(
        self, droid_name: str, droid_directory_path: str
    ) -> object:
        """This method imports the module and creates an object of the class"""
        droid_module = importlib.import_module(
            self.format_name_to_path(droid_name, droid_directory_path)
        )
        class_object = getattr(droid_module, droid_name.capitalize())
        return class_object
