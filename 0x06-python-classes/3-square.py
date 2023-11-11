#!/usr/bin/python3
# file: 3-square.py
# Auth: kelechi nnadi <@alx swe>

"""class definition"""


class Square:
    """class definition on the size"""

    def __init__(self, size):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
