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

    # Only returns strings!!!

    # Main menu and Droid Type are lists because I want the ability to handle more options in the future
    MAIN_MENU = ["Add New Droid", "Print Collection", "Exit"]

    def print_main_menu(self) -> str:
        """Prints Main Menu"""
        print("Type Selection Number:")
        for index, item in enumerate(self.MAIN_MENU):
            print(index, item)
        user_input = input(">")
        print()
        return user_input

    def print_droid_type_menu(self, droid_list: list) -> str:
        """Prints Droid Type Menu"""
        print("Type Selection Number:")
        for index, item in enumerate(droid_list):
            print(index, item)
        user_input = input(">")
        print()
        return user_input

    def print_collection(self, collection: DroidCollection) -> None:
        """Prints Droid Collection"""
        for droid in collection.collection:
            print(droid)
        print()

    def print_choice_menu(self, input_list: list, input_option: str) -> str:
        """Get Material For Droid method"""
        print(f"Type {input_option} Selection Number:")
        for index, item in enumerate(input_list):
            print(index, item)
        user_input_index = int(input(">"))
        print()
        user_input = input_list[user_input_index]
        return user_input

    def get_quantity(self, option: str) -> str:
        """gets number of option"""
        print(f"How many {option} do you want?")
        user_input = input(">")
        print()
        return user_input

    def get_yes_or_no(self, option: str) -> str:
        print(f"Add {option} to the droid?\n0 Yes\n1 No")
        user_input = input(">")
        return user_input
