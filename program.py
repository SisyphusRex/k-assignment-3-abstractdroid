"""Program code"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
import sys

# First Party Imports
from user_interface import UserInterface
from droid_collection import DroidCollection
from droid_master import DroidMaster
from DroidClasses.ParentOnly.droid import Droid
import importlib
import inspect

# Third Party Imports


def main(*args):
    """Method to run program"""

    # I use a list here so that I can handle more droid types in the future
    # Ideally, there would be a function that creates the list of available droid types
    DROID_DIRECTORY = "DroidClasses\Creatable"

    my_master = DroidMaster()
    list_of_droid_types = my_master.find_droid_types(DROID_DIRECTORY)
    my_ui = UserInterface()
    my_collection = DroidCollection()
    color_list = my_master.dict_to_list(Droid.COLOR_COST)
    material_list = my_master.dict_to_list(Droid.MATERIAL_COST)

    main_choice = my_ui.print_main_menu()
    while int(main_choice) < 3:
        match int(main_choice):
            case 0:
                # create a droid
                choice = my_ui.print_droid_type_menu(list_of_droid_types)
                droid_name = list_of_droid_types[int(choice)]
                droid_object = my_master.import_module_and_create_class_object(
                    droid_name, DROID_DIRECTORY
                )
                parameter_dict = my_master.get_params(droid_object)
                my_dict = {}
                for key, value in parameter_dict.items():
                    if value == "bool":
                        # handle yes no option
                        choice = my_ui.get_yes_or_no(key)
                        if choice == "0":
                            my_dict.update({key: False})
                        if choice == "1":
                            my_dict.update({key: True})
                    if value == "int":
                        # hadle quanity options
                        quantity = int(my_ui.get_quantity(key))
                        my_dict.update({key: quantity})
                    if value == "str":
                        # handle qualitative options
                        if key == "color":
                            choice = my_ui.print_choice_menu(color_list, key)
                            my_dict.update({key: choice})
                        if key == "material":
                            choice = my_ui.print_choice_menu(material_list, key)
                            my_dict.update({key: choice})
                created_droid = droid_object(**my_dict)
                created_droid.calculate_total_cost()
                my_collection.add(created_droid)

            case 1:
                # print the list of droids
                my_ui.print_collection(my_collection)

            case 2:
                sys.exit()
        main_choice = my_ui.print_main_menu()
