#!/usr/bin/python3
"""This program defines an object attribute lookup function."""


def lookup(obj):
    """This function will return a list of an object's available attributes."""
    return (dir(obj))
