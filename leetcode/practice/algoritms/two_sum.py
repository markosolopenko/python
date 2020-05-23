from typing import List


def two_sum(n: List[int], t: int) -> List[int]:
    for i in range(len(n)):
        if t - n[i] in n:
            if n.index(t - n[i]) == i:
                return [i + 1, n.index(t - n[i]) + 2]
            return [i + 1, n.index(t - n[i]) + 1]


if __name__ == '__main__':
    print(two_sum([0, 0, 0, 32], 0))