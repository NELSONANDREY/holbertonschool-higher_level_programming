#!/usr/bin/python3
for nu in range(0, 10):
    for nu2 in range(0, 10):
        if nu is 8 and nu2 is 9:
            print("{:d}{:d}".format(nu, nu2))
        elif nu < nu2:
            print("{:d}{:d}".format(nu, nu2), end=", ")
