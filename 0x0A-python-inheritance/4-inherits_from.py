#!/usr/bin/python3
"""Defines an inherited class_checking function"""


def inherits_from(obj, a_class):
    """Check if object is an inherted instance of class,

    args:
        abj: The object to check
        a_class: The class
    Returns:
        If obj is inherited instance of a_class - True
        otherwise - False
    """
    if issubclass(type(obj), a_class):
        return True
    return False
