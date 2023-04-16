#!/usr/bin/python3
# 3-say_my_name.py

def say_my_name(first_name, last_name=""):
    """ print first and second argument to the stdout

        Args:
            first_name(str): first argument which is a string
            last_name(str): second argument which is a string
        Raise:
            TypeError
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
