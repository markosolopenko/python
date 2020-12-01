import numpy as np
import math


def func():
    min_presents = 34000000
    min_units = min_presents / 10

    max_num = int(min_units // 4)

    total = np.zeros(max_num + 1, dtype=int)

    for i in range(1, max_num + 1):
        n = max_num // i
        idx = i * np.array(range(1, n + 1))
        total[idx] += i * 10
    for i in range(1, max_num + 1):
        if total[i] >= min_presents:
            print("House {} got {} presents".format(i, total[i]))
            break


def part2():
    min_presents = 34000000
    min_units = min_presents / 10
    max_num = int(min_units // 4)

    total = np.zeros(max_num + 1, dtype=int)

    for i in range(1, max_num + 1):
        n = max_num // i
        if n > 50:
            n = 50
        idx = i * np.array(range(1, n + 1))
        total[idx] += i * 11

    for i in range(1, max_num + 1):
        if total[i] >= min_presents:

            print("House {} got {} presents".format(i, total[i]))
            break


if __name__ == '__main__':
    part2()
    # func()