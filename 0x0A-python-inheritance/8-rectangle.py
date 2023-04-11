#!/usr/bin/python3
"""This program defines a class Rectangle that inherits from the BaseGeometry class in task file 7."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle calculated using the BaseGeometry class."""

    def __init__(self, width, height):
        """The constructor that will intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
