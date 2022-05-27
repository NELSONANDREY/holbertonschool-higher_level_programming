#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Returns a maximum number from a list"""

    if len(list_of_integers) < 1:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
