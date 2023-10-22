#!/usr/bin/python3
"""Write a class Student that defines a student by:
   (based on 10-student.py)"""


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
        Retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:
            attrs = self.__dict__.keys()
        attri = {
            attr: getattr(self, attr)
            for attr in attrs
            if isinstance(getattr(self, attr), (list, dict, str, int, bool))
        }
        return attri

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
