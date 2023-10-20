#!/usr/bin/python3
# file: 8-uppercase.py
# Auth: kelechi nnadi <alx swe>

def uppercase(str):
    """ function that prints string in uppercase followed
    followed by a new line"""
    for i in str:
        print("{}".format(ord(i)), end="")
