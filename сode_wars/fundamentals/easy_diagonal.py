# import math
# def diagonal(row, index):
#     row= row+1
#     index = index+1
#     tb = math.factorial(row)/math.factorial(row-index)
#     tb = int(tb) / math.factorial(index)
#     return int(tb)

import numpy as np
from pprint import pprint
import time


def pascal(c, r):
    if c > r:
        return 0
    elif c == 0 or c == r:
        return 1
    else:
        return pascal(c - 1, r - 1) + pascal(c, r - 1)

def diagonal(n, p):
    return sum([pascal(p, i) for i in range(1, n+1)])

def diagonal_inefficient(n, p):
    triangle = []

    for i in range(n + 1):
        row = []
        for j in range(0, i + 1):
            row.append(pascal(j, i))
        triangle.append(row)
    summ = 0

    for i in range(n + 1):
        if len(triangle[i]) > p:
            summ += triangle[i][p]

    return summ

def diagonal_with_numpy(n, p):
    triangle = np.zeros(shape=(n + 1, n + 1))

    for i in range(n + 1):
        for j in range(0, i + 1):
            triangle[i, j] = pascal(j, i)

    return np.sum(triangle[:, p])


if __name__ == "__main__":
    pass
    # s1 = time.time()
    #
    # print(diagonal(20, 5))
    #
    # s2 = time.time()
    #
    # print(f'Execution time: {s2 - s1}')
    #
    # s1 = time.time()
    #
    # print(diagonal_with_numpy(20, 5))
    #
    # s2 = time.time()
    #
    # print(f'Execution time: {s2 - s1}')
    #
    # s1 = time.time()

    # print(diagonal_efficient(20, 4))

    # s2 = time.time()

    # print(f'Execution time: {s2 - s1}')