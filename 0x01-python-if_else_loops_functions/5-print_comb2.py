#!/usr/bin/python3
for nu in range(0, 100):
    if nu == 99:
        print("{0:0=2d}".format(nu))
    else:
        print("{0:0=2d}".format(nu), end=", ")
