def greatest_product(n):
    count = 0
    result = 0
    some_list = []
    check = []
    string = ''
    some = 0
    for a in n:
        if result == len(n) - 4:
            break
        else:
            for j in range(5):
                string += n[result]
                result += 1
            some += 1
            check.append(string)
            string = ''
            count += 1
            result = some
    multiply = 1
    for num in check:
        for element in num:
            multiply *= int(element)
        some_list.append(multiply)
        multiply = 1
    return some_list






if __name__ == '__main__':
    print(greatest_product("123834539327238239583"))
    # 3240