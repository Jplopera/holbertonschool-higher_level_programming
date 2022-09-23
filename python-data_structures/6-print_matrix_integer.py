#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for v in range(len(x)):
            if v < (len(x) - 1):
                print("{:d} ".format(x[v]), end="")
            else:
                print("{:d}".format(x[v]), end="")
        print("")
