#!/usr/bin/python3
for ch in range(97, 123):
    lower_case = chr(ch)
    if lower_case != 'q' and lower_case != 'e':
        print("{}".format(lower_case), end="")
