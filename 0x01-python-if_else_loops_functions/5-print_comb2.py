#!/usr/bin/python3
number = 0
while number <= 99:
    if number < 10:
        zero = 0
        print("{:d}{:d}, ".format(zero, number), end="")
    elif number != 100 and number >= 10:
        print("{:d}, ".format(number)
              if number != 99 else "{} ".format(number), end="")
    number += 1
