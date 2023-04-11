#!/usr/bin/python3
"""This program defines a class MyInt that inherits from int."""


class MyInt(int):
    """This will invert the int operators == and !=."""

    def __eq__(self, value):
        """Override the == opeartor with the != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override the != operator with the == behavior."""
        return self.real == value
