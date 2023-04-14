#!/usr/bin/python3
# 4-inherits_from.py

def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class

       Args:
          obj(object): The object
          a_class(class): The class
       Return:
           True if instance otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
