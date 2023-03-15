#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ' '
        for item in my_string:
            if item == 'c' or item == 'C':
                continue
            new_string += item
    return new_string
