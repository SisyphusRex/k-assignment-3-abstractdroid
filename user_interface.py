"""User Interface Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
import re
# First Party Imports
from droid_collection import DroidCollection
from colors import print_red
# Third Party Imports


class UserInterface:
    """User Interface Class"""

    # For uniformity and better interaction with other classes, this class is only concerned with three things:
    # 1. Printing to terminal
    # 2. getting user console input
    # 3. returning strings AND ONLY strings in its methods that have returns

    # Main menu and Droid Type are lists because I want the ability to handle more options in the future
    MAIN_MENU = ["Add New Droid", "Print Collection", "Exit"]

    def print_main_menu(self) -> str:
        """Prints Main Menu"""
        running = True
        while running:
            print("Type Selection Number:")
            # I use enumerate here rather than range(len(list[])) because it functions the same but simpler
            for index, item in enumerate(self.MAIN_MENU):
                print(index, item)
            user_input = input(">")
            print()
            running = self.__validate_list_input(user_input, self.MAIN_MENU)
        return user_input

    def print_droid_type_menu(self, droid_list: list) -> str:
        """Prints Droid Type Menu"""
        running = True
        while running:
            print("Type Selection Number:")
            for index, item in enumerate(droid_list):
                print(index, item)
            user_input = input(">")
            print()
            running = self.__validate_list_input(user_input, droid_list)
        return user_input

    def print_collection(self, collection: DroidCollection) -> None:
        """Prints Droid Collection"""
        #TODO: I want to be able to print the color of he droid
        #in that color.  I will have to pull out the color (red, blue, etc.)
        #from the larger string using regular expressions
        #and then use a print method imported from colors.py

        #NOTE: I will not implement printing in color for the color.
        #This would involve me hardcoding the color options to this class
        #rather than searching the modules dynamically for qualitative
        #option dicts

        #NOTE: I might implement the regex search, just for practice
        for droid in collection.collection:
            #droid_color_broken is the droid string split into a list
            #based on re.split by color
            #This will let us print the color string in its color

            #this pattern is needed to search for each color
            # pattern = r"Red|Yellow|Blue|Green"
            # droid_color_broken = re.split((pattern), str(droid))
            # print(droid_color_broken)
            # for string in droid_color_broken:
            #     if string == "Red":
            #         print_red("Red")
            #     else:
            #         print(string)
            print(droid)
        print()

    def print_choice_menu(self, input_list: list, input_option: str) -> str:
        """Get Material or Color For Droid method"""
        running = True
        while running:
            print(f"Type {input_option} Selection Number:")
            for index, item in enumerate(input_list):
                print(index, item)
            user_input = input(">")
            print()
            running = self.__validate_list_input(user_input, input_list)
        user_input_index = int(user_input)
        user_input = input_list[user_input_index]
        return user_input

    def get_quantity(self, option: str) -> str:
        """gets number of option"""
        running = True
        while running:
            print(f"How many {option} do you want?")
            user_input = input(">")
            print()
            running = self.__validate_quanity_input(user_input)
        return user_input

    def get_yes_or_no(self, option: str) -> str:
        """method to get yes or no input"""
        running = True
        while running:
            print(f"Add {option} to the droid?\n0 Yes\n1 No")
            user_input = input(">")
            running = self.__validate_yes_no_input(user_input)
        return user_input

    def __validate_list_input(self, input1: str, choice_list: list) -> bool:
        """Method to validate input when choices are a list"""
        # also known as a qualitative validator
        try:
            input_int = int(input1)
        except ValueError:
            print_red("Input must be an int.")
            return True
        if input_int in range(len(choice_list)):
            return False
        else:
            print_red("Choice not in menu.")
            return True

    def __validate_quanity_input(self, input1: str) -> bool:
        """Quantity input validator"""
        try:
            input_int = int(input1)
        except ValueError:
            print_red("Input must be an int.")
            return True
        if 0 <= input_int <= 25:
            return False
        else:
            print_red("Quantity must be between 0 and 25, inclusive")
            return True

    def __validate_yes_no_input(self, input1: str) -> bool:
        """Bool input validator"""
        try:
            input_int = int(input1)
        except ValueError:
            print_red("Input must be an int.")
            return True
        if 0 <= input_int <= 1:
            return False
        else:
            print_red("Input must be 0 or 1")
            return True
