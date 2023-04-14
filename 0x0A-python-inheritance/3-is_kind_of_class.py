#!/usr/bin/python3
# 3-is_kind_of_class.py

def is_kind_of_class(obj, a_class):
    """ checks if object is an instance of, of if object is an instance
        of an inherited class.

       Args:
           obj(object): object to check
           a_class(class): class to check
       Return:
           True if is an instance otherwise false
    """
    return isinstance(obj, a_class)
