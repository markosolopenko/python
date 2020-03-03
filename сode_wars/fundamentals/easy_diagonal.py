import math
def diagonal(row, index):
    row= row+1
    index = index+1
    tb = math.factorial(row)/math.factorial(row-index)
    tb = int(tb) / math.factorial(index)
    return int(tb)

# def binomialCoeff(n, k):
#     sums = 0
#     res = 1
#     if (k > n - k):
#         k = n - k
#     for i in range(0, k+1):
#         res = res * (n - i)
#         res = res // (i + 1)
#         sums += res
#
#     return sums

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
        print(f'Length: {len(triangle[i])}')
        if len(triangle[i]) >= p:
            print(f'Element: {triangle[i][p-1]}')
            summ += triangle[i][p-1]

    return summ


if __name__ == "__main__":

    print(diagonal(20,15))

    print(diagonal(20, 3))

