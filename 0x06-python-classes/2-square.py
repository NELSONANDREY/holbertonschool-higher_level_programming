#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)
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
