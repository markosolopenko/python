from itertools import combinations, permutations

containers = [33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42]


def puzzles():
    all_com = []
    for i in range(len(containers)+1):
        com = combinations(containers, i)
        com_list = list(com)
        all_com += com_list
    c = 0
    a = []
    l = 1000
    for j in all_com:
        count = sum([i for i in j])
        if count == 150:
            l = min(l, len(j))
            a.append(j)
            c += 1
    min_length = l
    c2 = 0
    for i in a:
        if len(i) == min_length:
            c2 += 1
    print(f'puzzle1: {c}')
    print(f'puzzle2: {c2}')


if __name__ == '__main__':
    puzzles()