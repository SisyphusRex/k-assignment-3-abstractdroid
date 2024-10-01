"""DroidCollection Class File"""

#Walter Podewil
#CIS 226
#October 1, 2024

#System Imports

#First Party Imports

#Third Party Imports

class DroidCollection():
    """Collection of Created droids"""
    def __init__(self, collection = None):
        """Constructor"""
        self.collection = collection or []

    def add(self, droid):
        """Appends droid to the list"""
        self.collection.append(droid)