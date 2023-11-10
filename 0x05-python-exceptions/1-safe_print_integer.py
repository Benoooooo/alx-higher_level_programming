#!/usr/bin/python3
# file: 1-safe_print_integer.py
# Auth: kelechi nnadi <@alx swe>

def safe_print_integer(value):
    try:
        print('{:d}'.format(value))
        return True
    except ValueError:
        return False
