#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for x in range(0, len(matrix)):
            for y in range(0, matrix[x]):
                if y != len(matrix[x]) - 1:
                    print(matrix[x][y], end=" ")
                else:
                    print(matrix[x][y])
