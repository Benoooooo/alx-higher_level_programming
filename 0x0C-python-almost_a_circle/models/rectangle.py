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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
            self.__width = value

        @height.setter
        def height(self, value):
            """set height"""
            self.__height = value

        @x.setter
        def x(self, value):
            """set x"""
            self.__x = value

        @y.setter
        def y(self, value):
            """set y"""
            self.__y = value
