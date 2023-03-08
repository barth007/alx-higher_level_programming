#!/usr/bin/python3
number = 0
while number <= 98:
    hexidecimal = hex(number)
    print("{} = {}".format(number, hexidecimal))
    number += 1
