"""Protocol Droid Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
from typing import override

# First Party Imports
from DroidClasses.ParentOnly.droid import Droid

# Third Party Imports


DROID_TYPE_NAME = "Protocol"


class Protocol(Droid):
    """Protocol Droid Parent Class"""

    COST_PER_LANGUAGE: float = 1.00
    DROID_MODEL_SURCHARGE: float = 2.00

    def __init__(self, material: str, color: str, number_of_languages: int):
        """Constructor and Attributes"""
        super().__init__(material, color)
        self.number_of_languages = number_of_languages

    def __str__(self):
        """String method"""

    def calculate_total_cost(self):
        """Calculate total cost based off of languages and droid type"""
        super().calculate_total_cost()
        self.total_cost = (
            self.total_cost
            + self.DROID_MODEL_SURCHARGE
            + self.COST_PER_LANGUAGE * self.number_of_languages
        )
