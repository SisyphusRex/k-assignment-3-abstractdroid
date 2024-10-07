"""Protocol Droid Class File"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
from typing import override

# First Party Imports
from DroidClasses.Abstract.droid import Droid

# Third Party Imports


DROID_TYPE_NAME = "Protocol"


class Protocol(Droid):
    """Protocol Droid Parent Class"""

    PROTOCOL_MODEL_SURCHARGE: float = 2.00

    def __init__(self, material: str, color: str, number_of_languages: int):
        """Constructor and Attributes"""
        super().__init__(material, color)
        self.number_of_languages = number_of_languages

    def __str__(self):
        """String method"""
        return f"{super().__str__()}\n  {'Languages: ' + str(self.number_of_languages):<20}"

    @override
    def calculate_total_cost(self):
        """Calculate total cost based off of languages and droid type"""
        super().calculate_total_cost()
        self.total_cost = (
            self.total_cost
            + self.PROTOCOL_MODEL_SURCHARGE
            + self.QUANTITY_OPTION_COST * self._number_of_quantity_options
        )

    @property
    def _number_of_quantity_options(self):
        return self.number_of_languages
