#!/usr/bin/python3
def max_integer(my_list=[]):
    long = len(my_list)
    if long > 0:
        maxm = my_list[0]
        for i in my_list:
            if i > maxm:
                maxm = i
    elif long == 0:
        return None
    return maxm
