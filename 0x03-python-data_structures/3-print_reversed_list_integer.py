#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# kelechi nnadi <alx swe africa>

def print_reversed_list_integer(my_list=[]):
    """function that print the list in reverse
    order"""
    if my_list == "":
        return None
    for i in my_list[::-1]:
        print('{:d}'.format(i))
