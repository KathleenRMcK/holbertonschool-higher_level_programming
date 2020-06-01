#!/usr/bin/python3
"""
Define class Square
"""


class Square:
    """
    define class Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """inits square"""
        self.__size = size
        self.position = position

    def area(self):
        """square area"""
        return (self.__size ** 2)

    def my_print(self):
        """print info"""
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for help in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """square position"""
        return self.__position

    @position.setter
    """setter of position"""
    self.__position = value
    if not isinstance(value, tuple):

    @property
    def size(self):
        """size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
