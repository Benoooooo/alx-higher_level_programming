#!/usr/bin/python3
# file: 3-say_my_name.py
# kelechi nnadi <@alx swe>
"""function that prints a string"""


def say_my_name(first_name, last_name=""):
    """say my name function that takes two parameter
    firstname: the firstname of the person
    lastname: the lastname of the person
    """
    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print(" My name is {} {}".format(first_name, last_name))
