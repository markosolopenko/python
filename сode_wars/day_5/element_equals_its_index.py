# TODO: Check correctness

def index_equals_value(arr):
    lowest_index = []
    for char in range(len(arr)):
        if arr[char] == char:
            lowest_index.append(char)
    if lowest_index:
        return min(lowest_index)
    return -1


if __name__ == "__main__":
    print(index_equals_value((-5, 1, 2, 3, 4, 5, 7, 10, 15)))