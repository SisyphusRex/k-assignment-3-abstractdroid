"""Astromech Droid Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
from typing import override

# First Party Imports
from DroidClasses.Creatable.utility import Utility

# Third Party Imports


DROID_TYPE_NAME = "Astromech"


class Astromech(Utility):
    """Astromech Droid Class"""

    navigation: bool = False
    number_of_ships: int = None

    COST_PER_SHIP: int = None

    def __init__(
        self,
        str1: str,
        str2: str,
        bool1: bool,
        bool2: bool,
        bool3: bool,
        bool4: bool,
        int1: int,
    ):
        """Constructor"""
        super().__init__(str1, str2, bool1, bool2, bool3)
        self.bool4 = bool4
        self.int1 = int1

    def __str__(self):
        """String method"""

    def calculate_total_cost(self):
        """calculate total cost method"""
