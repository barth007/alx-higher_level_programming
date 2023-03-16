#!/usr/bin/python3
"""
def square_matrix_simple(matrix=[]):
    matrice = [[row[x] **2 for x in range(len(matrix))] for row in matrix]
    return matrice
#second method below
"""


def square_matrix_simple(matrix=[]):
    transposed = []
    for row in matrix:
        transposed_row = []
        for x in range(len(matrix)):
            transposed_row.append(row[x] ** 2)
        transposed.append(transposed_row)
    return transposed
