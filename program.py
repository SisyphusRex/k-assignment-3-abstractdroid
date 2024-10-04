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

    choice = my_ui.print_main_menu()
    match int(choice):
        case 0:
            # create a droid
            choice = my_ui.print_droid_type_menu(my_master.droid_type_names)
            # match int(choice):
            #     case 0:
            #         # astromech
            #         ...
            #     case 1:
            #         # janitor
            #         ...
            #     case 2:
            #         # protocol
            #         material = my_ui.print_choice_menu(material_list, "Material")
            #         color = my_ui.print_choice_menu(color_list, "Color")
            #         number_of_languages = int(my_ui.get_quantity("Languages"))
            #         user_protocol = Protocol(material, color, number_of_languages)
            #         user_protocol.calculate_total_cost()
            #         print(user_protocol)
            #     case 3:
            #         # utility
            #         ...

        case 1:
            # print the list of droids
            my_ui.print_collection(my_collection)

        case 2:
            sys.exit()
