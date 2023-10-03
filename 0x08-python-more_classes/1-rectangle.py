#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Representing a rectangle."""

    def _init_(self, width=0, height=0):
        """Initialize a  Rectangle.

        Args:
            width(int): width of a rectangle
            hight(int): hieght of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get  width of the rectange"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the rectangle.

        Args:
            value (int): the new width value

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle.

        Args:
            value (int): the new height value

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
