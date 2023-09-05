#!/usr/bin/python3
import random
number = random.randint(-1, 10)
if number > 0:
    print('{} is positive'.format(number))
elif number < 0:
    print('{} is nagative'.format(number))
else:
    print('{} is zero'.format(number))
