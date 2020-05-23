import numpy as np


def split_and_add(numbers, n):
    if len(numbers) == 1:
        return numbers
    times = 0
    res = []
    while times != n:
        mid = len(numbers) // 2
        arr1 = numbers[:mid]
        arr2 = numbers[mid:]
        if len(arr1) > len(arr2):
            arr2 = [0]*(len(arr1) - len(arr2)) + arr2
        elif len(arr1) < len(arr2):
            arr1 = [0]*(len(arr2)-len(arr1)) + arr1
        for i in range(len(arr1)):
            res.append(arr1[i] + arr2[i])
        times += 1
        numbers = res
        res = []
    return numbers


if __name__ == '__main__':
    print(split_and_add([1, 2, 3, 4, 5], 2))