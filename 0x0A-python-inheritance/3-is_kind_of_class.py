#!/usr/bin/python3
"""
Module cont.
"""


def is_kind_of_class(obj, a_class):
    """True on obj and class instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
