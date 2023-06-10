#!/usr/bin/python3

def fizzbuzz():
    """fizzbuzz prints the number from 1 to 100 seperated by a space.
    """
    for i in range(1, 100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
