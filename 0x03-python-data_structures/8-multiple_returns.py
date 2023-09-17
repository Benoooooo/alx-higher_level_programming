#!/usr/bin/python3
# 8-multiple_returns.py
# kelechi nnadi <alx school africa>

def multiple_returns(sentence):
    """function that returns a tuple with tha length of a string
    and its first characteer"""

    if sentence == '':
        sentence[0] = None
        return tuple(sentence)
    else:
        t = sentence[0]
        r = len(sentence)
        res = (r, t)
        return res
