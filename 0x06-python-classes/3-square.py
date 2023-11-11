#!/usr/bin/python3
# file: 3-square.py
# Auth: kelechi nnadi <@alx swe>

"""class definition"""


class Square:
    """ class defining the data of square"""

    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        """initializing the size of file if checked"""


    def area(self):
        """ check the area of the size and return
        """

        return self.__size ** 2
