#!/usr/bin/python3
def fizzbuzz():
    for numerito in range(1, 101):
        if numerito % 3 == 0 and numerito % 5 == 0:
            print("FizzBuzz", end=" ")
        elif numerito % 5 == 0:
            print("Buzz", end=" ")
        elif numerito % 3 == 0:
            print("Fizz", end=" ")
        else:
            print(numerito, end=" ")
