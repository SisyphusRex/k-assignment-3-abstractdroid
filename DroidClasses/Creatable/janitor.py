"""Janitor Droid Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports

# First Party Imports
from DroidClasses.Creatable.utility import Utility

# Third Party Imports


DROID_TYPE_NAME = "Janitor"


class Janitor(Utility):
    """Janitor Droid Class"""

    broom: bool = False
    vacuum: bool = False

    def __init__(
        self,
        str1: str,
        str2: str,
        bool1: bool,
        bool2: bool,
        bool3: bool,
        bool4: bool,
        bool5: bool,
    ):
        """Constructor"""
        super().__init__(str1, str2, bool1, bool2, bool3)
        self.bool4 = bool4
        self.bool5 = bool5

    def __str__(self):
        """String Method"""

    def calculate_total_cost(self):
        """Calculate total cost by droid type and options"""
