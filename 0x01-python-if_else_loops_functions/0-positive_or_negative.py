#!/usr/bin/python3
import random
number = random.randint(-1, 10)
if number > 0:
    print(number,'is positive')
elif number < 0:
    print(number,'is nagative')
else:
    print(number,'is zero')
