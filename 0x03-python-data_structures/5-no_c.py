#!/usr/bin/python3
# 5-no_c.py
# kelechi nnadi <alx swe school>

def no_c(my_string):
    """function that removes all characters c
    and C from a string"""
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return("".join(copy))
