#!/usr/bin/python3
for nu in range(0, 9):
    for nu2 in range(nu + 1, 10):
        if nu == 8:
            print("{:d}{:d}".format(nu, nu2))
        else:
            print("{:d}{:d}".format(nu, nu2), end=", ")
