"""Console Color Changer"""



# System Imports
import os

# First Party Imports

# Third Party Imports


# 10/8/2024: This module is not implemented in my user_interface.py yet because printing is not simple because of the
# dynamic nature of the program.

os.system("")


def singleton(cls):
    """Singleton functioin"""
    return cls()


@singleton
class Style:
    """Contains color constants"""

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"
    CLEAR = "\033[H\033[2J"

    def __getattribute__(self, name):
        """Override default dunder method"""
        value = super().__getattribute__(name)
        print(value, end="")
        return value


def print_red(message):
    """method to print in red"""
    Style.RED
    print(message)
    Style.RESET
