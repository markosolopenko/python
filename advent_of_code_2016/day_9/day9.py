import re


with open('input.txt', 'r') as file:
    inputs = file.read()


def puzzle1():
    amount_of_letters, times_to_repeat = 0, 0
    marker = ''
    start_from = 0
    decompressed_line = ''
    index = 0
    while index <= len(inputs) - 1:
        if inputs[index] == '(' and amount_of_letters == 0:
            for i in range(index+1, len(inputs)):
                if inputs[i] == ')':
                    start_from = i+1
                    break
                else:
                    marker += inputs[i]
            amount_of_letters, times_to_repeat = map(int, marker.split('x'))
            marker = ''
        else:
            if amount_of_letters != 0:
                line_to_compress = inputs[start_from:amount_of_letters+start_from]
                decompressed_line += line_to_compress * times_to_repeat
                index = amount_of_letters+start_from
                amount_of_letters, times_to_repeat = 0, 0
            else:
                decompressed_line += inputs[index]
                index += 1
    print(len(decompressed_line))


pattern = re.compile('\((\d+)x(\d+)\)')


def smart_solution(s, second_part=False):
    parens = pattern.search(s)
    if not parens:
        return len(s)
    length = int(parens.group(1))
    times = int(parens.group(2))
    start = parens.start() + len(parens.group())
    count = smart_solution(s[start:start+length], True) if second_part else length
    return (len(s[:parens.start()]) + times * count + smart_solution(s[start+length:], second_part))


if __name__ == '__main__':
   # puzzle1()
   print(smart_solution(inputs, second_part=True))