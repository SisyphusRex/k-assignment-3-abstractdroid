"""Program code"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports

# First Party Imports
from user_interface import UserInterface
from droid_collection import DroidCollection

# Third Party Imports


def main(*args):
    """Method to run program"""
    my_ui = UserInterface()
    my_collection = DroidCollection()
    choice = my_ui.print_main_menu()
    match int(choice):
        case 1:
            # create a droid
            choice = my_ui.print_droid_type_menu()
            match int(choice):
                case 1:
                    # Protocol
                    ...
                case 2:
                    # Utility
                    ...
                case 3:
                    # Janitor
                    ...
                case 4:
                    # Astromech
                    ...

        case 2:
            # print the list of droids
            my_ui.print_collection(my_collection)
