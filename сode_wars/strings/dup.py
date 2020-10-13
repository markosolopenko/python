def dup(arry):
    for string in range(len(arry)):
        index = 0
        new_string = ''
        curr = ''
        for letter in arry[string]:
            if curr == letter:
                continue
            curr = letter
            index += 1
            new_string += letter
        arry[string] = new_string

    return arry


if __name__ == '__main__':
    print(dup(["ccooddddddewwwaaaaarrrrsssss","piccaninny","hubbubbubboo"]))
