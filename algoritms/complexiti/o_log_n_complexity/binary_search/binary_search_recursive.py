def binary_search_recursive(array, num, run_time):
    mid = len(array) // 2
    if array[mid] > num:
        run_time += 1
        return binary_search_recursive(array[:mid], num, run_time)
    elif array[mid] < num:
        run_time += 1
        return binary_search_recursive(array[mid:], num, run_time)
    else:
        return run_time


if __name__ == '__main__':
    print(binary_search_recursive(list(range(1, 200)), 20, 1))
