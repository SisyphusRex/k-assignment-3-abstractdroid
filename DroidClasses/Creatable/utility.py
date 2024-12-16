"""Utility Droid Class File"""



# System Imports


# First Party Imports
from DroidClasses.Abstract.droid import Droid

# Third Party Imports

DROID_TYPE_NAME = "Utility"


class Utility(Droid):
    """Utility Droid Parent Class to Janitor and Astromech"""

    UTILITY_MODEL_SURCHARGE: float = 0.75

    def __init__(
        self,
        material: str,
        color: str,
        toolbox: bool,
        computer_connection: bool,
        scanner: bool,
    ):
        """Constructor and Attributes"""
        super().__init__(material, color)
        self.toolbox = toolbox
        self.computer_connection = computer_connection
        self.scanner = scanner

    def __str__(self):
        """String Method"""
        return f"{super().__str__()}\n  {'Toolbox: ' + str(self.toolbox):<20} {'Computer: ' + str(self.computer_connection):<20} {'Scanner: ' + str(self.scanner):<20}"

    def calculate_total_cost(self):
        """Calculate Total Cost Method by options and droid type"""
        super().calculate_total_cost()
        self.total_cost = (
            self.total_cost
            + self.UTILITY_MODEL_SURCHARGE
            + self.OPTION_COST * self._number_of_options
        )

    @property
    def _number_of_options(self) -> int:
        """counts number of options selected"""
        count: int = 0
        if self.toolbox:
            count += 1
        if self.computer_connection:
            count += 1
        if self.scanner:
            count += 1
        return count
