def insert_sort():
    array_of_elements = [4, 1, 7, 5, 3]
    for num in range(len(array_of_elements)):
        previous = num
        while previous > 0 and array_of_elements[previous] < array_of_elements[previous-1]:
            array_of_elements[previous], array_of_elements[previous-1] = array_of_elements[previous-1], array_of_elements[previous]
            previous -= 1
    return array_of_elements



if __name__ == '__main__':
    print(insert_sort())