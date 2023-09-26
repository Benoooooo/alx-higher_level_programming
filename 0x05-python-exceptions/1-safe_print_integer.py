#!/usr/bin/python3
def sefe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
