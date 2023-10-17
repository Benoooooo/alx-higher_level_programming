#!/usr/bin/python3
# kelechi nnadi <alx swe>
"""create rectangle"""
import unittest
from .base import Base


class Rectangle(Base):
    """class rectangle definintion"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            y (int, optional): The y-coordinate of the rectangle's position..
            id (int, optional): The unique identifier of the rectangle.

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """get width"""
            return self.__width

        @property
        def height(self):
            """get height"""
            return self.__height

        @property
        def x(self):
            """get x"""
            return self.__x

        @property
        def y(self):
            """get y"""
            return self.__y

        @width.setter
        def width(self, value):
            """set width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """set height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @x.setter
        def x(self, value):
            """set x"""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            """set y"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """calculate area"""
            return self.width * self.height
