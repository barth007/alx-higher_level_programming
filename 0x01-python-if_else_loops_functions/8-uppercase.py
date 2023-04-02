#!/usr/bin/python3
"""
uppercase - function prints a string in uppercase
@param str: argument to be convented to uppercase
"""


def uppercase(str):
    msg = ''
    for strs in str:
        if ord(strs) >= 97 and ord(strs) <= 122:
            strs = chr(ord(strs) - 32)
        msg = msg + strs
    print("{}".format(msg))
