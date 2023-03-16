#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    finds the occurence of an element and replaced it with a new value

    Args:
    my_list: is the initial list.
    search: isthe element to replace in the list
    replace: is the new element

    Return: newlist[]
    new_list = []
    for elem in my_list:
        if elem == search:
            new_list.append(replace)
        else:
            new_list.append(elem)
    return new_list

    OR

    for i elem enumerate(my_list):
        if elem == search:
            my_list[i] = replace
    return my_list
    """
    new_list = [replace if elem == search else elem for elem in my_list]
    return new_list
