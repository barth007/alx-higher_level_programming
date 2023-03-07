#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt_digit = number % 10
if lt_digit > 5:
    print(f"Last digit of {number:d} is {lt_digit:d} and is greater than 5")
elif lt_digit == 0:
    print(f"Last digit of {number:d} is {lt_digit:d} and is 0")
elif lt_digit < 6 and lt_digit != 0:
    print(f"Last digit of {number:d} is {lt_digit:d} and is less than 6")
