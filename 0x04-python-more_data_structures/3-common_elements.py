#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    the function returns a set of common elements in two sets

    Args:
    set_1(set): the first set
    set_2(set): the second set

    Return:
    sets of common in both sets

    new_list = []
    for item in set_1:
        if item in set_2:
            new_list.append(item)
    return new_list
    """
    new_list = [item for item in set_1 if item in set_2]
    return new_list
