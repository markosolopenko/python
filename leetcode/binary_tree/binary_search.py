from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


if __name__ == '__main__':
    print(BinarySearch([-1,0,3,5,9,12], 2))