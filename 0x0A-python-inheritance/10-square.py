#!/usr/bin/python3
"""
Rectangle class cont.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Rectangle class that inherits BaseGeometry"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area of square"""
        return self.__size ** 2
