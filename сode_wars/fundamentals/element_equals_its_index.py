import sys

sys.setrecursionlimit(1000000)


def index_equals_value(arr):
    lowest_index = []
    for char in range(len(arr)):
        if arr[char] == char:
            lowest_index.append(char)
    if lowest_index:
        return min(lowest_index)
    return -1


if __name__ == "__main__":
    print(index_equals_value((-1,0,3,6)))

    import sys

    sys.setrecursionlimit(1000000)

# I need your explain for this solution
# def index_equals_value(arr, i=0):
#     try:
#         if arr[i] == i:
#             return i
#         return index_equals_value(arr, i=i + 1)
#     except:
#         return -1