#!/usr/bin/python3
"""This program defines a text file-reading function."""


def read_file(filename=""):
    """This function will print the contents of a UTF8 text file to stdout(standard output)."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
