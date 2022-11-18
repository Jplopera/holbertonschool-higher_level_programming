#!/usr/bin/python3
"""Module that contains function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """divides all elements of a matrix."""
    len_column = len(matrix[0])
    erro_1 = 'matrix must be a matrix (list of lists) of integers/floats'
    erro_2 = 'Each row of the matrix must have the same size'

    for column in matrix:
        if len(column) != len_column:
            raise TypeError(erro_2)
        for row in column:
            if type(row) not in [int, float]:
                raise TypeError(erro_1)

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return (list(map(lambda x: list(map(lambda y:
                                        round(y / div, 2), x)), matrix)))
