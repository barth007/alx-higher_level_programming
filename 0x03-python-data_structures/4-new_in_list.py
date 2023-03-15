#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        copied_list = my_list.copy()
        copied_list.pop(idx)
        copied_list.insert(idx, element)
        return copied_list
