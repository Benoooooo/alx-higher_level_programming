#!/usr/bin/python3
# 6-print_matrix_integer.py
# kelechi nnaid <alx swe africa>

def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers"""
    if not matrix:
        return

    for row in matrix:
        for i, num in enumerate(row):
            if i != 0:
                print(" ", end="")
            print("{:d}".format(num), end="")
        print()
