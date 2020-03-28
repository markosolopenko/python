# import numpy as np
# def min_num_taxis(requests):
#     r = np.zeros(10000)
#     for i, j in requests:
#         r[i: j+1] += 1
#     return int(max(r))
from heapq import heappush, heappop


def min_num_taxis(requests):
    taxis = [-1]
    for start, end in sorted(requests):
        if taxis[0] < start:
            heappop(taxis)
        heappush(taxis, end)
    return len(taxis)






if __name__ == '__main__':
    print(min_num_taxis([(1,2), (3, 4), (5, 6), (7, 8), (9, 10)]))
