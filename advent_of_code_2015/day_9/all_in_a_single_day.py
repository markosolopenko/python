import re
from itertools import permutations

travel_routes = dict()


def find_cities(file):
    cities = [file[0].split()[0]]
    curr = cities[0]
    for i in file:
        i = i.split()
        if i[0] != curr:
            break
        if i[2] not in cities:
            cities.append(i[2])
    return cities


def find_distance():
    global travel_routes

    file = open('day9.txt').read().split('\n')
    routes = [re.split(" to | = ", line.strip()) for line in file]
    for i in routes:

        city_from, city_to, km = i
        travel_routes[(city_from, city_to)] = int(km)
        travel_routes[(city_to, city_from)] = int(km)


def get_distance(travel_route):
    distance = 0
    for i in range(len(travel_route) - 1):
        distance += travel_routes[(travel_route[i], travel_route[i+1])]
    return distance


def puzzles():
    find_distance()
    distances = []
    file = open('day9.txt').read().split('\n')
    cities = find_cities(file)

    for permutation in permutations(cities):
        distances.append(get_distance(permutation))

    print("min distance", min(distances))
    print("max distance", max(distances))


if __name__ == "__main__":
    puzzles()