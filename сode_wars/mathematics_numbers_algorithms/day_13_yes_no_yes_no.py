import numpy as np
# def yes_no(arr: list) -> list:
#     resalt = []
#     a = 1
#     while arr:
#         if a == 1:
#             some = first_index(arr)
#             arr = cleaning(arr, some)
#             resalt += some
#             a = 2
#         if a == 2:
#             some = secon_index(arr)
#             arr = cleaning(arr, some)
#             resalt+=some
#             a = 1
#     return resalt
#
#
#
#
# def first_index(arr):
#     re_arranged = []
#     for a in arr:
#         if arr.index(a) % 2 == 0:
#             re_arranged.append(a)
#     return re_arranged
# def secon_index(arr):
#     re_arrange = []
#     for a in arr:
#         if arr.index(a) % 2 != 0:
#             re_arrange.append(a)
#     return re_arrange
# def cleaning(arr_to_clear, arr_what_clear):
#     for a in arr_to_clear:
#         if a in arr_what_clear:
#             arr_to_clear.remove(a)
#     return arr_to_clear


def yes_no_generator(list_of_elements: list):

    if len(list_of_elements) > 0:

        next_iter = []

        for i, element in enumerate(list_of_elements):
            if i % 2 == 0:
                yield element
            else:
                next_iter.append(element)
        yield from yes_no_generator(next_iter)


def yes_no(list_of_elements: list) -> list:
    return [x for x in yes_no_generator(list_of_elements)]


def flatten(array):
    for element in array:
        if isinstance(element, list):
            yield from flatten(element)
        else:
            yield element


def parse_sentences_with_word(file_path, word):

    text = ''

    with open(file_path, 'r') as file:
        for line in file:
            text += line

    for sentence in text.split('.'):
        if word in sentence:
            yield sentence


if __name__ == "__main__":

    # array = [[1, 2, 3], [[[321321, 23232]]], 12, 232]
    # result = [1, 2, 3, 321321, 23232, 12, 232]
    #
    # print([x for x in flatten(array)])

    for i, x in enumerate(parse_sentences_with_word('data/green_mile.txt', 'me')):
        print(f'{i}: {x.strip()}')