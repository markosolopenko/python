def find_missing_number(numbers):
    return sum(range(1, len(numbers) + 2)) - sum(numbers)


if __name__ == '__main__':
    print(find_missing_number([1, 2, 4]))
