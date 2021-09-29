"""
defining a class named square
with a private instance size
"""
class Square:
    """
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise ValueError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """
        this functions calculates and returns
        the are a of a square
        """
        return(self.__size * self.__size)
