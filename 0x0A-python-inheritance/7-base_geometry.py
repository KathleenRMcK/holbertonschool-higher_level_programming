#!/usr/bin/python3
"""
class cont.
"""


class BaseGeometry():
    """BaseGeometry class init"""
    pass

    def area(self):
        """area exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """TypeError for not an int and
        ValueError for 0 or less"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
