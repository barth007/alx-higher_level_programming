#!/usr/bin/python3
# 2-matrix_divided.py

def matrix_divided(matrix, div):
    """divides element of a matrix with a divisor

       Args:
           martrix(list of lists(int/float)): containing list of lists
           div(float/int): The divisors
       Return:
           new_matrix = matrix[row][column]/div
       Raise:
          TypeError
          ZeroDivisionError
    """
    if not all(isinstance(row, list) and all(isinstance(element, (int, float))
                       for element in row)for row in matrix):
        raise TypeError("matrix must be a matrix
                        (list of lists) of integers/floats")
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return ([[round(matrix[row][column] / div, 2) for column in
                range(len(matrix[row]))] for row in range(len(matrix))])
