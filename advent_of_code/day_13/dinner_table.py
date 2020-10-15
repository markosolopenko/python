from itertools import permutations
import re


all_connections = dict()
people_attendees = []


def parse_table():
    file = open('day13.txt').read().split('\n')
    global all_connections
    global people_attendees
    connections = []
    for line in file:
        if 'gain' in line:
            line = line.replace('gain ', '')
        elif 'lose' in line:
            line = line.replace('lose ', '-')
        line = line.replace('.', '')
        connections.append(re.split(' would | happiness units by sitting next to ', line.strip()))
    for connection in connections:
        guy_from, number, guy_to = connection
        all_connections[(guy_from, guy_to)] = int(number)
        people_attendees.append(guy_from)
    people_attendees = list(set(people_attendees))


def get_scenario(permutation):
    scenario = 0
    for i in range(len(permutation)):
        if i == len(permutation) - 1:
            scenario += all_connections[(permutation[i], permutation[0])] + all_connections[(permutation[0], permutation[i])]
        else:
            scenario += all_connections[(permutation[i], permutation[i+1])] + all_connections[(permutation[i+1], permutation[i])]
    return scenario


def add_myself_to_the_table():
    with open('day13.txt', 'w') as file:
        for i in file:
            file.write('')


def puzzles():
    scenarios = []
    parse_table()
    for permutation in permutations(people_attendees):
        scenarios.append(get_scenario(permutation))
    print(max(scenarios))


if __name__ == '__main__':
    add_myself_to_the_table()
    # puzzles()