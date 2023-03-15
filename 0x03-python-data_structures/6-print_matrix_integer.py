#!/usr/bin/python3
"""
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end = " ")
        print()
"""


def print_matrix_integer(matrix=[[]]):
    [print(' '.join(['{:d}'.format(col) for col in row])) for row in matrix]
