from itertools import combinations


def choose_best_sum(t, k, ls):
    comb = combinations(ls, k)
    result = []
    for a in comb:
        if sum(a) <= t:
            result.append(sum(a))
    if result:
        return max(result)
    return None


if __name__ == '__main__':
    xs = [50, 55, 57, 58, 60]
    print(choose_best_sum(174, 3, xs))