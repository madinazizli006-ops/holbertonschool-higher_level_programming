#!/usr/bin/python3
"""Module that defines a Square class with __str__ method."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __str__(self):
        """Defines the string representation for printing."""
        res = ""
        if self.__size == 0:
            return res

        # Yuxarıdan boşluqlar
        res += "\n" * self.__position[1]

        # Kvadratın sətirləri
        for i in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                res += "\n"
        return res

    def my_print(self):
        """Prints the square to stdout."""
        print(self.__str__())
