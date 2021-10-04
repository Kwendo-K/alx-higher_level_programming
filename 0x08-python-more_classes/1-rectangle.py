#!/usr/bin/python3
"""
a class of type rectangle
args: width, height
"""


class Rectangle:
    """initializing attributes
    args: width, height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """getter returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height if it's > 0"""
        if type(value) is not int:
            raise TypeError("height must be an int")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def width(self):
        """getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter sets width if its > 0"""
        if type(value) is not int:
            raise TypeError("width must be an int")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
