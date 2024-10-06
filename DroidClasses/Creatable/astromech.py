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
        material: str,
        color: str,
        toolbox: bool,
        computer_connection: bool,
        scanner: bool,
        navigation: bool,
        number_of_ships: int,
    ):
        """Constructor"""
        super().__init__(material, color, toolbox, computer_connection, scanner)
        self.navigation = navigation
        self.number_of_ships = number_of_ships

    def __str__(self):
        """String method"""
        return f"{super().__str__()}\n  {'Navigation: ' + str(self.navigation):<20} {'Ships: ' + str(self.number_of_ships):<20}"

    def calculate_total_cost(self):
        """calculate total cost method"""
        super().calculate_total_cost()
        self.total_cost = (
            self.total_cost
            + self._number_of_options * self.OPTION_COST
            + self._number_of_quantity_options * self.QUANTITY_OPTION_COST
        )

    @property
    @override
    def _number_of_options(self):
        """Counts options, in this case navigation"""
        count: int = 0
        if self.navigation:
            count += 1
        return count

    @property
    @override
    def _number_of_quantity_options(self):
        """Calculates number of quantity options from ships"""
        return self.number_of_ships
