#!/usr/bin/python3
"""This python program defines a Python class-to-JSON function."""


def class_to_json(obj):
    """This class will return the dictionary represntation of a simple data structure."""
    return obj.__dict__
