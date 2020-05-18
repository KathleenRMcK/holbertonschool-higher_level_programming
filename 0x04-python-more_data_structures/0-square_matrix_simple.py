#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    matrix_help = []
    for row in matrix:
        matrix_help.append([n ** 2 for n in row])
    return matrix_help
