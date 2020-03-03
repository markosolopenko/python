# import math
# def diagonal(row, index):
#     row= row+1
#     index = index+1
#     tb = math.factorial(row)/math.factorial(row-index)
#     tb = int(tb) / math.factorial(index)
#     return int(tb)


def pascal(c, r):
    if c == 0 or c == r:
        return 1
    else:
        return pascal(c - 1, r - 1) + pascal(c, r - 1)


def diagonal(n, p):
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


if __name__ == "__main__":

    print(diagonal(20,21))

    # print(diagonal(20, 3))

