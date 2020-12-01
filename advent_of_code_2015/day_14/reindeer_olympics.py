# import re
# from pprint import pprint
#
#
# def parse_table():
#     file_text = open('day14.txt').read().split('\n')
#     reindeer_info = []
#     for line in file_text:
#         line = re.sub('for | seconds', '', line)
#         reindeer_info.append(re.split(' can fly | but then must rest ', line.strip()))
#     info = []
#     for reindeer in reindeer_info:
#         name = reindeer[0]
#         speed = reindeer[1].split()[0]
#         run_time = reindeer[1].split()[-1].split(',')[0]
#         rest_time = reindeer[-1].split('.')[0]
#         total_time = 0
#         total_km = 0
#         info.append([name, speed, run_time, rest_time, total_time, total_km])
#     return info
#
#
# def puzzle1():
#     time_to_fly = 2503
#     info = parse_table()
#     is_true = False
#     while is_true is not True:
#         for i in info:
#             km_run = int(i[1]) * int(i[2])
#             count = int(i[2]) + int(i[3])
#             if i[4] + count >= time_to_fly and i[0] is not True:
#                 lost = time_to_fly - i[4]
#                 if lost < int(i[2]):
#                     km_run = (int(i[2]) - lost) * int(i[1])
#                     i[-1] = int(i[-1]) + km_run
#                     i[0] = True
#                     i[4] = time_to_fly
#                 else:
#                     i[-1] = int(i[-1]) + km_run
#                     i[0] = True
#                     i[4] = time_to_fly
#             elif i[0] is not True:
#                 i[4] = i[4] + count
#                 i[-1] = int(i[-1]) + km_run
#         for j in info:
#             if j[0] is not True:
#                 is_true = False
#                 break
#             else:
#                 is_true = True
#     print(max([i[-1] for i in info]))
#
#
# def puzzle2():
#     time_to_fly = 1000
#     info = parse_table()
#     for i in range(time_to_fly):
#         distances = [int(i[1]) for i in info]
#
#
# if __name__ == '__main__':
#     # puzzle1()
#     puzzle2()
#     # Comet 140
#     # Dancer 176

from typing import List

# deer: List[str, int, int, int] = []


def parse_input():
    global deer

    lines = [line.split(" ") for line in open("day14.txt").readlines()]
    deer = [[line[0], int(line[3]), int(line[6]), int(line[13])] for line in lines]


def traveled_after(deer_info, num_seconds):
    distance = 0
    total_seconds = 0
    distances = []

    while True:
        for i in range(deer_info[2]):
            total_seconds += 1
            if total_seconds > num_seconds:
                return distance, distances
            distance += deer_info[1]
            distances.append(distance)

        for i in range(deer_info[3]):
            total_seconds += 1
            if total_seconds > num_seconds:
                return distance, distances
            distances.append(distance)


def puzzles():
    parse_input()
    max_distance = 0
    all_distances = []
    for doe in deer:
        distance, distances = traveled_after(doe, 2503)
        all_distances.append(distances)
        if distance > max_distance:
            max_distance = distance

    print("max distance:", max_distance)

    num_deer = len(deer)
    deer_points = [0] * num_deer
    for i in range(2503):
        second_distances = [all_distances[j][i] for j in range(num_deer)]
        best_distance = max(second_distances)
        leaders = [i for i, x in enumerate(second_distances) if x == best_distance]
        for doe in leaders:
            deer_points[doe] += 1

    print("max points:", max(deer_points))


if __name__ == "__main__":
    puzzles()
