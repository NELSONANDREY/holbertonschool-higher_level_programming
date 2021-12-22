#!/usr/bin/python3
for nuo in range(ord('z'), ord('a') - 1, -1):
    if nuo % 2 != 0:
        nuo = nuo - 32
    print("{:c}".format(nuo), end="")
