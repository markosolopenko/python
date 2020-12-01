import re
from string import ascii_lowercase

with open('day_4.txt', 'r') as file:
    encrypted_text = file.read().split('\n')


def count_characters(line):
    s = {}
    alphabet = ascii_lowercase
    for i in line:
        if i in alphabet:
            if i in s:
                s[i] = s[i] + 1
            else:
                s[i] = 0
    return s


def puzzle1():
    numbers = []
    for line in encrypted_text:
        s = re.findall('\[.+\]', line)
        line = line.replace(s[0], '')
        line = line.replace('-', '')
        is_true = True
        char_line = count_characters(line)
        for i in s[0]:
            if i not in '[]' and i not in line or i not in '[]' and char_line[i] < 0:
                is_true = False
                break

        if is_true:
            number = re.findall('[0-9]+', line)
            numbers.append(number[0])
    print(sum([int(i) for i in numbers]))


if __name__ == '__main__':
    puzzle1()