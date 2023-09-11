#!/usr/bin/python3
# 4-new_in_list.py
# kelechi nnadi <alx swe africa>

def new_in_list(my_list, idx, element):
    """function that replaces an element in a list at a specific
    position without modifying the original list"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
