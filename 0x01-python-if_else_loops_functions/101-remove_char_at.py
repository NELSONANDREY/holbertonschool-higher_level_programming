#!/usr/bin/python3
def remove_char_at(str, n):
    sep = ""
    if len(str) >= n and n >= 0:
        for nu in str:
            if str[n] != nu:
                sep = sep + nu
    else:
        sep = str
    return(sep)
