#!/usr/bin/python3
# 9-divisible_by_2.py
# kelechi nnadi <alx swe africa>

def divisible_by_2(my_list=[]):
    """ function that finds all multiples of 2
    in a list"""

    for i in my_list:
        if i % 2 == 0:
            n = True
        else:
            u = False
            new_list = [n, u]
    return new_list
