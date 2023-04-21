#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __str__(self):
        node = self._head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self._head is None:
            self._head = new_node
            return
        elif self._head.data > value:
            new_node.next_node = self._head
            self._head = new_node
            return
        else:
            current_node = self._head
            while current_node.next_node is not None and current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

