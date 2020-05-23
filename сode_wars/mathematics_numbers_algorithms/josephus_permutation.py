def josephus(xs, k):
    i, ys = 0, []
    while len(xs) > 0:
        i = (i + k - 1) % len(xs)
        ys.append(xs.pop(i))
    return ys


if __name__ == '__main__':
    print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
    # [1, 3, 5, 7, 9]
    # [1, 5, 9]
    # [1, 9]
    # [1]