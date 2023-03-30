#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers.
       Args:
           my_list (list): The list to print elements from.
           x (int): The number of elements of my_list to print.
       Returns:
            The number of elements printed.
    """
    counter = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                counter += 1
        except (TypeError, ValueError):
            raise IndexError
    print(" ")
    return (counter)
