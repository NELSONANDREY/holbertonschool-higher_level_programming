#!/usr/bin/python3
"""Module for print class empty
"""


class Square:
    """class empty"""
    def __init__(self, size=0):
        """generate atribute private
        self: """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    """calculate area of square"""
    def area(self):
        size = self.__size
        return size * size
