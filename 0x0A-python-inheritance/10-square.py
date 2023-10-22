#!/usr/bin/python3
"""Define a Rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __int__(self, size):
        """ Initialize a new square."""

        self.integer_validator("size", size)
        super().__init(size, size)
        self.__size = size
