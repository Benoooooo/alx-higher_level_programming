#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
#tr = f'{str[39:-63]} {str[107:-18]} {str[0:-122]}'
str = '{} {} {}'.format(str[39:-63], str[107:-18], str[0:-122])
print(str)
