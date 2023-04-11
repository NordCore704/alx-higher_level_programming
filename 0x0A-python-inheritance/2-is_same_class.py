#!/usr/bin/python3
"""This python program defines a class-checking function."""


def is_same_class(obj, a_class):
    """A function that will check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object that will be checked.
        a_class (type): The class that will match the type of obj.
    Returns:
        If obj is exactly an instance of a_class - True.
        Else - False.
    """
    if type(obj) == a_class:
        return True
    return False
