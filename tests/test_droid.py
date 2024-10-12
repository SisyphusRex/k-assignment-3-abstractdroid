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



# Third Party imports
import pytest
# requires pip install pytest

#NOTE: This is the old version of test astromech price without a class:
# def test_astromech_price(monkeypatch):
#simulated_responses = ["0", "0", "0", "0", "0", "0", "0", "0", "1"]
#my_responses = iter(simulated_responses)
#monkeypatch.setattr(builtins, "input", lambda message: next(my_responses))
#try:
#   assert main().my_collection.collection[0].total_cost == 17.75
#except StopIteration:
#   pass


class EndToEndTest(TestCase):
    """Test end to end functionality"""
    def test_astromech_price(self):
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
        simulated_responses = ["0", "0", "0", "0", "0", "0", "0", "0", "1"]

        # turn the list into an iterator, which allows us to use the next() function to move through the items to the next without a for loop
        my_responses = iter(simulated_responses)

        # use monkeypatch to replace input() with lambda function that returns next response in iterator
        # lambda message is necessary because some inputs pass an argument
        #NOTE: monkeypatch must be called using pytest.MonkeyPatch()
        pytest.MonkeyPatch().setattr(builtins, "input", lambda message: next(my_responses))

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
        #Arrange
        expected_material = "Steel"
        expected_color = "Red"
        expected_number_of_languages = 2

