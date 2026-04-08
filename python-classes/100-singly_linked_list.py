#!/usr/bin/python3
"""Module for a singly linked list."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets next_node with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes the linked list."""
        self.__head = None

    def __str__(self):
        """Defines the printable representation of the list."""
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position."""
        new_node = Node(value)

        # Siyahı boşdursa və ya yeni dəyər başdan kiçikdirsə
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Ortada və ya sonda uyğun yeri tapmaq
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
