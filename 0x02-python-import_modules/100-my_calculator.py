#!/usr/bin/python3
# file: 100-my_calculator.py
# Auth: kelechi nnadi <@alx swe>

if __name__ == '__main__':
    """ program that imports all functions from the file
    calculator_1.py and handles basic opeations """
    import calculator_1

    n = len(sys.argv) - 1

    if n < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1
    elif 
