#!/usr/bin/python3
# 9-max_integer.py
# kelechi nnadi <alx swe africa>

def max_integer(my_list=[]):
    """ function that prints the biggest integer
    and not allowed to use max() function if the
    list is empty return  None"""

    largest = my_list[0]
    for i in range(1, len(my_list)):
        if i == []:
            return None
        if my_list[1] > largest:
            largest = my_list[i]
    return largest
