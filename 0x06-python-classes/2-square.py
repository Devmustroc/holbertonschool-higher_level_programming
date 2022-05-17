#!/usr/bin/python3
"""Define Square Class"""


class square():
    """
    private instance class attribute for a square
    """

    def __init__(self, size=0):
        """ function that create a square

        Args:
            size: the size of square

        Raises:
            TypeError: exception
            ValueError: exception
        Return:
            None.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
