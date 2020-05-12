def find_max(array, largest, i):
    if i == len(array):
        return largest
    elif array[i] > largest:
        largest = array[i]
        i += 1
        return find_max(array, largest, i)
    else:
        i += 1
        return find_max(array, largest, i)

# def find_max(array):
#     largest = 0
#     for i in range(len(array)):
#         if array[i] > largest:
#             largest = array[i]
#     return largest


if __name__ == '__main__':
    # print(find_max([12, 2, 3, 52, 128, 9, 21]))
    print(find_max([12, 2, 3, 52, 9, 21, 128], 0, 0))