#!/usr/bin/python3
"""This program defines a class named Student."""


class Student:
    """Represent the student class for any student provided."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with name info as constructor params.
        Args:
            first_name, is a string (str): The first name of the student provided.
            last_name (str): The last name of the student as provided.
            age (int): The age of the given student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student provided.
        If attrs is a list of strings, it will represent only those attributes
        included in the list.
        Args:
            attrs, a list (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
