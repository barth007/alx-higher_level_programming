#!/usr/bin/python3
number1 = 0
while number1 < 10:
    number2 = number1 + 1
    while number2 < 10:
        if number1 != 8:
            print("{}{}, ".format(number1, number2), end="")
        else:
            print("{}{}".format(number1, number2))
        number2 += 1
    number1 += 1
