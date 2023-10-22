#!/usr/bin/python3
"""Define a function that writes  an Object to text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file

    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
