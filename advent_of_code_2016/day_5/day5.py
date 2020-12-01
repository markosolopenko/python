from hashlib import md5


def solution_part1():
    result = ''
    start_int = 0

    while len(result) < 8:
        hexhash = md5(('ugkcyxxp' + str(start_int)).encode('ascii')).hexdigest()
        as_str = str(hexhash)

        if as_str.startswith('00000'):
            result += as_str[5]
        start_int += 1

    return result


if __name__ == '__main__':
    print(solution_part1())