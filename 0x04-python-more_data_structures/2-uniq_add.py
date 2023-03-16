#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    computes all unique integers in a list

    Args:
    my_list(list): this is a lisst

    Return:
    new_list[]
    """
    add_sum = 0
    new_list = set(my_list)
    for i in new_list:
        add_sum = add_sum + i
    return add_sum
