#!/usr/bin/python3
"""This program defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This class reprsents improved base geometry."""

    def area(self):
        """This method is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method acts as a validator: Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter which is a string.
            value (int): The parameter to validate.
        Raises:
            TypeError: If the value parameter is not an integer.
            ValueError: If the value parameter is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
