#!/usr/bin/python3
"""This program defines a class named Student."""


class Student:
    """Represent the student class for any student to be entered in."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student constructor params.
        Args:
            first_name, a string (str): The first given name of the student.
            last_name, a string (str): The last given name of the student.
            age (int): The age of the student as provided.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method will get a dictionary representation of the Student.
        If attrs is a list of strings, it will represent only those attributes that are
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """This method will replace all attributes of the Student.
        Args:
            json (dict): The key:value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
