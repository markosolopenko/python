import re

unknown_aunt = {'children': '3', 'cats': '7', 'samoyeds': '2', 'pomeranians': '3', 'akitas': '0',
                    'vizslas': '0', 'goldfish': '5', 'trees': '3', 'cars': '2', 'perfumes': '1'}


def parse_file():
    file = open('day16.txt').read().split('\n')
    aunts = {}
    aunts_info = {}
    num = 1
    for line in file:
        line = re.findall('[a-z]+: [0-9]+', line)
        aunts[str(num)] = aunts_info
        for i in line:
            i = i.split(': ')
            aunts_info[i[0]] = i[-1]
        num += 1
        aunts_info = {}
    return aunts


def add_full_info():
    global unknown_aunt
    aunts_info = parse_file()

    for info in aunts_info:
        for key, value in unknown_aunt.items():
            if key not in aunts_info[info]:
                aunts_info[info][key] = value
    return aunts_info


def puzzle1():
    nearest = {}
    count = 0
    full_info = add_full_info()
    for info in full_info:
        for key, value in unknown_aunt.items():
            if unknown_aunt[key] == full_info[info][key]:
                count += 1
        nearest[info] = count
        count = 0
    max_key = ''
    max_value = max(nearest.values())
    for i in nearest:
        if nearest[i] == max_value:
            max_key = i
            break
    print(f'Puzzle1: {max_key}')


def puzzle2():
    nearest = {}
    count = 0
    not_allowed = ['cats', 'pomeranians', 'trees', 'goldfish']
    full_info = parse_file()
    for info in full_info:
        for key, value in unknown_aunt.items():
            if key == 'cats' and key in full_info[info] and int(full_info[info][key]) > int(value):
                count += 1
            elif key == 'trees' and key in full_info[info] and int(full_info[info][key]) > int(value):
                count += 1
            elif key == 'pomeranians' and key in full_info[info] and int(full_info[info][key]) < int(value):
                count += 1
            elif key == 'goldfish' and key in full_info[info] and int(full_info[info][key]) < int(value):
                count += 1
            elif key not in not_allowed and key in full_info[info] and value == full_info[info][key]:
                count += 1
        nearest[info] = count
        count = 0

    max_key = ''
    max_value = max(nearest.values())
    for i in nearest:
        if nearest[i] == max_value:
            max_key = i
            break
    print(f'Puzzle2: {max_key}')


if __name__ == '__main__':
    puzzle1()
    puzzle2()

