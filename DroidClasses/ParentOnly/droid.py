"""Second Abstract class, Inherits from abstract_droid"""

# Walter Podewil
# CIS 226
# October 1, 2024

# System Imports
from abc import ABC, abstractmethod
from typing import override

# First Party Imports
from DroidClasses.ParentOnly.abstract_droid import AbstractDroid

# Third Party Imports


# File Constants to keep track of options prices
COLOR_COST: dict = {"Red": 1.00, "Yellow": 1.50, "Blue": 2.00, "Green": 2.50}
MATERIAL_COST: dict = {
    "Aluminum": 1.25,
    "Steel": 1.50,
    "Titanium": 1.75,
    "Carbon Fiber": 2.00,
}


class Droid(AbstractDroid, ABC):
    """Parent class to Protocol and Utility"""

    DROID_BASE_COST: float = 10.00

    def __init__(self, material: str, color: str):
        """Constructor"""
        super().__init__()
        self.material = material
        self.color = color

    def __str__(self) -> str:
        """String method"""
        return f"{self.format_price(self.total_cost)} {self._get_class_name()} {self.material} {self.color}"

    def calculate_total_cost(self):
        """Calculates Total Cost"""
        self.total_cost = self.DROID_BASE_COST

    def format_price(self, number: float) -> float:
        """Format price to 2 decimal places"""
        return f"${number:.2f}"

    def _get_class_name(self) -> str:
        my_str = str(type(self))
        my_list = my_str.split(".")
        name = my_list[-1].strip("'>")
        return name
