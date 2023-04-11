#!/usr/bin/python3
"""
This program contains the MyList class
"""


class MyList(list):
    """The MyList class: it will implement a sorted printing for the built-in list class."""

    def print_sorted(self):
        """This method will print a list in sorted ascending order."""
        print(sorted(self))
