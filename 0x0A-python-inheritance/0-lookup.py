#!/usr/bin/python3
# 0-lookup.py

def lookup(obj):
    """list available attribute and method of an object

       Args:
           obj(object): The object to return it's method and attribute
       Return:
           list of all attribute and method
    """
    all_method = dir(obj)
    return (all_method)
