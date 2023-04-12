#!/usr/bin/python3
"""This program will deliver a file-writing function."""


def write_file(filename="", text=""):
    """The function that will write a string to a UTF8-encoded text file.
    Args:
        filename, a string (str): The name of the file to write to.
        text, a string param (str): The text to be written to the file.
    Returns:
        The number of written characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
