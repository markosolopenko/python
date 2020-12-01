from itertools import permutations
import re
with open('day3.txt', 'r') as file:
    numbers = file.read().split('\n')

first_index = []
second_index = []
third_index = []


def puzzle1():
    possible_triangles = 0
    for line in numbers:
        all_in_line = re.findall('[0-9]+', line)
        first, second, third = all_in_line
        first = int(first)
        second = int(second)
        third = int(third)
        if first + second > third and first + third > second and second + third > first:
            possible_triangles += 1
    print(possible_triangles)


def make_arrays():
    o = []
    t = []
    s = []
    for line in numbers:
        all_in_line = re.findall('[0-9]+', line)
        first, second, third = all_in_line
        if len(o) == 3:
            first_index.append(o)
            second_index.append(t)
            third_index.append(s)
            o = []
            t = []
            s = []
        o.append(int(first))
        t.append(int(second))
        s.append(int(third))
    first_index.append(o)
    second_index.append(t)
    third_index.append(s)


def puzzle2():
    make_arrays()
    possible_triangles = 0
    for f in first_index:
        first, second, third = f
        if first + second > third and first + third > second and second + third > first:
            possible_triangles += 1
    for s in second_index:
        first, second, third = s
        if first + second > third and first + third > second and second + third > first:
            possible_triangles += 1
    for t in third_index:
        first, second, third = t
        if first + second > third and first + third > second and second + third > first:
            possible_triangles += 1
    print(possible_triangles)


if __name__ == "__main__":
    # puzzle1()
    puzzle2()