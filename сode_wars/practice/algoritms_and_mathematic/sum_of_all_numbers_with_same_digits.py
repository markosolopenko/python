from itertools import permutations
from math import factorial
import time


def sum_arr(num):
    return sum(map(lambda x: int(''.join(x)), list(permutations(list(str(num))))))


def sum_arrangements(num):
    num_str = str(num)
    length = len(num_str)
    total = 0

    c = factorial(length - 1) * sum(map(int, num_str))

    for i in range(length):
        total += c
        c *= 10

    return total


if __name__ == '__main__':
    sta1 = time.time()
    sum_arr(123)
    end1 = time.time()
    print(f'My is execution {end1 - sta1} second')

    sta2 = time.time()
    sum_arrangements(123)
    end2 = time.time()
    print(f'Andrey is execution {end2 - sta2} second')