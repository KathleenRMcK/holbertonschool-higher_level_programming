#!/usr/bin/python3
"""
MyList Module
"""


class MyList(list):
    """class called MyList"""
    def print_sorted(self):
        """allowed ascending sort"""
        print(sorted(self))
