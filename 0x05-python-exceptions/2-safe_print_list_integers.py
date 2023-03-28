#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - function that prints the
        first x elements of a list and only integers
    @my_list: can contain any type integer, string.
    @x: number of elements to access in my_list
    """
    counter = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except ValueError:
           raise IndexError
    print(" ")
    return (counter)
