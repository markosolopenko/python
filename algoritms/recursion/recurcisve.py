def sum_recursive(arr, sum_of_numbers):
    if not arr:
        return sum_of_numbers
    else:
        sum_of_numbers += arr[0]
        return sum_recursive(arr[1:], sum_of_numbers)


if __name__ == '__main__':
    print(sum_recursive([2, 1, 3, 4, 5, 6, 7], 0))
