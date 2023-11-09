#!/usr/bin/python3
# file: 0-safe_print_list.py
# Auth: kelechi nnadi <@alx swe>

def safe_print_list(my_list=[], x=0):
    """ function that prints x element of a list"""
    counter = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            counter += 1
        except IndexError:
            break

    print()
    return counter
