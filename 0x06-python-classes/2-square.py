#!/usr/bin/python3
"""
This class defines a square with a private instance called size
"""


class Square:
    """
    class square defination
    arg: size
    """
    def __init__(self, size=0):
        """
        initializing square attributes
        Attribute: size
        """
        if type(size) is not int:
            raise ValueError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
