#!/usr/bin/python3

def print_last_digit(number):
    """ print_last_digit: print the last digit of a number

        Args:
           number
    """
    if number < 0:
        number = abs(number)
    last_number = number % 10
    print("{:d}".format(last_number), end="")
    return last_number
