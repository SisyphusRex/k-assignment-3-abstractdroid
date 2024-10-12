"""Pytest methods"""

# this requires pip install pytest

# Walter Podewil
# October 5, 2024
# CIS 226

# System Imports
import builtins
from unittest import TestCase

# First Party Imports
from program import main
from DroidClasses.Creatable.protocol import Protocol
from utils import Utilities


# Third Party imports
import pytest

# requires pip install pytest

# NOTE: This is the old version of test astromech price without a class:
# def test_astromech_price(monkeypatch):
# simulated_responses = ["0", "0", "0", "0", "0", "0", "0", "0", "1"]
# my_responses = iter(simulated_responses)
# monkeypatch.setattr(builtins, "input", lambda message: next(my_responses))
# try:
#   assert main().my_collection.collection[0].total_cost == 17.75
# except StopIteration:
#   pass


def spoof_user_input(simulated_inputs: list) -> None:
    """Method to take list of inputs and spoof user inputs"""
    simulated_iter: iter = iter(simulated_inputs)
    # MonkeyPatch replaces builtin function called input with lambda function
    pytest.MonkeyPatch().setattr(
        builtins, "input", lambda message: next(simulated_iter)
    )


class EndToEndTest(TestCase):
    """Test end to end functionality"""

    def test_astromech_end_to_end(self):
        """Tests for correct price after simulating user inputs"""
        # first input: 0 add new droid
        # second input: 0 choose astromech
        # third input : 0 choose material Aluminum
        # fourth input: 0 choose color Red
        # fifth input : 0 add toolbox Yes
        # sixth input: 0 add computer Yes
        # seventh input: 0 add scanner Yes
        # eigth input:  0 add navigation Yes
        # ninth input : 1 number of ships 1

        # this is a list of 'user inputs' that I am spoofing, in order
        simulated_responses: list = ["0", "0", "0", "0", "0", "0", "0", "0", "1"]

        # turn the list into an iterator, which allows us to use the next() function to move through the items to the next without a for loop
        my_responses: iter = iter(simulated_responses)

        # use monkeypatch to replace input() with lambda function that returns next response in iterator
        # lambda message is necessary because some inputs pass an argument
        # NOTE: monkeypatch must be called using pytest.MonkeyPatch()
        pytest.MonkeyPatch().setattr(
            builtins, "input", lambda message: next(my_responses)
        )

        # since the program will ask for inputs after we have exhausted our simulated_responses, we must catch the error
        try:
            # run main with monkeypatch on input()
            # access the created droids total_cost attribute and compare to manually calculated total
            self.assertEqual(main().my_collection.collection[0].total_cost, 17.75)
        except StopIteration:
            # this exception is needed because my iterator is not continuous, but the program can be
            pass


class ProtocolDroidTest(TestCase):
    """Test the Protocol Droid"""

    def setUp(self):
        """Set up method for all tests in this class"""
        self.protocol_droid = Protocol("Steel", "Red", 2)

    def test_protocol_droid_creation(self):
        """Test protocol droid creation"""
        # Arrange
        expected_material: str = "Steel"
        expected_color: str = "Red"
        expected_number_of_languages: int = 2

        # Act
        # this is covered in the setUp

        # Assert
        self.assertEqual(self.protocol_droid.material, expected_material)
        self.assertEqual(self.protocol_droid.color, expected_color)
        self.assertEqual(
            self.protocol_droid.number_of_languages, expected_number_of_languages
        )

    def test_prototcol_droid_cost(self):
        """Tests total price for protocol droid"""
        # Arrange
        # Droid Base Cost = 10.00
        # Material Cost Steel = 1.50
        # Color Cost Red = 1.00
        # Model Surcharge Protocol= 2.00
        # Quantity Option Cost = 0.75 * 2 = 1.50
        # total = 16.00
        expected_cost: float = 16.00

        # Act
        self.protocol_droid.calculate_total_cost()

        # assert
        self.assertEqual(self.protocol_droid.total_cost, expected_cost)

    def test_protocol_end_to_end_cost(self):
        """Tests total cost after spoofing user inputs"""
        # Arrange
        # 0 create new droid
        # 3 choose protocol
        # 1 choose steel
        # 0 choose red
        # 2 number of ships
        input_list: list = ["0", "3", "1", "0", "2"]
        spoof_user_input(input_list)
        expected_cost: float = 16.00

        # Act
        try:
            calculated_cost: float = main().my_collection.collection[0].total_cost

            # Assert
            self.assertEqual(calculated_cost, expected_cost)
        except StopIteration:
            pass

    def test_protocol_string_method(self):
        """Tests protocol droid string method"""
        # Arrange
        expected_string = (
            "Protocol            \n"
            "  Price: $16.00        Material: Steel      Color: Red          \n"
            "  Languages: 2        "
        )

        # act
        self.protocol_droid.calculate_total_cost()
        calculated_str: str = str(self.protocol_droid)

        # assert
        self.assertEqual(calculated_str, expected_string)

    # def test_protocol_number_of_quantity(self):
    #     """Tests protocol number of quantity method"""
    #     # NOTE: This test will not pass because the method called is a protected method
    #     # Arrange
    #     expected_number: int = 2

    #     # Act
    #     # covered with setUp

    #     # assert
    #     self.assertEqual(
    #       self.protocol_droid._number_of_quantity_options(), expected_number
    #     )


class UtilityTest(TestCase):
    """This class tests the Utility Module"""

    # used r to treat string as a raw string
    DROID_DIRECTORY = r"tests\PracticeDroidClasses"

    def setUp(self):
        self.utility = Utilities()

    def test_for_get_dict_method_exists(self):
        """Test to see if class has get dict method"""
        # Arrange

        # act
        # covered in setUp

        # assert
        self.assertTrue(hasattr(self.utility, "get_dict_from_str"))

    def test_for_find_droid_types_method_exists(self):
        """test to see if class has find droid method"""

        # arrange

        # act
        # covered in setUp

        # Assert
        self.assertTrue(hasattr(self.utility, "find_droid_types"))

    def test_utils_find_droid_types_method(self):
        """test for find droid method"""

        # Arrange
        expected_droid_names: list[str] = ["Practice Droid One", "Practice Droid Two"]

        # Act
        calculated_droid_names: list[str] = self.utility.find_droid_types(
            self.DROID_DIRECTORY
        )

        # Assert
        self.assertListEqual(
            calculated_droid_names, expected_droid_names
        )  # lists must have same contents and order
        self.assertCountEqual(
            calculated_droid_names, expected_droid_names
        )  # lists must have same contents, regardless of order
