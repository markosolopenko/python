from typing import List


def select_sort(sequences_to_sort: List):
    sorted_list = []
    for i in range(len(sequences_to_sort)):
        smallest = find_smallest(sequences_to_sort)
        sorted_list.append(sequences_to_sort.pop(smallest))
    return sorted_list


def find_smallest(array):
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < array[smallest_index]:
            smallest_index = i
    return smallest_index


if __name__ == '__main__':
    print(select_sort([5, 3, 6, 2, 10]))
