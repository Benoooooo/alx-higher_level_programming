#!/usr/bin/python3
# kelechi nnadi <alx swe>
# 0-rectangle.py
"""empty class that defines
    the rectangle"""


class Rectangle:
    """this class defines a rectangle"""


    def __init__(self, width=0, height=0):
        """init the width to 0 and the height to 0"""
        
        self.width = width
        self.height = height

        @property
        def width(self):
            
            return self.__width

        @width.setter
        def width(self, value):



            if type(value) is not int:
                raise TypeError("width must do the integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):

            return self.__width

        @width.setter
        def width(self, value):

            if type(value) is not int:
                raise TypeError("width must do the integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__height = value
