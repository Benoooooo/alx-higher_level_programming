#!/usr/bin/python3
# file: 6-square.py
# Auth: kelechi nnadi <@alx swe>
""" define the 6-square.py class"""


class Square:
    """ class definition that houses
    all the data for the code and init

    __init__: initializing the value
    to private
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """get the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get the private instance attribuet position."""
        self.__position

    @position.setter
    def position(self, value):
        if (not isintance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int)for num in value) or
                any(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the current area of teh square."""
        self.__size ** 2

    def my_print(self):
        """print the square withe # character"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]

        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
