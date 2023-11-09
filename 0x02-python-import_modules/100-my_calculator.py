#!/usr/bin/python3
# file: 100-my_calculator.py
# Auth: kelechi nnadi <@alx swe>

if __name__ == '__main__':
    """ program that imports all functions from the file
    calculator_1.py and handles basic opeations """
    import calculator_1
    import sys

    n = len(sys.argv) - 1

    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
    else:
       addi = lambda a, b: a + b
       subi = lambda a, b: a - b
       divi = lambda a, b: a / b
       muli = lambda a, b: a * b
       res = 0
       for i in sys.argv:
           res += int(i)
       if op != addi:
           print("Unknown operator. Available operators: +, -, * and /")
           print(1)
       elif op != subi:
           print("Unknown operator. Available operators: +, -, * and /")
           print(1)
       elif op != divi:
           print("Unknown operator. Available operators: +, -, * and /")
           print(1)
       elif op != muli:
           print("Unknown operator. Available operators: +, -, * and /")
           print(1)
       print("{} {} {} = {} ".format(a, op, b, calculator_1(a, b)))

