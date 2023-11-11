#!/usr/bin/python3
# file: 3-square.py
# Auth: kelechi nnadi <@alx swe>

"""class definition"""


class Square:
    """a class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            calculates and returns the area of the area
        """
        return (self.__size * self.__size)
