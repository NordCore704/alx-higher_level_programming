#!/usr/bin/python3
"""This program will define a JSON file-writing function, for writing an object to a plaintext file."""
import json


def save_to_json_file(my_obj, filename):
    """This function will write an object to a plaintext file using JSON representation or formatting."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
