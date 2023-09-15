#!/usr/bin/python3
#5-no_c.py
#kelechi nnadi <alx swe school>

def no_c(my_string):
    """function that removes all characters c
    and C from a string"""
    for i in my_string:
        if  i == 'c' or i == 'C':
            continue
        my_string[i]
        return my_string
