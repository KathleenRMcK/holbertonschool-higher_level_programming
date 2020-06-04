#!/usr/bin/python3
"""
Module for inheritence
"""


def inherits_from(obj, a_class):
    """Checks for direct and indirect inheritence"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
