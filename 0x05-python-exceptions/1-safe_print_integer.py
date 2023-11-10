#!/usr/bin/python3
# file: 1-safe_print_integer.py
# Auth: kelechi nnadi <@alx swe>

def safe_print_integer(value):
    """function that print an integer with "{}".format()"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
