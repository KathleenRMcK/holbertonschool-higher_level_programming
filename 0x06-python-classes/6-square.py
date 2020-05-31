#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """square lives here"""

    def __init__(self, size=0):
        """it was born here"""
        self.__size = size
        self.position = position

    def area(self):
        """it lived here"""
        return (self.__size ** 2)

    def my_print(self):
        """here's it's story"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for help in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """here's his will"""
        return self.__position

    @position.setter
    """here's his address"""
    self.__position = value
    if not isinstance(value, tuple):

    @property
    def size(self):
        """here's his height and weight"""
        return self.__size

    @size.setter
    def size(self, value):
        """this is a square obit apparently"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
