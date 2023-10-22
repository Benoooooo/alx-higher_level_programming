#!/usr/bin/python3
"""a class Student that defines a student by:(based on 9-student.py)"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance

        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary of a Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        attri = {}
        for attr in attrs:
            if hasattr(self, attr) and isinstance(getattr(self, attr),
                         (list, dict, str, int, bool)):
                attri[attr] = getattr(self, attr)
        return attrii
