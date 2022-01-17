#!/usr/bin/python3
def safe_print_list(my_list=[], x=0)
    try:
        cinit = 0
        while cinit < x:
            print("{}".format(my_list=[cinit]), end=" ")
            cinit += 1
        print()
        return cinit
    except IndexError:
        print()
        return cinit
        pass

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

