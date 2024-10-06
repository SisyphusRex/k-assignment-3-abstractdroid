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


class Droid(AbstractDroid, ABC):
    """Parent class to Protocol and Utility"""

    COLOR_COST: dict = {"Red": 1.00, "Yellow": 1.50, "Blue": 2.00, "Green": 2.50}
    MATERIAL_COST: dict = {
        "Aluminum": 1.25,
        "Steel": 1.50,
        "Titanium": 1.75,
        "Carbon Fiber": 2.00,
    }
    DROID_BASE_COST: float = 10.00
    OPTION_COST: float = 1.00
    QUANTITY_OPTION_COST: float = 0.75

    def __init__(self, material: str, color: str):
        """Constructor"""
        super().__init__()
        self.material = material
        self.color = color

    def __str__(self) -> str:
        """String method"""
        return f"{self._class_name:<20}\n  {'Price: ' + str(self.formatted_price):<20} {'Material: ' + str(self.material):<20} {'Color: ' + str(self.color):<20}"

    def calculate_total_cost(self):
        """Calculates Total Cost"""
        self.total_cost = self.DROID_BASE_COST + self._material_cost + self._color_cost

    @property
    def formatted_price(self) -> float:
        """Format price to 2 decimal places"""
        return f"${self.total_cost:.2f}"

    @property
    def _class_name(self) -> str:
        """Takes class name out of type() call"""
        my_str = str(type(self))
        my_list = my_str.split(".")
        name = my_list[-1].strip("'>")
        return name

    @property
    def _material_cost(self) -> float:
        """Gets Material cost value"""
        return self.MATERIAL_COST[self.material]

    @property
    def _color_cost(self) -> float:
        """Gets Color Cost value"""
        return self.COLOR_COST[self.color]
