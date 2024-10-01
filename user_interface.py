"""User Interface Class File"""

#Walter Podewil
#CIS 226
#October 1, 2024

#System Imports

#First Party Imports
from droid_collection import DroidCollection

#Third Party Imports

class UserInterface():
    """User Interface Class"""

    MAIN_MENU = ("Type the number of your choice:\n"
                 "1. Add a New Droid\n"
                 "2. Print Droid List")

    DROID_TYPE_MENU = ("What type of Droid would you like to create?\n"
                       "1. Protocol\n"
                       "2. Utility\n"
                       "3. Janitor\n"
                       "4. Astromech")

    def print_main_menu(self) -> str:
        """Prints Main Menu"""
        print(self.MAIN_MENU)
        user_input = input(">")
        return user_input

    def print_droid_type_menu(self) -> str:
        """Prints Droid Type Menu"""
        print(self.DROID_TYPE_MENU)
        user_input = input(">")
        return user_input

    def print_collection(self, collection: DroidCollection) -> None:
        """Prints Droid Collection"""


