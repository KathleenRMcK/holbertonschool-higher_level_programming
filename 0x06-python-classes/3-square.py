#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """is a square"""

    def __init__(self, size=0):
        """inits a square"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """area of square"""
        return (self.__size ** 2)
