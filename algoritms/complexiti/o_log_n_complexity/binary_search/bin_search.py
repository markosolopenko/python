import math


def bin_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = math.floor(left+(right-left)/2)

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    print(bin_search([1, 2, 3, 4, 5, 6], 6))