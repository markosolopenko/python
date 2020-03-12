import numpy as np
def yes_no(arr: list) -> list:
    resalt = []
    a = 1
    while arr:
        if a == 1:
            some = first_index(arr)
            arr = cleaning(arr, some)
            resalt += some
            a = 2
        if a == 2:
            some = secon_index(arr)
            arr = cleaning(arr, some)
            resalt+=some
            a = 1
    return resalt




def first_index(arr):
    re_arranged = []
    for a in arr:
        if arr.index(a) % 2 == 0:
            re_arranged.append(a)
    return re_arranged
def secon_index(arr):
    re_arrange = []
    for a in arr:
        if arr.index(a) % 2 != 0:
            re_arrange.append(a)
    return re_arrange
def cleaning(arr_to_clear, arr_what_clear):
    for a in arr_to_clear:
        if a in arr_what_clear:
            arr_to_clear.remove(a)
    return arr_to_clear

if __name__ == "__main__":
    print(yes_no([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))