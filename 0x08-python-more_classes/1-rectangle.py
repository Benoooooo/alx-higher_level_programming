#!/usr/bin/python3
# kelechi nnadi <alx swe>
# 0-rectangle.py
"""empty class that defines
    the rectangle"""


class Rectangle:
    """this class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """init a Rectangle
        Args:
            width (int): width of the rectangle.
            height (int): height of a rectangle """

        self.width = width
        self.height = height

        @property
        def width(self):
            """ Gent width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """set the width of the rectangle

            Args:
              value (int): the new width value

            Raises:
                TypeError: if the value is not an integer.

            ValueError: if the value is not an than 0"""

            if type(value) is not int:
                raise TypeError("width must do the integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Get height of rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            """set the height of the rectangle

            Args:
              value (int): the new height value
            Raises:
                TypeError: if the value is not an integer.
            ValueError: if the value is less than 0."""

            if type(value) is not int:
                raise TypeError("width must do the integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
