#!/usr/bin/python3
"""Define Square Class"""

class square():
    """
    private instance class attribute for a square
    """

    def __init__(self, size=0):
        """

        Args:
            size: the size of square

        Raises:
            TypeError: exception
            ValueError: exception
        Return:
            None.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be <= 0")
        self.__size = size
