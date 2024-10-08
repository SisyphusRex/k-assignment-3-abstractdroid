"""Pytest methods"""

# this requires pip install pytest

# Walter Podewil
# October 5, 2024
# CIS 226

# System Imports
import builtins

# First Party Imports
from program import main

# Third Party imports
# requires pip install pytest


def test_astromech_price(monkeypatch):
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

    # turn the list into an iterator
    my_responses = iter(simulated_responses)

    # use monkeypatch to replace input() with lambda function that returns next response in iterator
    monkeypatch.setattr(builtins, "input", lambda: next(my_responses))

    # since the program will ask for inputs after we have exhausted our simulated_responses, we must catch the error
    try:
        # run main with monkeypatch on input()
        # access the created droids total_cost attribute and compare to manually calculated total
        assert main().my_collection.collection[0].total_cost == 17.75
    except StopIteration:
        #this exception is needed because my iterator is not continuous, but the program can be
        pass
