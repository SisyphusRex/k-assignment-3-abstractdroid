"""Utility Droid Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
from typing import override

# First Party Imports
from DroidClasses.ParentOnly.droid import Droid

# Third Party Imports

DROID_TYPE_NAME = "Utility"


class Utility(Droid):
    """Utility Droid Parent Class to Janitor and Astromech"""

    toolbox: bool = False
    computer_connection: bool = False
    scanner: bool = False

    def __init__(self, str1: str, str2: str, bool1: bool, bool2: bool, bool3: bool):
        """Constructor and Attributes"""
        super().__init__(str1, str2)
        self.bool1 = bool1
        self.bool2 = bool2
        self.bool3 = bool3

    def __str__(self):
        """String Method"""

    def calculate_total_cost(self):
        """Calculate Total Cost Method by options and droid type"""
