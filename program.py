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

# Third Party Imports


def main(*args):
    """Method to run program"""

    # I use a list here so that I can handle more droid types in the future
    # Ideally, there would be a function that creates the list of available droid types
    DROID_DIRECTORY = "DroidClasses\Creatable"
    my_master = DroidMaster()
    my_master.find_droid_types(DROID_DIRECTORY)
    my_ui = UserInterface()
    my_collection = DroidCollection()
    choice = my_ui.print_main_menu()
    match int(choice):
        case 0:
            # create a droid
            choice = my_ui.print_droid_type_menu(my_master.droid_type_names)

        case 1:
            # print the list of droids
            my_ui.print_collection(my_collection)

        case 2:
            sys.exit()
