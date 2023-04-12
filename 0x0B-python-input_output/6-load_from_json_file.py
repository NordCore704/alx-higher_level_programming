#!/usr/bin/python3
"""This program defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """This function will create a Python object from a JSON file, as is given."""
    with open(filename) as f:
        return json.load(f)
