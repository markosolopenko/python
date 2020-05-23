import string


# def find_number(last_name: str) -> str:
#     numbers_book = string.ascii_uppercase
#     run_time = 1
#     mid = len(numbers_book) // 2
#     for _ in last_name:
#         if numbers_book.index(last_name[0]) > mid:
#             numbers_book = numbers_book[mid:]
#             mid = len(numbers_book) // 2
#             run_time += 1
#         elif numbers_book.index(last_name[0]) < mid:
#             numbers_book = numbers_book[:mid]
#             mid = len(numbers_book) // 2
#             run_time += 1
#         else:
#             return f'For find your number "{last_name}" we should to do <{run_time}> operations'


def loop_binary_search(array, num_to_find):
    # mid = len(array) // 2
    # run_time = 1
    # for _ in array:
    #     ask = input("Your number > or < ")
    #     if array[mid] > num_to_find:
    #         array = array[:mid]
    #         mid = len(array) // 2
    #         run_time += 1
    #     elif array[mid] < num_to_find:
    #         array = array[mid:]
    #         mid = len(array) // 2
    #         run_time += 1
    #     else:
    #         return f'For find your number <{array[mid]}> we need <{run_time}> operations'

    mid = len(array) // 2
    run_time = 1
    while True:
        ask = input(f"Your number > or < that {array[mid]} ")
        if ask == '+':
            break
        elif ask == '<':
            array = array[:mid]
            mid = len(array) // 2
            run_time += 1
        elif ask == '>':
            array = array[mid:]
            mid = len(array) // 2
            run_time += 1
    return f'For find your number <{array[mid]}> we need <{run_time}> operations'


if __name__ == '__main__':
    print(loop_binary_search(list(range(1, 1000)), 20))
    # print(find_number('Nolopenko'))