#!/usr/bin/python3
# file: 3-infinite_add.py
# Auth: kelechi nnadi <@alx swe>

import sys
import math

if __name__ == '__main__':
    if len(sys.argv) > 1:
        result = 0
        for arg in sys.argv[1:]:
            result += int(arg)
        print(result)
    else:
        print(0)
