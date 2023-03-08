#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lt_digit = (abs(number) % 10) * -1
else:
    lt_digit = number % 10
if lt_digit > 5:
    print(f"Last digit of {number} is {lt_digit} and is greater than 5")
elif lt_digit == 0:
    print(f"Last digit of {number:d} is {lt_digit:d} and is 0")
elif lt_digit < 6 and lt_digit != 0:
    print(f"Last digit of {number} is {lt_digit} is less than 6 and not 0")
