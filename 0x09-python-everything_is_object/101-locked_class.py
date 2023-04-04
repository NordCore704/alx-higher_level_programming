#!/usr/bin/python3
"""Creates a locked class."""


class classLocked:
    """
    Prevent the user from instantiating new classLocked attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
