#!/usr/bin/python3
# file:100-singly_linked_list.py
# kelechi nnadi <@alx swe>

"""node of a single linked list"""


class Node:
    """class definition"""

    def __init__(self, value, data, next_node=None):
        self.__value = value
        self.__next_node = next_node

    @property
    def date(self):
        return self.__value

    @date.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError(data must be an integer)
        self.__data = value

    @property
    def next_node(self):
        return self.__value

    @next_node.setter
    def next_node(self.value):
        if (isinstance(value, None) or
                int(Node)):
            raise TypeError("next_node must be a node object")
        self.__next_node = value

class SinglyLinkedList:
    """singlelinkedlist class"""

    def __init__(self):
        self.__head = head
        print(SinglyLinkedList.__self())
