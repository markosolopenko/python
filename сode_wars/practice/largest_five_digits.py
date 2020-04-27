def solution(digits):
    arr_sum = []
    arr_string = []
    for i in range(len(digits)):
        if i == len(digits) - 4:
            break
        string = ''
        num = 0
        for j in range(i, i + 5):
            num += int(digits[j])
            string += digits[j]
        arr_sum.append(num)
        arr_string.append(string)

    while True:
        maximal = arr_string[arr_sum.index(max(arr_sum))]
        if find_max(maximal) == True:
            break
        arr_string.remove(maximal)
    return maximal


def find_max(maximal):
    for a in maximal:
        if maximal.count(a) > 1:
            return False
    return True


if __name__ == '__main__':
    print(solution('1234567898765'))