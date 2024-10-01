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

    MAIN_MENU = (
        "Type the number of your selection:\n"
        "1. Add New Droid\n"
        "2. Print Collection"
    )

    DROID_TYPE_LIST = ["Protocol", "Utility", "Janitor", "Astromech"]

    def print_main_menu(self) -> str:
        """Prints Main Menu"""
        print(self.MAIN_MENU)
        user_input = input(">")
        return user_input

    def print_droid_type_menu(self) -> str:
        """Prints Droid Type Menu"""
        for index in range(len(self.DROID_TYPE_LIST)):
            print(f"{index:<3} {self.DROID_TYPE_LIST[index]}")
        user_input = input(">")
        return user_input

    def print_collection(self, collection: DroidCollection) -> None:
        """Prints Droid Collection"""
