#!/usr/bin/python3
# file: 3-square.py
# Auth: kelechi nnadi <@alx swe>

"""class definition"""


class Square:
    """a class representing a square.

    Attributs:
    __six (int): the size of the square.

    Methods:
        area(): calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initializes a square instance.

        Args:
            size (int): the size of the square

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
            calculates and returns the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
