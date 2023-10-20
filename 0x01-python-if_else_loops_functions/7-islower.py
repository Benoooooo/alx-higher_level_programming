#!/usr/bin/python3
# file: 7-islower.py
# Auth: kelechi nnadi <alx swe>

def islower(c):
    """ function that return the lowercase charaters
    if c is lowercase return True else false"""
    if c >= str(ord("a")) and c < str(ord("z")):
        return True
    else:
        return False
