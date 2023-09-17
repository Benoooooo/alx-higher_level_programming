#!/usr/bin/python3
# 7-add_tuple.py
# kelechi nnadi <alx swe school>

def add_tuple(tuple_a=(), tuple_b=()):
    """function that add 2 tuples"""

    res1 = tuple_a[0] + tuple_b[0]
    res2 = tuple_a[1] + tuple_b[1]
    tup = ()
    for i in tup:
        if i < 2:
            tup = i + 0
            return tup
        else:
            return tup
    return res1, res2

