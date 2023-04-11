#!/usr/bin/python3
"""This python program defines a function that adds attributes to the given objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if it is a possibility.
    Args:
        obj (any): The object to which an atrribute will be added to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot in any way be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
