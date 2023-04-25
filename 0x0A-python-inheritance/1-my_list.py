#!/usr/bin/python3
"""
contains the MyList class
"""

class MyList(list):
    """Is a subclass of list"""
    def __init__(self):
        "'"This initializes the object:
         super().__init__()

    def print_sorted(self):
        """To print the sorted list"""
        print(sorted(self))
