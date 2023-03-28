#!/usr/bin/python3
def safe_print_integer(value):
    """
    safe_print_integer - function prints an integer with "{:d}".format()
    @value: can be any thing a string or integer
    """
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
