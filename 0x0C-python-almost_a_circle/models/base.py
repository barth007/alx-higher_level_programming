#!/usr/bin/python3

class Base:
    """Defining a Base of a class

       Arguments:
           __nb_objects(int): represent id for every instance of class created
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize instance

           Args:
              id(int):an integer representing an id for an instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
