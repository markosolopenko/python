import string


def find_number(last_name: str) -> str:
    numbers_book = string.ascii_uppercase
    run_time = 1
    mid = len(numbers_book) // 2
    for _ in last_name:
        if numbers_book.index(last_name[0]) > mid:
            numbers_book = numbers_book[mid:]
            mid = len(numbers_book) // 2
            run_time += 1
        elif numbers_book.index(last_name[0]) < mid:
            numbers_book = numbers_book[:mid]
            mid = len(numbers_book) // 2
            run_time += 1
        else:
            return f'For find your number "{last_name}" we should to do <{run_time}> operations'


if __name__ == '__main__':
    print(find_number('Nolopenko'))