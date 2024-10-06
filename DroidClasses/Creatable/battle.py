"""File for battle droid class"""

# Walter Podewil
# CIS 226
# October 5, 2024

# System Imports

# First Party Imports
from DroidClasses.ParentOnly.droid import Droid

# Third Party Imports


DROID_TYPE_NAME = "Battle"


class Battle(Droid):
    """Class for Battle Droid"""

    BATTLE_MODEL_SURCHARGE: float = 5.00

    def __init__(
        self, material: str, color: str, number_of_laser_guns: int, lightsaber: bool
    ):
        """Constructor"""
        super().__init__(material, color)
        self.number_of_laser_guns = number_of_laser_guns
        self.lightsaber = lightsaber

    def __str__(self):
        """String Method"""
        return f"{super().__str__()}\n  {'Laser Guns: ' + str(self.number_of_laser_guns):<20} {'Lightsaber: ' + str(self.lightsaber)}"

    def calculate_total_cost(self):
        super().calculate_total_cost()
        self.total_cost = (
            self.total_cost
            + self.number_of_laser_guns * self.QUANTITY_OPTION_COST
            + self._number_of_options * self.OPTION_COST
        )

    @property
    def _number_of_options(self):
        count: int = 0
        if self.lightsaber:
            count += 1
        return count
