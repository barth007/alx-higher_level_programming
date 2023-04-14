#!/usr/bin/python3
# 2-is_same_class.py

def is_same_class(obj, a_class):
    """checks if object is exactly an instance of a class

       Args:
           obj(object): object to check
           a_class(class): class to check
       Return:
           True if obj an instance or false if otherwise
    """
    check = type(obj) is a_class
    return (check)
