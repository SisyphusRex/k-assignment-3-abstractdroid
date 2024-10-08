"""File for battle droid class"""

# Walter Podewil
# CIS 226
# October 5, 2024

# System Imports

# First Party Imports
from DroidClasses.Abstract.droid import Droid

# Third Party Imports


DROID_TYPE_NAME = "Battle"


class Battle(Droid):
    """Class for Battle Droid"""

    ARMORR_QUALITATIVE_DICT: dict = {
        "PLATE": 0.25,
        "CHAIN": 0.50,
        "SCALE": 0.75,
    }

    BATTLE_MODEL_SURCHARGE: float = 5.00

    def __init__(
        self,
        material: str,
        color: str,
        number_of_laser_guns: int,
        lightsaber: bool,
        armor: str,
    ):
        """Constructor"""
        super().__init__(material, color)
        self.number_of_laser_guns = number_of_laser_guns
        self.lightsaber = lightsaber
        self.armor = armor

    def __str__(self):
        """String Method"""
        return f"{super().__str__()}\n  {'Laser Guns: ' + str(self.number_of_laser_guns):<20} {'Lightsaber: ' + str(self.lightsaber):<20} {'Armor: ' + str(self.armor):<20}"

    def calculate_total_cost(self):
        super().calculate_total_cost()
        self.total_cost = (
            self.total_cost
            + self.number_of_laser_guns * self.QUANTITY_OPTION_COST
            + self._number_of_options * self.OPTION_COST
            + self.__armor_cost()
        )

    @property
    def _number_of_options(self):
        count: int = 0
        if self.lightsaber:
            count += 1
        return count

    def __armor_cost(self) -> float:
        return self.ARMOR_QUALITATIVE_DICT[self.armor]
