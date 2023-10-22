#!/usr/bin/python3
"""write a class Student that defines a student"""


class Student:
    """create student class"""

    def __init__(self, first_name, last_name, age):
        """public instanc attr
        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance."""
        dict_attr = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                dict_attr[attr] = value
        return dict_attr
