#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        cinit = 0
        while cinit < x:
            print("{}".format(my_list[cinit]), end=" ")
            cinit += 1
        print()
        return cinit
    except IndexError:
        print()
        return cinit
        pass
