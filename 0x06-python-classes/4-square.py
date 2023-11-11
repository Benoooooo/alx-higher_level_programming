#!/usr/bin/python3
# file: 4-square.py
# Auth: kelechi nnadi <@alx swe>

"""the code is to privetize the attribut"""


class Square:
    """
        definition of an attribute to function class square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """propeprty to retrive it"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
