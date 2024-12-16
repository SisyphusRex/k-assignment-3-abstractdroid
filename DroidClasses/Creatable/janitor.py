"""Janitor Droid Class File"""



# System Imports
from typing import override

# First Party Imports
from DroidClasses.Creatable.utility import Utility

# Third Party Imports


DROID_TYPE_NAME = "Janitor"


class Janitor(Utility):
    """Janitor Droid Class"""

    def __init__(
        self,
        material: str,
        color: str,
        toolbox: bool,
        computer_connection: bool,
        scanner: bool,
        broom: bool,
        vacuum: bool,
    ):
        """Constructor"""
        super().__init__(material, color, toolbox, computer_connection, scanner)
        self.broom = broom
        self.vacuum = vacuum

    def __str__(self):
        """String Method"""
        return f"{super().__str__()}\n  {'Broom: ' + str(self.broom):<20} {'Vacuum: ' + str(self.vacuum):<20}"

    def calculate_total_cost(self):
        """Calculate total cost by droid type and options"""
        super().calculate_total_cost()
        self.total_cost = self.total_cost + self.OPTION_COST * self._number_of_options

    @override
    @property
    def _number_of_options(self) -> int:
        count: int = 0
        if self.broom:
            count += 1
        if self.vacuum:
            count += 1
        return count
