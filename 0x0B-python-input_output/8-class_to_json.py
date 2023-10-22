#!/usr/bin/python3
""" function that returns the dictionary description
with simple data structure (list, dictionary, string,
integer and boolean) for JSON serialization of an object"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple
    data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: The dictionary

    """
    dic_attr = {}
    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            dic_attr[attr] = value
    return dic_attr
