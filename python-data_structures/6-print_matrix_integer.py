#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(0, row):
        for j in range(0, col):
            endd = "" if j == col -1 else " "
            print("{:d}".format(matrix[i][j]), end=endd)
        print()
