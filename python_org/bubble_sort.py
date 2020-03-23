def bubble_sort():
    list_to_sort = [20, 11, 2, 14, 8, 9, 21, 144]
    for i in range(len(list_to_sort)):
        for j in range(len(list_to_sort) - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
    print(list_to_sort)


if __name__ == '__main__':
    bubble_sort()