#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
new = number % 10
if new > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, new))
elif new == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, new))
elif new < 6 and new != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, new))
