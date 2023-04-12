#!/usr/bin/python3
"""This program defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """The function that will return the Python object representation of a JSON string as passed."""
    return json.loads(my_str)
