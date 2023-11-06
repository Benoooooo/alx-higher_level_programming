#!/usr/bin/python3
# file: 1-calculation.py
# Auth: kelechi nnadi <@alx swe>

if __name__ == '__main__':
    """ function that dose some maths"""
    import math
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
