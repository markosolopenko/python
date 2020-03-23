def sort_insert():
    list_to_sort = [5, 2, 1, 3, 4]
    for a in range(1, len(list_to_sort)):
        previous = a
        while previous > 0 and list_to_sort[previous - 1] > list_to_sort[previous]:
            list_to_sort[previous], list_to_sort[previous - 1] = list_to_sort[previous - 1], list_to_sort[previous]
            previous -= 1
    print(list_to_sort)




if __name__ == '__main__':
    sort_insert()