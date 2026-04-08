#!/usr/bin/python3
"""Module that defines a Square class with comparison methods."""


class Square:
    """Represents a square with comparison capabilities."""

    def __init__(self, size=0):
        """Initializes the square."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if one square is less than another in area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if one square is less than or equal in area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if one square is greater than another in area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if one square is greater than or equal in area."""
        return self.area() >= other.area()
