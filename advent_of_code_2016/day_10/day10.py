import re
from collections import defaultdict


with open('puzzle.txt', 'r') as file:
    instructions = file.read().splitlines()

bots_with_values = [line.split() for line in instructions if line.startswith('value')]
commands = [line.split() for line in instructions if not line.startswith('value')]


connections = {}


def find_connections():
    for line in commands:
        name, low, high = line[1], line[5:7], line[-2:]
        connections[name] = (low, high)


bots = defaultdict(list)
outputs = defaultdict(list)
stack = []


def add_value(name, value):
    bots[name].append(value)
    if len(bots[name]) == 2:
        stack.append(name)


def send_value(value, connection):
    if connection[0] == 'bot':
        add_value(connection[1], value)
    elif connection[0] == 'output':
        outputs[connection[1]] = value


def find_bots_with_values():
    for line in bots_with_values:
        value, name = int(line[1]), line[-1]
        add_value(name, value)


def puzzle1():
    wanted_bot = ''
    find_connections()
    find_bots_with_values()
    while stack:
        name = stack.pop()
        low_bot, high_bot = sorted(bots[name])
        low_connection, high_connection = connections[name]
        if low_bot == 17 and high_bot == 61:
            wanted_bot = name
        send_value(low_bot, low_connection)
        send_value(high_bot, high_connection)
    print(wanted_bot)


def puzzle2():
    s = ['0', '1', '2']
    sum_of_outputs = 1
    for i in outputs:
        if i in s:
            sum_of_outputs *= outputs[i]
    print(sum_of_outputs)


if __name__ == '__main__':
    puzzle1()
    puzzle2()