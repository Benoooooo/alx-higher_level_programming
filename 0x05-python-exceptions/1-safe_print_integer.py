#!/usr/bin/python3
# file: 1-safe_print_integer.py
# Auth: kelechi nnadi <@alx swe>

def safe_print_integer(value):
    """function that print an integer with "{}".format()"""
    count = 0
    try:
        print("{:d}".format(value))
        count += 1
    except ValueError:
        pass
    return count
