#!/usr/bin/python3

"""Defines a matrix division function"""


def matrix_divided(matrix, div):

    """Divides all elements of a matrix.

    Args:
        matrix(list): A list of lists of ints or floats.
        div(int/float): the divisor

    raises:
        TypeError: If the elements of the matrix are not numbers.
        TypeError: If matrix rows are not os same size.
        TypeError: If div is not a float or integer.
        ZeroDivisionError: If div is equal to zero.

    returns:
        A new matrix after the elements division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):

        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix:
       raise TypeError(
                "Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError(
                " div must be a number")
    if div == 0:
        raise ZeroDivisionError(
                "Division by zero")

    return([list(map(lambda x: round(x / 2, 2), row)) for row in matrix])
