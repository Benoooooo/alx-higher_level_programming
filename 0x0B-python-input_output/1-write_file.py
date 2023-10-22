#!/usr/bin/python3
"""Define a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Reads a text file (UTF-8) and prints its content to stdout.
    If the file doesn't exist, it will be created.rgs:

    Args:
    filename (str): The path of the text file to write to. Defaults to "".
    text (str): The string to write to the file. Defaults to "".

    Returns:
    int: nunber of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
