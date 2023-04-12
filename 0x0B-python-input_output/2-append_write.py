#!/usr/bin/python3
"""This program defines a file-appending function."""


def append_write(filename="", text=""):
    """This fuction appends or attachs a string to the end of a UTF8-encoded text file.
    Arguments:
        filename, a string param (str): The name of the file to append the text to.
        text (str): The string or text to append to the file.
    Returns:
        The number of text characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
