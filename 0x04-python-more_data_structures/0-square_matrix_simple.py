#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    computes the square value of all integers of a matrix.
    Args:
    matrix (list[list[int]]): A 2-dimensional matrix of integers.
    Returns:
    list[list[int]]: A new matrix of the same size as `matrix`.

    matrice = [[row[x] **2 for x in range(len(matrix))] for row in matrix]
    return matrice
    #second method below
    """


def square_matrix_simple(matrix=[]):
    """
    transposed = []
    for row in matrix:
        transposed_row = []
        for x in range(len(matrix)):
            transposed_row.append(row[x] ** 2)
        transposed.append(transposed_row)
    return transposed
    # third method
    """

    squared_rows = map(lambda row: list(map(lambda val: val**2, row)), matrix)
    return list(squared_rows)
