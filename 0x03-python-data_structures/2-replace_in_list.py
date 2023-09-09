#!/usr/bin/python3
# 2-replace_in_list.py
# kelechi nnadi <alx-swe africa>

def replace_in_list(my_list, idx, element):
    """function that replaces an element of a list
    at a specific position"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    for i in my_list:
        my_list[idx] = element
        return my_list
