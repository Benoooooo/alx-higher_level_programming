#!/usr/bin/python3
# Auth: kelechi nnadi <alx swe>
# file: 3-print_alphabt.py

for i in range(97, 123):
    if i == 113 or i == 101:
        continue
    print("{}".format(chr(i)), end="")
