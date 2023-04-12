#!/usr/bin/python3
"""This program defines a class Student."""


class Student:
    """The created or represented Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with attributes.
        Args:
            first_name, a string (str): The first name of the given student.
            last_name (str): The last name of the student given.
            age (int): The age of the student as provided.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This function will get a dictionary representation of the Student."""
        return self.__dict__
