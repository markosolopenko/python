def max_sum_seq(arr, num_range):
    array_size = len(arr)
    window_sum = sum([arr[i] for i in range(num_range)])
    max_sum = window_sum
    for i in range(array_size - num_range):
        window_sum = window_sum - arr[i] + arr[i+num_range]
        max_sum = max(max_sum, window_sum)
    return max_sum


if __name__ == '__main__':
    print(max_sum_seq([2, 1, 10, 8, 20, 3], 2))
