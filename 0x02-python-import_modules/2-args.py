#!/usr/bin/python3
# file: 2-args.py
# Auth: kelechi nnadi <@alx swe>

import sys


def main():
    """ function that print the number of and list of
    arguments"""
    argv = sys.argv[1:]
    n = len(argv)

    if n == 0:
        print("0 argument(s).")
    elif n == 1:
        print("1 argument:")
        print("1: {} ".format(argv[0]))
    else:
        print("{} arguments:".format(n))
        for i, arg in enumerate(argv, start=1):
            print("{}: {} ".format(i, arg))


if __name__ == "__main__":
    main()
