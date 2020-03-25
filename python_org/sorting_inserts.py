def sort_insert(matrix):
    list_to_sort = matrix
    for a in range(1, len(list_to_sort)):
        previous = a
        while previous > 0 and list_to_sort[previous - 1] > list_to_sort[previous]:
            list_to_sort[previous], list_to_sort[previous - 1] = list_to_sort[previous - 1], list_to_sort[previous]
            previous -= 1
    return list_to_sort



def main():
    list_to_sort = []
    rows = int(input('Enter number of rows: '))
    columns = int(input('Enter number of columns: '))
    for num in range(rows):
        lis = []
        for s in range(columns):
            lis.append(int(input()))
            if len(lis) == rows:
                print()
        list_to_sort.append(lis)
    some = 0
    print(f'Matrix before sort: ')
    for j in list_to_sort:
        print(j)
    while some != len(list_to_sort):
        for a in range(1, len(list_to_sort[some]) - 1):
            if list_to_sort[some][a] < list_to_sort[some][a-1] or list_to_sort[some][a] > list_to_sort[some][a+1]:
                sort_insert(list_to_sort[some])
                some += 1
            else:
                some += 1
    print(f'Sorted Matrix: ')
    for i in list_to_sort:
        print(i)


if __name__ == '__main__':
   main()