#!/usr/bin/python3
# 1-element_at.py
# kelechi nnadi <alx-swe africa>

def element_at(my_list, idx):
    """function that retrieves an element from a list"""
    if idx < 0 and idx >= len(my_list):
        return None
    return my_list[idx]
