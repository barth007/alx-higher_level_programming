#!/usr/bin/python3
def _len(my_list=[]):
    """
        _len - returns of a list
        @my_list: the list argument
    """
    a = 0
    for i in my_list:
        a = a + 1
    return (a)


def safe_print_list(my_list=[], x=0):
    """
        safe_print_list - a function that prints x elements of a list.
        @my_list: a list that can contain any type of data type
        @x: this is the number of element to prints
    """
    a = 0
    try:
        [print("{}".format(my_list[i]), end='') for i in range(x)]
        print("\n")
        return (x)
    except IndexError:
        print("\n")
        return (_len(my_list))
