# import math
# result = {1:1.414213, 10:1.478197, 40:1.478896}
# def len_curve(n):
#     return result.get(n, 1.478942)
# print(len_curve(1))

import math

def y(x):
    return x * x


def distance(a, b):
    xa, ya = a
    xb, yb = b
    d = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
    return d


def len_curve(n: int, interval_begin: float = 0, interval_end: float = 1, parabola=y) -> float:
    """
    finds an approximation of the length of the given function on given interval approximated by
    n points
    :param n:
    :param interval_begin:
    :param interval_end:
    :param parabola:
    :return:
    """
    points = []

    interval_len = interval_end - interval_begin

    for i in range(0, n + 1):
        x = interval_begin + i * (interval_len / n)
        y = parabola(x)
        points.append((x, y))

    total_distance = 0

    for idx in range(len(points) - 1):
        a = points[idx]
        b = points[idx + 1]
        d = distance(a, b)
        # print(f'Distance between {a} and {b} is {d}')
        total_distance += d

    return total_distance

for n in range(1, 100):
    print(len_curve(n))


