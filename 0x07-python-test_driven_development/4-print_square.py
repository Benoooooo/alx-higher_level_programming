#!/usr/bin/python3
# file: 4-print_square.py
# Auth: kelechi nnadi <@alx swe>
"""function that prints a square with the character #"""

def print_square(size):
    """print square"""

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) < 0:
        raise TypeError("size must be an integer")
    sq = "#"
    for i in range(size):
        print(sq[i], end="")
