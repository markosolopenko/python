def reverse(lst):
    empty_list = len(lst) *[None]
    decrease = -1
    for i in lst:
        empty_list[decrease] = i
        decrease -= 1
    return empty_list


if __name__ == '__main__':
    print(reverse([1, None, 14, 'two']))