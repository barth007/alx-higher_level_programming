#!/usr/bin/python3
number = 0
while number <= 99:
    if number < 99:
        zero = 0
        print("{:d}{:d}, ".format(zero, number)
              if number < 10 else "{}, ".format(number), end="")
    else:
        print("{:d}".format(number))
    number += 1
