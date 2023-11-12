#!/usr/bin/python3
# file: 0-add_integer.py
# Auth: kelechi nnadi <@alx swe>
"""
This module defines a function called 'add_integer' that adds two numbers
result = add_integer(5, 3)
print(result)  # Output: 8
"""


def add_integer(a, b=98):
    """
    This is the docstring for the 'add_integer' function.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return (int(a) + int(b))
