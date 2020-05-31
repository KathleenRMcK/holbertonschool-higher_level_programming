#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """is square"""

    def __init__(self, size=0):
        """inits square"""
        self.__size = size

    def area(self):
        """area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints it all"""
        if self.__size == 0:
            print("")
        else:
            for help in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """get size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
