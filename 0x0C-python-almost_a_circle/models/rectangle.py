#!/usr/bin/python3
from models.base import Base
"""define rectangle"""


class Rectangle(Base):
    """class rectangle definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The unique identifier of the rectangle.
        """
        super().__init__(id)
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    @property
    def width(self):
        """Get width"""
        return self._width

    @property
    def height(self):
        """Get height"""
        return self._height

    @property
    def x(self):
        """Get x"""
        return self._x

    @property
    def y(self):
        """Get y"""
        return self._y

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @x.setter
    def x(self, value):
        """Set x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self._x = value

    @y.setter
    def y(self, value):
        """Set y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self._y = value

    def area(self):
        """Calculate area"""
        return self._width * self._height

    def display(self):
        """Prints a text representation of this rectangle.
        """
        h_off = ' ' * self.x
        h_val = '#' * self.width
        print('\n' * self.y, end='')
        print('{:s}{:s}\n'.format(h_off, h_val) * self.height, end='')

    def _str_(self):
        """Creates a string representation"""
        parts = (
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
                )
        res = '[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}'.format(
                parts[0], parts[1], parts[2], parts[3], parts[4]
                )
        return res

    def update(self, *args, **kwargs):
        """Updates the attributes """
        attrs = ('id', 'width', 'height', 'x', 'y')
        for key, val in zip(attrs, args):
            setattr(self, key, val)
        if (type(args) is None or len(args) == 0) and (type(kwargs) is dict):
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Creates a dictionary"""
        res = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
        return res
