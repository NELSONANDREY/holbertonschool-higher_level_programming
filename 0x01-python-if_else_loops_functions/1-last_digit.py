#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    new = (((number * (- 1)) % 10) * -1)
else:
    new = number % 10
ls = "Last digit of"
if new > 5:
    print("{:s} {:d} is {:d} and is greater than 5".format(ls, number, new))
elif new == 0:
    print("{:s} {:d} is {:d} and is 0".format(ls, number, new))
elif new < 6 and new != 0:
    ln = "and is less than 6 and not 0"
    print("{:s} {:d} is {:d} {:s}".format(ls, number, new, ln))
