"""This file holds the utility module"""

# Walter Podewil
# CIS 226
# October 2, 2024

# System Imports
import pathlib
import importlib.util
import importlib
import inspect
import sys

# First Party Imports

# Third Party Imports


class Utilities:
    """This Class contains methods for dynamically finding droid modules and parameters in a directory"""

    def find_droid_types(self, input_path: str) -> list:
        """Finds droid files and adds droid names to list"""
        droid_type_names = []
        # pathlib.Path().glob() returns a list of files with .py extension in input_path directory
        for source_file in pathlib.Path(input_path).glob("*.py"):
            # .stem returns filename without file extension
            name = source_file.stem
            # .spec_from_file_location creates a modulespec object of the file
            # a modulespec object contains information about a module used to load it
            spec = importlib.util.spec_from_file_location(name, source_file)
            # .module_from_spec creates a module based on the spec created
            mod = importlib.util.module_from_spec(spec)
            # .loader.exec_module executes the module in own namespace
            spec.loader.exec_module(mod)
            # now that the module is loaded, we can check the module for the attribute we are looking for
            if hasattr(mod, "DROID_TYPE_NAME"):
                droid_type_names.append(getattr(mod, "DROID_TYPE_NAME"))
        return droid_type_names

    def format_name_to_path(self, droid_name: str, droid_directory_path: str):
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
        # I store the parameters in a dict for easy call back later with only the key
        return droid_constructor_parameters

    def import_module_and_create_class_object(
        self, droid_name: str, droid_directory_path: str
    ) -> object:
        """This method imports the module and creates an object of the class"""

        # first we import the module from the file
        droid_module = importlib.import_module(
            self.format_name_to_path(droid_name, droid_directory_path)
        )
        # then we get an object of the class within the module using the module and class name
        class_object = getattr(droid_module, droid_name.capitalize())
        return class_object

    def find_name_of_new_qualitative_lists(self, droid_object: object) -> list:
        """this method finds lists of qualitative droid options in class files"""
        # TODO: I want this method to take in the droid_object that the user wants to create and look in its class file
        # and the files of its parent (super) classes for hardcoded constant dicts that refer to the different variants and
        # relative costs of a new droid option.
        # For example, lets say I want to give the Battle droids lightsaber various colors to choose from
        # Inside of the battle.py and the Battle class, I will define a constant variable, a dict, called LIGHTSABER_COLORS
        # and populate it with various colors and their costs.
        # I want this method to find that dict without me hardcode importing the module on the program.py

        # HINT: I think I will have success in this method if I create a naming scheme similar to the one I used for scanning files
        # for DROID_TYPE_NAME.  Perhaps every qualitative dictionary should be <insert parameter here>_QUALITATIVE_DICT.
        # If they all have the same structure, when my program.py file gets a string parameter, such as lightsaber_colors it will raise the name case and
        # concatenate _QUALITATIVE_DICT .  the result will be LIGHTSABER_COLORS_QUALITATIVE_DICT.  Then, the program can easily
        # access the dict by using droid_object.LIGHTSABER_COLORS_QUALITATIVE_DICT.
        # If all the dicts have the same name structure, then when programs.py makes a property call through
        # droid_object.<instert_parameter>_QUALITATIVE_DICT, regardless of in what class or file the dict exists, inheritance
        # will allow me to access it.

        # HINT2: Perhaps I do not need to scan the classes for dicts, but instead examine the parameter in the program.py file
        # and try to make a property call if it refers to a qualitative option stored in a dict.

    def __get_dict_name_from_parameter(
        self, parameter_name: str, dict_suffix: str
    ) -> str:
        """adds dict suffix to paramter name and returns dict name"""
        dict_name = parameter_name.upper() + dict_suffix
        return dict_name

    def get_dict_from_str(
        self, droid_object: object, parameter_name: str, dict_suffix: str
    ) -> dict:
        """Returns the dict on which parameter is based"""
        try:
            options_dict = getattr(
                droid_object,
                self.__get_dict_name_from_parameter(parameter_name, dict_suffix),
            )
        except AttributeError:
            sys.exit(
                f"The dict for this qualititative attribute -{parameter_name}- does not exist or is misspelled.  Examine the droid module.\n"
                "The dict in the class must have the DICT_SUFFIX to be read.\n"
                f"You are missing: {parameter_name.upper()}{dict_suffix} in the module."
            )
        return options_dict
