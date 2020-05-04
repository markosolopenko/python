def sort_number(a):
    a.sort()
    if a[-1] == 1:
        a[-1] = 2
        return sorted(a)
    a[-1] = 1
    return sorted(a)


if __name__ == '__main__':
    sort_number([1,2,3,4,5,6])