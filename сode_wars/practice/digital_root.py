def digital_root(number):
    # number = str(number)
    # sum_of_digits = 0
    # while len(number) != 1:
    #     for a in number:
    #         sum_of_digits += int(a)
    #     number = str(sum_of_digits)
    #     sum_of_digits = 0
    # return int(number)


    return number if len(str(number)) == 1 else digital_root(sum(map(int, str(number))))


if __name__ == '__main__':
    print(digital_root(459))


