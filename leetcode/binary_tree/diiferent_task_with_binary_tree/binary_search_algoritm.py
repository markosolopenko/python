def binary_search():
    list_of_elements = list(range(1000 + 1))

    user_number = int(input(f"please put a number! from range({list_of_elements[0]} to {list_of_elements[-1]}) "))
    switch = True
    times_to_find = 0
    num = (len(list_of_elements) - 1) / 2
    mid = list_of_elements[int(num)]
    while switch:
        # ask = input(f"(Your number is > {mid} or <) "
        #             f" IF {mid} is your number put True ")
        # if ask == "True" or mid == user_number:
        #     times_to_find += 1
        #     switch = False
        if mid == user_number \
                or list_of_elements[0] == user_number \
                or list_of_elements[-1] == user_number:
            times_to_find += 1
            switch = False
        else:
            # if ask == '>':
            if user_number > mid:
                list_of_elements = list_of_elements[int(num)+1:]
                num = (len(list_of_elements)-1) / 2
                mid = list_of_elements[int(num)]
                times_to_find += 1
            elif user_number < mid:
            # elif ask == '<':
                list_of_elements = list_of_elements[:int(num)+1]
                num = (len(list_of_elements) - 1) / 2
                mid = list_of_elements[int(num)]
                times_to_find += 1

    return times_to_find






def binary_search_number(list_of_numbers, item):
    low = 0
    high = len(list_of_numbers) - 1

    while low <= high:
        mid = low + high
        guess = list_of_numbers[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    print(binary_search_number([1, 3, 5, 9, 7], 9))
    # print(binary_search())