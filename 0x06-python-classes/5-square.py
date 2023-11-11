#!/usr/bin/python3
# file: 5-square.py
# Auth: kelechi nnadi <@alx swe>

"""define the 4 square"""


class Square:
    """class definition of private instance attributs

    args:
        making the argument the main of the code
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must ve an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
