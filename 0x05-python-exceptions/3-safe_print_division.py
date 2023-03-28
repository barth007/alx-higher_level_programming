#!/usr/bin/python3
def safe_print_division(a, b):
    """
    safe_print_division -function that divides 2 integers and prints the result
    @a & @b: an integer
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return ("{}".format(result))
