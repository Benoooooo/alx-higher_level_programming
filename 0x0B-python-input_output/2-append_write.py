#!/usr/bin/python3
"""Define function that appends string at the end of text  file"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and
    returns the number of characters added.

    Args:
        filename (str): The text file to append to. Defaults to "".
        text (str): The string to append to the file. Defaults to "".

    Returns:
        int: The number of characters added to the file.

    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
