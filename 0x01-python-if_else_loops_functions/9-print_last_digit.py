#!/usr/bin/python3
# file: 9-print_last_digit.py
# Auth: kelechi nnadi <alx swe>

def print_last_digit(number):
    """function that print the last digit of a number"""
    last = abs(number) % 10
    if last > 0:
        print(last, end="")
    elif last == 0:
        print(last, end="")
    return last
