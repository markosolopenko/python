import math

import numpy as np


def f(x):
    return math.sqrt(1 + x) - 1


def f_modified(x):
    return math.sqrt(1 + x) - 1


if __name__ == "__main__":
    print(f(1e-15))
    print(f_modified(1e-15))
