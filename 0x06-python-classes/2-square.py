#!/usr/bin/python3
# file: 2-square.py
# Auth: kelechi nnadi <@alx swe>

""" define square class that takes data"""


class Square:
    """square defines the data it gets"""

    def __init__(self, size=0):
        """initialising the value of size and check for
        if the size provided is an integer or less than
        zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
