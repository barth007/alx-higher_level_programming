#!/usr/bin/python3
# 100-singly_linked_list.py
""" Represent of a Node"""

class Node:
    """ Define a Node

        Arguments:
            data(integer): The value to added the node
            next_node(Node): representing a node
    """
    def __init__(self, data, next_node=None):
        """ A constructor

            Args:
                data
                next_node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """A retriever method

           Return:
                the value set by the setter
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """Sets values of in a node

           Args:
               value(integer)
           Raise:
               TypeError
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        """retriever for next node
        """
        return(self.__next_node)
    @next_node.setter
    def next_node(self, value):i
        if value is not  None and not  isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        current_node = self.__head
        result = []
        while current_node is not None:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return ('\n'.join(result))

    def sorted_insert(self, value):
        new_node = Node(value)
        temp = self.__head

        if not self.__head:
            self.__head = new_node
            return
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        else:
            while not (temp.next_node is None)  and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

        
