"""Program code"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
import sys

# First Party Imports
from user_interface import UserInterface
from droid_collection import DroidCollection
from utils import Utilities
from DroidClasses.Abstract.droid import Droid


# Third Party Imports


def main(*args):
    """Method to run program"""

    # constant used to find droid modules file path
    DROID_DIRECTORY = "DroidClasses\Creatable"
    # constant to establish naming convention for dictionaries of qualitative options and their prices
    # if the class has a special parameter and a list of its options and prices
    # that dict of options and prices must have this suffix concatenated to the parameter name.
    # example: colors must have dict COLORS_QUALITATIVE_DICT for my program to find it in the class file
    QUALITATIVE_DICT_SUFFIX = "_QUALITATIVE_DICT"

    # loads utility class
    my_utility = Utilities()
    # uses utility method to find all creatable droid modules in the directory
    list_of_droid_types = my_utility.find_droid_types(DROID_DIRECTORY)
    # loads user interface
    my_ui = UserInterface()
    # loads droid collection class
    my_collection = DroidCollection()

    # creates a list out of the dict of colors and their costs
    # color_list = my_utility.dict_to_list(Droid.COLOR_COST)
    # creates a list out of the dict of materials and their costs
    # material_list = my_utility.dict_to_list(Droid.MATERIAL_COST)

    # displays the main menu
    main_choice = my_ui.print_main_menu()

    # this is the logic of the main menu.  A user has only three options:
    # 1. Create a Droid
    # 2. Print the collection
    # 3. Exit
    while int(main_choice) < 3:
        match int(main_choice):
            case 0:
                # create a droid
                # Since I wrote this program to handle additions to the Droid Modules in the future without
                # hardcoding imports of each new addition as well as menu changes, we must use our utility
                # methods to import the module indicated by the user input.
                choice = my_ui.print_droid_type_menu(list_of_droid_types)
                droid_name = list_of_droid_types[int(choice)]
                droid_object = my_utility.import_module_and_create_class_object(
                    droid_name, DROID_DIRECTORY
                )

                # Since we do not know what the parameters of a class constructor will be, we must use
                # this utility method to discover the parameters and assign them to a dict.
                # This parameter_dict stores the name of the parameter and what DATA TYPE it is.
                # Knowing the data type is very important because our user interface displays different
                # options depending on whether we want yes or no input, quantity, or quality.
                parameter_dict = my_utility.get_params(droid_object)
                # the parameter_dict holds the parameter name and its data type
                my_dict = {}
                # my_dict will be the collection of paramter names and the values determined by user input
                for key, value in parameter_dict.items():
                    # displays menu depending on type of parameter.  Since we are only dealing with three types of parameters
                    # to construct a droid, simple if statements or maybe a match case will suffice
                    if value == "bool":
                        # if the parameter is a bool, we know that it requires a True or False statement
                        # or Yes or No for the user
                        choice = my_ui.get_yes_or_no(key)
                        if choice == "1":
                            my_dict.update({key: False})
                        if choice == "0":
                            my_dict.update({key: True})
                    if value == "int":
                        # If the parameter is an int, we know that the user must input a quantity
                        quantity = int(my_ui.get_quantity(key))
                        my_dict.update({key: quantity})
                    if value == "str":
                        # This is the hardest parameter type to address dynamically.  When a parameter takes a string,
                        # it indicates that the droid is being constructed (object of class instantiated) with a qualitative
                        # physical attribute (color, material, etc.).  The choices of droid attributes are predefined in dicts or lists and the user
                        # can only select an option from the choices.  My program does not accept open ended inputs, only integers.
                        # This poses a problem because what if someone wanted to add a droid module to creatable classes that can be
                        # constructed with other qualitative options held in a new list.  My program does not search for that list, and
                        # only refers to the colors and materials defined in the Droid.py module.
                        # TODO: In the future, I would like to remove the hardcoded lists and instead search through the modules for qualitative
                        # lists using a utility method.  Honestly, I think I can leave the color and material "if comparisons" hard coded
                        # but have a third "if key == ..." comparison that compares the key to a dynamic value returned by the utility method
                        # which scoured the module for a qualitative list or dict indicated by the constant CAPITAL_LETTERS.
                        # if key == "color":
                        #     choice = my_ui.print_choice_menu(color_list, key)
                        #     my_dict.update({key: choice})
                        # if key == "material":
                        #     choice = my_ui.print_choice_menu(material_list, key)
                        #     my_dict.update({key: choice})
                        # TODO:this is where I need the comparison of the parameter name to the utility method returned value:
                        # if key == my_utility.find_name_of_new_qualitative_lists()
                        #   choice = my_ui.print_choice_menu(droid_object.<my_utility.find_name_of_new_qualitative_lists()>)
                        qualitative_dict = my_utility.get_dict_from_str(
                            droid_object, key, QUALITATIVE_DICT_SUFFIX
                        )
                        qualitative_list = my_utility.dict_to_list(qualitative_dict)
                        choice = my_ui.print_choice_menu(qualitative_list, key)
                        my_dict.update({key: choice})

                # here, we use the dictionary of parameters to instantiate a droid
                created_droid = droid_object(**my_dict)
                created_droid.calculate_total_cost()
                my_collection.add(created_droid)

            case 1:
                # print the list of droids
                my_ui.print_collection(my_collection)

            case 2:
                sys.exit()
        main_choice = my_ui.print_main_menu()
