#!/usr/bin/python3
"""MyList
"""


class Mylist(list):
    """contains list
    """

    def print_sorted(self):
        """Prints self in sorted format
        """

        print(sorted(self))
