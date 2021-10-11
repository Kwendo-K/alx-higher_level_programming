#!/usr/bin/python3
"""
a class called MYlist that inherits from list
"""


class MyList(list):
    """
    this class inherits from list
    methods: print_sorted
    """

    def print_sorted(self):
        """returns list in ascending order"""
        print(sorted(self))
