"""User Interface Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports

# First Party Imports
from droid_collection import DroidCollection

# Third Party Imports


class UserInterface:
    """User Interface Class"""

    # Main menu and Droid Type are lists because I want the ability to handle more options in the future
    MAIN_MENU = ["Add New Droid", "Print Collection", "Exit"]

    def print_main_menu(self) -> str:
        """Prints Main Menu"""
        print("Type Selection Number:")
        for index, item in enumerate(self.MAIN_MENU):
            print(index, item)
        user_input = input(">")
        return user_input

    def print_droid_type_menu(self, droid_list: list) -> str:
        """Prints Droid Type Menu"""
        print("Type Selection Number:")
        for index, item in enumerate(droid_list):
            print(index, item)
        user_input = input(">")
        return user_input

    def print_collection(self, collection: DroidCollection) -> None:
        """Prints Droid Collection"""
