#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """Implements sorted for the built-in list class """

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
