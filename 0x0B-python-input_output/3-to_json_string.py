#!/usr/bin/python3
"""This program defines a string-to-JSON type function with the json module."""
import json


def to_json_string(my_obj):
    """This function will return the JSON representation of a string object."""
    return json.dumps(my_obj)
