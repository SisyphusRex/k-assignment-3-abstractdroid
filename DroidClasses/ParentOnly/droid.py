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


class Droid(AbstractDroid, ABC):
    """Parent class to Protocol and Utility"""

    DROID_BASE_COST: float = 10.00

    def __init__(self, material: str, color: str):
        """Constructor"""
        super().__init__()
        self.str1 = material
        self.str2 = color

    def __str__(self):
        """String method"""

    def calculate_total_cost(self):
        """Calculates Total Cost"""
        self.total_cost = self.DROID_BASE_COST
