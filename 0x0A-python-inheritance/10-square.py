#!/usr/bin/python3
"""This program defines a Rectangle subclass Square from the Rectangle class in task 9."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creates a square class."""

    def __init__(self, size):
        """Initialize a new square.
        Args:
            size (int): The size of the new created square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
